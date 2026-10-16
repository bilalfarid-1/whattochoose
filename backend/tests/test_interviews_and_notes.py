from datetime import datetime, timezone
from fastapi import status

def test_interview_stage_lifecycle(client, auth_headers, test_company):
    # 1. Create Application
    app_resp = client.post(
        "/api/v1/applications/",
        json={
            "company_id": test_company.id,
            "job_title": "Backend Python Engineer",
            "status": "screening"
        },
        headers=auth_headers
    )
    app_id = app_resp.json()["id"]

    # 2. Add Interview Stage
    stage_payload = {
        "stage_name": "Technical Live Coding (DSA & Systems)",
        "scheduled_at": datetime.now(timezone.utc).isoformat(),
        "interviewer_notes": "Focused on SQL query optimization and Python asyncio concurrency.",
        "outcome": "pending"
    }
    stage_resp = client.post(
        f"/api/v1/applications/{app_id}/interviews",
        json=stage_payload,
        headers=auth_headers
    )
    assert stage_resp.status_code == status.HTTP_201_CREATED
    stage_data = stage_resp.json()
    assert stage_data["stage_name"] == stage_payload["stage_name"]
    assert stage_data["outcome"] == "pending"
    stage_id = stage_data["id"]

    # 3. Update Stage Outcome
    patch_resp = client.patch(
        f"/api/v1/interviews/{stage_id}",
        json={"outcome": "passed", "interviewer_notes": "Solved dynamic programming problem and designed normalized schema successfully."},
        headers=auth_headers
    )
    assert patch_resp.status_code == status.HTTP_200_OK
    assert patch_resp.json()["outcome"] == "passed"

    # 4. List Interviews
    list_resp = client.get(f"/api/v1/applications/{app_id}/interviews", headers=auth_headers)
    assert list_resp.status_code == status.HTTP_200_OK
    assert len(list_resp.json()) == 1

def test_application_notes_journal(client, auth_headers, test_company):
    # 1. Create Application
    app_resp = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "Data Platform Engineer"},
        headers=auth_headers
    )
    app_id = app_resp.json()["id"]

    # 2. Add Notes
    client.post(
        f"/api/v1/applications/{app_id}/notes",
        json={"content": "Sent cold message to Lead Engineer on LinkedIn with GitHub portfolio link."},
        headers=auth_headers
    )
    client.post(
        f"/api/v1/applications/{app_id}/notes",
        json={"content": "Engineering Manager replied; referral submitted internally."},
        headers=auth_headers
    )

    # 3. List Notes
    notes_resp = client.get(f"/api/v1/applications/{app_id}/notes", headers=auth_headers)
    assert notes_resp.status_code == status.HTTP_200_OK
    notes = notes_resp.json()
    assert len(notes) == 2
    assert "referral submitted" in notes[0]["content"]

def test_cross_user_interview_stage_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B cannot access, create, mutate, or delete User A's interview stages."""
    # 1. User A creates application and interview stage
    app_resp = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "Distributed Systems Engineer", "status": "screening"},
        headers=auth_headers
    )
    app_id = app_resp.json()["id"]

    stage_resp = client.post(
        f"/api/v1/applications/{app_id}/interviews",
        json={
            "stage_name": "System Architecture Deep Dive",
            "scheduled_at": datetime.now(timezone.utc).isoformat(),
            "outcome": "pending"
        },
        headers=auth_headers
    )
    assert stage_resp.status_code == status.HTTP_201_CREATED
    stage_id = stage_resp.json()["id"]

    # 2. User B attempts to list User A's interview stages (must return 404)
    list_b = client.get(f"/api/v1/applications/{app_id}/interviews", headers=auth_headers_b)
    assert list_b.status_code == status.HTTP_404_NOT_FOUND

    # 3. User B attempts to inject an interview stage into User A's application (must return 404)
    inject_b = client.post(
        f"/api/v1/applications/{app_id}/interviews",
        json={"stage_name": "Unauthorized Stage Injection", "outcome": "failed"},
        headers=auth_headers_b
    )
    assert inject_b.status_code == status.HTTP_404_NOT_FOUND

    # 4. User B attempts to modify User A's interview stage (must return 404)
    patch_b = client.patch(
        f"/api/v1/interviews/{stage_id}",
        json={"outcome": "failed", "interviewer_notes": "Tampered note"},
        headers=auth_headers_b
    )
    assert patch_b.status_code == status.HTTP_404_NOT_FOUND

    # 5. User B attempts to delete User A's interview stage (must return 404)
    del_b = client.delete(f"/api/v1/interviews/{stage_id}", headers=auth_headers_b)
    assert del_b.status_code == status.HTTP_404_NOT_FOUND

    # 6. Verify User A's interview stage remains untouched and preserved
    verify_a = client.get(f"/api/v1/applications/{app_id}/interviews", headers=auth_headers)
    assert verify_a.status_code == status.HTTP_200_OK
    assert len(verify_a.json()) == 1
    assert verify_a.json()[0]["stage_name"] == "System Architecture Deep Dive"

def test_cross_user_application_notes_isolation(client, auth_headers, auth_headers_b, test_company):
    """Ensure User B cannot list, add, or delete User A's application journal notes."""
    # 1. User A creates application and a private note
    app_resp = client.post(
        "/api/v1/applications/",
        json={"company_id": test_company.id, "job_title": "Security Engineering Lead"},
        headers=auth_headers
    )
    app_id = app_resp.json()["id"]

    note_resp = client.post(
        f"/api/v1/applications/{app_id}/notes",
        json={"content": "Private negotiation notes: Target salary $120k + equity."},
        headers=auth_headers
    )
    assert note_resp.status_code == status.HTTP_201_CREATED
    note_id = note_resp.json()["id"]

    # 2. User B attempts to read User A's application notes (must return 404)
    read_b = client.get(f"/api/v1/applications/{app_id}/notes", headers=auth_headers_b)
    assert read_b.status_code == status.HTTP_404_NOT_FOUND

    # 3. User B attempts to post a note to User A's application (must return 404)
    post_b = client.post(
        f"/api/v1/applications/{app_id}/notes",
        json={"content": "Unauthorized eavesdropping entry"},
        headers=auth_headers_b
    )
    assert post_b.status_code == status.HTTP_404_NOT_FOUND

    # 4. User B attempts to delete User A's note (must return 404)
    del_b = client.delete(f"/api/v1/notes/{note_id}", headers=auth_headers_b)
    assert del_b.status_code == status.HTTP_404_NOT_FOUND

    # 5. Verify User A's note remains securely accessible to User A
    verify_a = client.get(f"/api/v1/applications/{app_id}/notes", headers=auth_headers)
    assert verify_a.status_code == status.HTTP_200_OK
    assert len(verify_a.json()) == 1
    assert "Private negotiation notes" in verify_a.json()[0]["content"]
