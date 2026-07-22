import pytest
from fastapi import status

# Tells pytest-asyncio that all tests in this file are async
pytestmark = pytest.mark.asyncio

VALID_USER_PAYLOAD = {
    "id": 2,
    "email": "testuser@example.com",
    "password": "securepassword123",
    "name": "Alex Mercer",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "balance": "5500.50",
    "isActive": True
}

async def test_create_user_success(client):
    """Verifies user generation works, removes plaintext password, and persists schema details."""
    response = await client.post("/user/", json=VALID_USER_PAYLOAD)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    assert data["email"] == VALID_USER_PAYLOAD["email"]
    assert data["name"] == VALID_USER_PAYLOAD["name"]
    assert "password" not in data  
    assert float(data["balance"]) == 5500.50

async def test_update_user_success(client):
    """Verifies that an existing user's details can be successfully patched."""
    # 1. Create a baseline user in the test DB
    response = await client.post("/user/", json=VALID_USER_PAYLOAD)
    assert response.status_code == status.HTTP_200_OK
    
    # Get the actual ID that PostgreSQL assigned to the user
    created_user = response.json()
    user_id = created_user["id"] 
    
    # 2. Define the patch updates
    PATCH_PAYLOAD = {
        "name": "Alex Mercer Updated",
        "city": "Los Angeles",
        "balance": 1000.00 
    }
    
    # 3. Perform the PATCH request with the database-provided ID
    update_response = await client.patch(f"/user/{user_id}", json=PATCH_PAYLOAD)

    # 4. Assertions on the newly returned data framework
    assert update_response.status_code == status.HTTP_200_OK
    updated_data = update_response.json()
            
    assert updated_data["name"] == PATCH_PAYLOAD["name"]
    assert updated_data["city"] == PATCH_PAYLOAD["city"]
    assert float(updated_data["balance"]) == 1000.00

async def test_get_all_users_success(client):
    """Seeds a user into the database and verifies the bulk retrieval list route works."""
    # 1. Seed a user so the collection is not empty
    setup_response = await client.post("/user/", json=VALID_USER_PAYLOAD)
    assert setup_response.status_code == status.HTTP_200_OK

    # 2. Query the HTTP GET endpoint (Changed from get_or_none to .get)
    response = await client.get("/user/")

    # 3. Assertions
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    
    # Verify the route returns an array/list structure containing our seeded entity
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["email"] == VALID_USER_PAYLOAD["email"]
