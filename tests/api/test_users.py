def test_get_users(api_context):
    response = api_context.get("users")
    assert response.status == 200
    assert response.json()["data"] is not None

def test_get_single_user(api_context, grab_reqres_json_file):
    response = api_context.get(f"users/{grab_reqres_json_file['users']['6']['id']}")
    assert response.status == 200
    assert response.json()["data"]["id"] == grab_reqres_json_file["users"]["6"]["id"]
    assert response.json()["data"]["email"] == grab_reqres_json_file["users"]["6"]["email"]

def test_register_user(api_context, grab_reqres_json_file):
    response = api_context.post("register", data={"email": grab_reqres_json_file["users"]["9"]["email"], "password": grab_reqres_json_file["users"]["9"]["password"]})
    assert response.status == 200
    assert response.json()["id"] == grab_reqres_json_file["users"]["9"]["id"]
    assert response.json()["token"] is not None

def test_login_user(api_context, grab_reqres_json_file):
    response = api_context.post("login", data={"email": grab_reqres_json_file["users"]["9"]["email"], "password": grab_reqres_json_file["users"]["9"]["password"]})
    assert response.status == 200
    assert response.json()["token"] is not None

def test_update_user(api_context, grab_reqres_json_file):
    response = api_context.put("users/2", data={"name": "morpheus", "job": "zion resident"})
    assert response.status == 200
    assert response.json()["name"] == "morpheus"
    assert response.json()["job"] == "zion resident"

def test_delete_user(api_context, grab_reqres_json_file):
    response = api_context.delete(f"users/{grab_reqres_json_file['users']['2']['id']}")
    assert response.status == 204