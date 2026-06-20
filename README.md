# pytest

API autotests for [Petstore Swagger](https://petstore.swagger.io/v2/pet) — CRUD on `/pet`.

Pet project while learning pytest, requests and Allure. Nothing fancy, but the layout is intentional: tests shouldn't know about URLs and raw JSON if you can avoid it.

## Run

```bash
git clone https://github.com/GeorgeKalyaev/pytest.git
cd pytest

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

pip install pytest requests pydantic faker allure-pytest responses

python -m pytest test_petstore_api.py -v
```

Allure output (optional):

```bash
python -m pytest test_petstore_api.py --alluredir=allure-results
```

## Structure

```
conftest.py              ← session fixture (autouse — setup/teardown for all tests)

test_petstore_api.py     ← scenarios, asserts
        ↓
pet_store_api.py         ← petCreate, petFindbyId, petUpdate, petDelete
        ↓
api_client.py            ← GET / POST / PUT / DELETE (requests)
        ↓
pet_store_models.py      ← Pet, DeletedPet, PetNotFoundError (Pydantic)
        ↓
data_generator.py        ← test data (Faker)
```

E2E goes through the full stack: create → get → update → get → delete → get (404). Some older tests still hit `api_client` directly. Mock test for `petFindbyId` uses `responses` — no real HTTP call.

## Notes

- Public demo API — fixed ids (e.g. `333444`) can clash with data from other people. If E2E flakes, try a random id or re-run.
- `.venv`, `allure-results`, `__pycache__` are in `.gitignore`.

## Stack

pytest · requests · pydantic · faker · allure-pytest · responses
