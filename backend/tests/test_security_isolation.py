from datetime import date
from fastapi import status

def test_user_b_cannot_get_user_a_application(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B receives 404 when attempting to access User A's application."""
    # User A creates an application
    create_resp = client.post(
        "/api/v1/applications/",
        json={
            "company_id": test_company.id,
            "job_title": "Backend Systems Engineer (Python)",
            "status": "applied"
        },
        headers=auth_headers
    )
    assert create_resp.status_code == status.HTTP_201_CREATED
    app_a_id = create_resp.json()["id"]

    # User B attempts to read User A's application
    read_resp = client.get(f"/api/v1/applications/{app_a_id}", headers=auth_headers_b)
    assert read_resp.status_code == status.HTTP_404_NOT_FOUND
    assert read_resp.json()["detail"] == "Application not found."

def test_user_b_cannot_modify_or_delete_user_a_application(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B cannot mutate or delete User A's application, and data integrity is preserved."""
    # User A creates application
    create_resp = client.post(
        "/api/v1/applications/",
        json={
            "company_id": test_company.id,
            "job_title": "Core Infrastructure Engineer",
            "status": "applied",
            "salary_range": "PKR 150k - 200k"
        },
        headers=auth_headers
    )
    app_a_id = create_resp.json()["id"]

    # User B attempts to PATCH User A's application
    patch_resp = client.patch(
        f"/api/v1/applications/{app_a_id}",
        json={"status": "offer_received", "job_title": "Malicious Tampering"},
        headers=auth_headers_b
    )
    assert patch_resp.status_code == status.HTTP_404_NOT_FOUND

    # User B attempts to DELETE User A's application
    del_resp = client.delete(f"/api/v1/applications/{app_a_id}", headers=auth_headers_b)
    assert del_resp.status_code == status.HTTP_404_NOT_FOUND

    # Verify User A's record was completely untouched
    verify_resp = client.get(f"/api/v1/applications/{app_a_id}", headers=auth_headers)
    assert verify_resp.status_code == status.HTTP_200_OK
    assert verify_resp.json()["status"] == "applied"
    assert verify_resp.json()["job_title"] == "Core Infrastructure Engineer"

def test_application_listing_multi_tenant_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure User A and User B only see their respective applications in index queries."""
    # User A creates 2 applications
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "User A App 1", "status": "applied"},
        headers=auth_headers
    )
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "User A App 2", "status": "screening"},
        headers=auth_headers
    )

    # User B creates 1 application
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "User B App 1", "status": "applied"},
        headers=auth_headers_b
    )

    # User A query
    list_a = client.get("/api/v1/applications/", headers=auth_headers).json()
    assert all("User A" in app["job_title"] for app in list_a)
    assert not any("User B" in app["job_title"] for app in list_a)

    # User B query
    list_b = client.get("/api/v1/applications/", headers=auth_headers_b).json()
    assert len(list_b) == 1
    assert list_b[0]["job_title"] == "User B App 1"

def test_analytics_metrics_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure funnel metrics for User B reflect only User B's applications."""
    # User A has 3 applications (1 offer, 1 rejected, 1 applied)
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "App 1", "status": "offer_received"},
        headers=auth_headers
    )
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "App 2", "status": "rejected"},
        headers=auth_headers
    )
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "App 3", "status": "applied"},
        headers=auth_headers
    )

    # User B has only 1 application (applied)
    client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "App B1", "status": "applied"},
        headers=auth_headers_b
    )

    # User B checks analytics
    analytics_b = client.get("/api/v1/analytics/", headers=auth_headers_b).json()
    assert analytics_b["total_applications"] == 1
    assert analytics_b["active_applications"] == 1
    assert analytics_b["offers_received"] == 0
    assert analytics_b["rejections"] == 0

    # User A checks analytics
    analytics_a = client.get("/api/v1/analytics/", headers=auth_headers).json()
    assert analytics_a["total_applications"] == 3
    assert analytics_a["offers_received"] == 1
    assert analytics_a["rejections"] == 1

def test_nested_notes_and_interviews_cross_user_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B cannot read, append, update, or delete User A's private notes and interview rounds."""
    # User A creates application
    app_resp = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "Systems Programmer", "status": "technical_interview"},
        headers=auth_headers
    )
    assert app_resp.status_code == status.HTTP_201_CREATED
    app_a_id = app_resp.json()["id"]

    # User A adds a private debrief note and interview stage
    note_resp = client.post(
        f"/api/v1/applications/{app_a_id}/notes",
        json={"content": "Private observation: Asked deep questions on ACID isolation levels and WAL logs."},
        headers=auth_headers
    )
    note_a_id = note_resp.json()["id"]

    stage_resp = client.post(
        f"/api/v1/applications/{app_a_id}/interviews",
        json={"stage_name": "Technical Architecture", "interviewer_notes": "Very positive on PostgreSQL internals."},
        headers=auth_headers
    )
    stage_a_id = stage_resp.json()["id"]

    # 1. User B attempts to list User A's notes
    notes_list_resp = client.get(f"/api/v1/applications/{app_a_id}/notes", headers=auth_headers_b)
    assert notes_list_resp.status_code == status.HTTP_404_NOT_FOUND

    # 2. User B attempts to append a note to User A's application
    notes_add_resp = client.post(
        f"/api/v1/applications/{app_a_id}/notes",
        json={"content": "Malicious injected note."},
        headers=auth_headers_b
    )
    assert notes_add_resp.status_code == status.HTTP_404_NOT_FOUND

    # 3. User B attempts to delete User A's note by note ID
    note_del_resp = client.delete(f"/api/v1/notes/{note_a_id}", headers=auth_headers_b)
    assert note_del_resp.status_code == status.HTTP_404_NOT_FOUND

    # 4. User B attempts to list User A's interview stages
    stages_list_resp = client.get(f"/api/v1/applications/{app_a_id}/interviews", headers=auth_headers_b)
    assert stages_list_resp.status_code == status.HTTP_404_NOT_FOUND

    # 5. User B attempts to schedule an interview stage on User A's application
    stage_add_resp = client.post(
        f"/api/v1/applications/{app_a_id}/interviews",
        json={"stage_name": "Unauthorized Round"},
        headers=auth_headers_b
    )
    assert stage_add_resp.status_code == status.HTTP_404_NOT_FOUND

    # 6. User B attempts to update User A's interview stage by ID
    stage_patch_resp = client.patch(
        f"/api/v1/interviews/{stage_a_id}",
        json={"outcome": "failed", "interviewer_notes": "Tampered review"},
        headers=auth_headers_b
    )
    assert stage_patch_resp.status_code == status.HTTP_404_NOT_FOUND

    # 7. User B attempts to delete User A's interview stage by ID
    stage_del_resp = client.delete(f"/api/v1/interviews/{stage_a_id}", headers=auth_headers_b)
    assert stage_del_resp.status_code == status.HTTP_404_NOT_FOUND

    # Verify User A's note and interview stage remain intact
    detail = client.get(f"/api/v1/applications/{app_a_id}", headers=auth_headers).json()
    assert len(detail["notes"]) == 1
    assert detail["notes"][0]["content"].startswith("Private observation")
    assert len(detail["interviews"]) == 1
    assert detail["interviews"][0]["stage_name"] == "Technical Architecture"
    assert detail["interviews"][0]["interviewer_notes"] == "Very positive on PostgreSQL internals."

def test_shared_company_directory_safety(client, auth_headers, auth_headers_b, test_company):
    """Ensure two distinct users can reference the shared company directory without data leakage."""
    # User A creates application under test_company
    app_a = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "User A Engineer", "status": "applied"},
        headers=auth_headers
    ).json()

    # User B creates application under the SAME test_company
    app_b = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "User B Engineer", "status": "screening"},
        headers=auth_headers_b
    ).json()

    # Company is shared
    assert app_a["company_id"] == test_company.id
    assert app_b["company_id"] == test_company.id

    # User A adds private note
    client.post(
        f"/api/v1/applications/{app_a['id']}/notes",
        json={"content": "User A private interview contact"},
        headers=auth_headers
    )

    # User B inspects their own application
    detail_b = client.get(f"/api/v1/applications/{app_b['id']}", headers=auth_headers_b).json()
    assert detail_b["company"]["name"] == test_company.name
    # User B sees 0 notes, User A's note is not visible
    assert len(detail_b["notes"]) == 0
