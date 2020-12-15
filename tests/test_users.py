import requests
from assertpy import assert_that


def test_users():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    content = response.json()
    assert_that(response.status_code).is_equal_to(200)
    assert_that(content['total']).is_equal_to(12)

