import allure
import pytest
from api_client import get,post, put, delete
from data_generator import generate_pet_data
from pet_store_models import Pet, DeletedPet, PetNotFoundError
from pet_store_api import petFindbyId

BASE_URL = "https://petstore.swagger.io/v2/pet"

post_body = generate_pet_data()

# change_body = {
#   "id": 777888,
#   "category": {
#     "id": 0,
#     "name": "qwertyqwerty"
#   },
#   "name": "doggie",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }



@pytest.mark.parametrize("pet", [generate_pet_data(id=777888), generate_pet_data(photoUrls=["string1", "string2"])], ids=["basic pet", "pet with multiple photoUrls"])
def test_post(pet):
    # post_body=generate_pet_data(id=pet_id)
    # pet["id"] = pet_id
    response = post(BASE_URL, json=pet)
    assert response.status_code == 200
    assert response.json() == pet
    # print_response(response)

@pytest.mark.skip(reason="This test is for demonstration purposes and will be skipped.")
@pytest.mark.parametrize("pet_id", [777888,444555,666111])
def test_get(pet_id):
    post_body["id"] = pet_id
    response = get(f"{BASE_URL}/{pet_id}")
    assert response.status_code == 200
    assert response.json() == post_body

@allure.title("Test PUT method with different pet names and category names")
@pytest.mark.parametrize("pet_name, pet_category_name", [("qwertyqwerty", "cat"),("emty", "mouse")], ids=["real", "unreal"])
def test_put(pet_name, pet_category_name):
    post_body["name"] = pet_name
    post_body["category"]["name"] = pet_category_name
    response = put(BASE_URL, json=post_body)
    with allure.step("Check response status code"):
        assert response.status_code == 200
    with allure.step("Check response body"):
        assert response.json() == post_body

# // в разные типы передавать разные типы анных кривые данные в поля передать + ids + поля меняющиеся 
@allure.title("Test post incorrect_type")
def test_incorrect_type():
    post_body["id"] = "string_ID_check"
    response = post(BASE_URL, json=post_body)
    with pytest.raises(AssertionError):
        assert response.status_code == 200
    # assert response.json() == post_body
    # print_response(response)

@allure.title("Test end-to-end scenario")
def test_end_to_end():
    pet_id = 333444
    post_body["id"] = pet_id
    post_body.pop("name") # удаляем обязательное поле, чтобы проверить, что оно действительно обязательное
    response = post(BASE_URL, json=post_body)
    with allure.step("Check pet creation response status code"):
        assert response.status_code == 200
    with allure.step("Check pet creation response body"):
        assert Pet(**response.json()) == Pet(**post_body)

    response = petFindbyId(pet_id)
    # with allure.step("Check pet retrieval response status code"):
    #     assert response.status_code == 200
    with allure.step("Check pet retrieval response body"):
        assert response == Pet(**post_body)

    pet_name = "bear"
    post_body["name"] = pet_name

    response = put(BASE_URL, json=post_body)
    with allure.step("Check put response status code"):
        assert response.status_code == 200
    with allure.step("Check put response body"):
        assert response.json() == post_body

    response = get(f"{BASE_URL}/{pet_id}")
    with allure.step("Check get retrieval response status code"):
        assert response.status_code == 200
    with allure.step("Check get retrieval response body = bear"):
        assert Pet(**response.json()) == Pet(**post_body)

    response = delete(f"{BASE_URL}/{pet_id}")
    with allure.step("Check delete response status code"):
        assert response.status_code == 200
    with allure.step("Check delete response body = bear - deleted"):
        assert DeletedPet(**response.json()).message == str(pet_id) # все остальное проверится DeletedPet само

    response = get(f"{BASE_URL}/{pet_id}")
    with allure.step("Check get retrieval response status code"):
        assert response.status_code == 404
    with allure.step("Check get retrieval response body = bear - not found"):
        assert PetNotFoundError(**response.json())
        
    

# response = requests.put(BASE_URL, json=change_body)
# assert response.status_code == 200
# assert response.json() == change_body
# print_response(response)

# response = requests.delete(f"{BASE_URL}/777888")
# # assert response.status_code == 200
# print(response.status_code)


# print_response(response.status_code)







# assert response.status_code == 200
# assert response.json() == post_body


