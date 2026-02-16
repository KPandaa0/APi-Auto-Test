def test_get_user_by_id(api_client):
    response =  api_client.get(f"api/user/profile")

    assert response.status_code == 200
    data = response.json()

    assert data["data"]["name"]
    assert data["data"]["email"]

