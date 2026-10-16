from fastapi import status

def test_empty_analytics(client, auth_headers):
    response = client.get("/api/v1/analytics/", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["total_applications"] == 0
    assert data["active_applications"] == 0
    assert data["response_rate_pct"] == 0.0
    assert data["interview_conversion_pct"] == 0.0

def test_funnel_analytics_calculation(client, auth_headers, test_company):
    # Seed 5 applications across various pipeline stages
    statuses = [
        "applied",
        "screening",
        "technical_interview",
        "offer_received",
        "rejected"
    ]
    for idx, s in enumerate(statuses):
        client.post(
            "/api/v1/applications/",
            json={
                "company_id": test_company.id,
                "job_title": f"Software Engineer Role {idx}",
                "status": s
            },
            headers=auth_headers
        )

    response = client.get("/api/v1/analytics/", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert data["total_applications"] == 5
    assert data["active_applications"] == 4  # All except 'rejected'
    assert data["offers_received"] == 1
    assert data["rejections"] == 1
    assert data["response_rate_pct"] == 80.0  # 4/5 responded
    assert data["by_status"]["applied"] == 1
    assert data["by_status"]["offer_received"] == 1
    assert data["by_status"]["rejected"] == 1

def test_cross_user_analytics_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B's funnel metrics remain completely isolated from User A's applications."""
    # User A creates multiple applications across different stages
    stages = ["applied", "technical_interview", "offer_received"]
    for idx, s in enumerate(stages):
        client.post(
            "/api/v1/applications/",
            json={
                "company_id": test_company.id,
                "job_title": f"User A Analytics Test Role {idx}",
                "status": s
            },
            headers=auth_headers
        )

    # User B requests analytics - must remain 0 and completely isolated
    res_b = client.get("/api/v1/analytics/", headers=auth_headers_b)
    assert res_b.status_code == status.HTTP_200_OK
    data_b = res_b.json()
    assert data_b["total_applications"] == 0
    assert data_b["active_applications"] == 0
    assert data_b["offers_received"] == 0
    assert data_b["rejections"] == 0
    assert data_b["response_rate_pct"] == 0.0
    assert all(count == 0 for count in data_b["by_status"].values())
