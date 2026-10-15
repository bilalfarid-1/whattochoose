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
