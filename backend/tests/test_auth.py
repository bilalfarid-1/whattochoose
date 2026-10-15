import pytest
from fastapi import status

def test_register_user_success(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "newgraduate@fast.nu.edu.pk",
            "password": "StrongPassword2026!",
            "full_name": "Muhammad Bilal"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == "newgraduate@fast.nu.edu.pk"
    assert data["full_name"] == "Muhammad Bilal"
    assert "id" in data
    assert "hashed_password" not in data

def test_register_duplicate_email_fails(client, test_user):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": test_user.email,
            "password": "AnotherPassword123!",
            "full_name": "Duplicate Candidate"
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "already exists" in response.json()["detail"]

def test_login_success(client, test_user):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "engineer@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_password_fails(client, test_user):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "engineer@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "Incorrect email or password" in response.json()["detail"]

def test_get_current_user_profile(client, auth_headers):
    response = client.get("/api/v1/auth/me", headers=auth_headers)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["email"] == "engineer@example.com"
    assert data["full_name"] == "Bilal Farid"

def test_unauthenticated_request_fails(client):
    response = client.get("/api/v1/auth/me")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
