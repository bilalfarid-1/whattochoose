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
