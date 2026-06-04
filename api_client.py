import allure
import requests

def request(method, url, json=None):
    print(f"{method} request to {url}")
    result = requests.request(method, url, json=json)
    print(f"Response status code: {result.status_code}")
    print(f"Response body: {result.json()}")
    return result

@allure.step("Send get request")
def get(url):

    # print(f"GET request to {url}")
    return request("GET", url)

@allure.step("Send post request")
def post(url, json):
    # print(f"POST request to {url} with JSON: {json}")
    return request("POST", url, json=json)

@allure.step("Send put request")
def put(url, json):
    # print(f"PUT request to {url} with JSON: {json}")
    return request("PUT", url, json=json)

@allure.step("Send delete request")
def delete(url):
    # print(f"DELETE request to {url}")
    return request("DELETE", url)