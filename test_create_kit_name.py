import sender_stand_request


def positive_assert(name):
    kit_body = sender_stand_request.get_kit_body(name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == name


def negative_assert_code_400(name):
    kit_body = sender_stand_request.get_kit_body(name)
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400


def test_create_kit_1_char():
    positive_assert("a")


def test_create_kit_511_char():
    positive_assert("a" * 511)


def test_create_kit_empty():
    negative_assert_code_400("")


def test_create_kit_512_char():
    negative_assert_code_400("a" * 512)

def test_create_kit_512_char():
    negative_assert_code_400("a" * 512)

def test_create_kit_special_char():
    positive_assert("№%@,")


def test_create_kit_spaces():
    positive_assert(" A Aaa ")


def test_create_kit_numbers():
    positive_assert("123")


def test_create_kit_no_name():
    negative_assert_code_400("")


def test_create_kit_number_type():
    negative_assert_code_400(123)