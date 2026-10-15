from datetime import date
from fastapi import status

def test_create_and_list_companies(client, auth_headers):
    # Create company
    response = client.post(
        "/api/v1/companies/",
        json={
            "name": "Netsol Technologies",
            "website": "https://netsoltech.com",
            "location": "Lahore, Pakistan",
            "notes": "Global asset finance software provider."
        },
        headers=auth_headers
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "Netsol Technologies"
    company_id = data["id"]

    # List companies
    list_resp = client.get("/api/v1/companies/", headers=auth_headers)
    assert list_resp.status_code == status.HTTP_200_OK
    companies = list_resp.json()
    assert any(c["id"] == company_id for c in companies)

def test_create_and_read_job_application(client, auth_headers, test_company):
    # Create application
    payload = {
        "company_id": test_company.id,
        "job_title": "Associate Backend Engineer (Python / FastAPI)",
        "job_url": "https://careers.example.com/jobs/101",
        "salary_range": "PKR 120k - 160k",
        "work_location": "hybrid",
        "status": "applied",
        "applied_date": str(date.today()),
        "deadline": "2026-11-15"
    }
    response = client.post("/api/v1/applications/", json=payload, headers=auth_headers)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["job_title"] == payload["job_title"]
    assert data["status"] == "applied"
    app_id = data["id"]

    # Retrieve detail
    detail_resp = client.get(f"/api/v1/applications/{app_id}", headers=auth_headers)
    assert detail_resp.status_code == status.HTTP_200_OK
    detail_data = detail_resp.json()
    assert detail_data["id"] == app_id
    assert detail_data["company"]["name"] == "Systems Limited"
    assert "interviews" in detail_data
    assert "notes" in detail_data

def test_application_status_update_and_filter(client, auth_headers, test_company):
    # Create application
    app_payload = {
        "company_id": test_company.id,
        "job_title": "Junior Python Systems Developer",
        "work_location": "remote",
        "status": "applied"
    }
    create_resp = client.post("/api/v1/applications/", json=app_payload, headers=auth_headers)
    app_id = create_resp.json()["id"]

    # Update status to screening
    patch_resp = client.patch(
        f"/api/v1/applications/{app_id}",
        json={"status": "screening"},
        headers=auth_headers
    )
    assert patch_resp.status_code == status.HTTP_200_OK
    assert patch_resp.json()["status"] == "screening"

    # Filter by status=screening
    filter_resp = client.get("/api/v1/applications/?status=screening", headers=auth_headers)
    assert filter_resp.status_code == status.HTTP_200_OK
    results = filter_resp.json()
    assert len(results) >= 1
    assert all(r["status"] == "screening" for r in results)

def test_delete_application(client, auth_headers, test_company):
    # Create application
    app_payload = {
        "company_id": test_company.id,
        "job_title": "Python QA Automation Intern",
        "status": "applied"
    }
    create_resp = client.post("/api/v1/applications/", json=app_payload, headers=auth_headers)
    app_id = create_resp.json()["id"]

    # Delete
    del_resp = client.delete(f"/api/v1/applications/{app_id}", headers=auth_headers)
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT

    # Verify not found
    get_resp = client.get(f"/api/v1/applications/{app_id}", headers=auth_headers)
    assert get_resp.status_code == status.HTTP_404_NOT_FOUND
