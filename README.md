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

pip install pytest requests pydantic faker allure-pytest

python -m pytest test_petstore_api.py -v
```

Allure output (optional):

```bash
python -m pytest test_petstore_api.py --alluredir=allure-results
```

## Structure

Layers (top to bottom):

```
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

| File | What it does |
|------|----------------|
| `api_client.py` | HTTP layer — get/post/put/delete via requests |
| `pet_store_api.py` | Pet endpoints — `petCreate`, `petFindbyId`, `petUpdate`, `petDelete` |
| `pet_store_models.py` | Pydantic models — `Pet`, `DeletedPet`, `PetNotFoundError` |
| `data_generator.py` | Test data, Faker |
| `conftest.py` | Session fixture (setup/teardown hooks) |
| `test_petstore_api.py` | Tests — parametrize, negative case, E2E |

Flow in tests: call `pet_store_api` → get a model back → assert. Older tests still call `api_client` directly; E2E uses the full stack.

E2E scenario: create → get → update → get → delete → get (404).

## Notes

- Public demo API — fixed ids (e.g. `333444`) can clash with data from other people. If E2E flakes, try a random id or re-run.
- `.venv`, `allure-results`, `__pycache__` are in `.gitignore`.

## Stack

pytest · requests · pydantic · faker · allure-pytest
