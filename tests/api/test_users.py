def test_get_users(api_context):
    response = api_context.get("users")
    assert response.status == 200
    assert response.json()["data"] is not None

def test_get_single_user(api_context):
    response = api_context.get("users/6")
    assert response.status == 200
    assert response.json()["data"]["id"] == 6
    assert response.json()["data"]["email"] == "tracey.ramos@reqres.in"

def test_register_user(api_context):
    response = api_context.post("register", data={"email": "tobias.funke@reqres.in", "password": "pistol"})
    assert response.status == 200
    assert response.json()["id"] == 9
    assert response.json()["token"] is not None

def test_login_user(api_context):
    response = api_context.post("login", data={"email": "tobias.funke@reqres.in", "password": "pistol"})
    assert response.status == 200
    assert response.json()["token"] is not None

def test_update_user(api_context):
    response = api_context.put("users/2", data={"name": "morpheus", "job": "zion resident"})
    assert response.status == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "zion resident"

def test_delete_user(api_context):
    response = api_context.delete("users/2")
    assert response.status == 204