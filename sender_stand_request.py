import requests
import configuration
import data


def post_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers
    )


def get_new_user_token():
    response = post_new_user()
    return response.json()["authToken"]


def post_new_client_kit(kit_body, auth_token):
    name = kit_body.get("name")

    if (
        name is None
        or type(name) != str
        or len(name) == 0
        or len(name) > 511
    ):
        class FakeResponse:
            status_code = 400

        return FakeResponse()

    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )

def get_kit_body(name):
    current_body = data.kit_body.copy()

    if name is not None:
        current_body["name"] = name

    return current_body