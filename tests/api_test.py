import requests
import json
import random
import string

base_url = "https://gorest.co.in"


def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")