from api_client import get, post, put, delete
from pet_store_models import Pet, DeletedPet, PetNotFoundError
PETURL = "https://petstore.swagger.io/v2/pet"
def petFindbyId(pet_id):
    response = get(f"{PETURL}/{pet_id}")
    if response.status_code == 200:
        return Pet(**response.json())
    else:
        return PetNotFoundError(**response.json())