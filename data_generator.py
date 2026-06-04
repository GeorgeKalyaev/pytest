
import random
from faker import Faker

fake = Faker()
post_body = {
  "id": 777888,
  "category": {
    "id": 0,
    "name": "hello"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

def generate_pet_data(**kwargs):
    pet_data = {"id": random.randint(1, 1000000),  "category": {"id": random.randint(1, 1000), "name": fake.first_name()}, "name": fake.first_name(), "photoUrls": [fake.url()], "tags": [{"id": random.randint(1, 1000), "name": fake.word()}], "status": random.choice(["available", "pending", "sold"])}
    pet_data.update(kwargs)
    return pet_data

print(generate_pet_data(id=111444,name="statik"))