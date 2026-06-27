# pytest

API autotests for [Petstore Swagger](https://petstore.swagger.io/v2/pet) — CRUD on `/pet`. Plus a small Playwright UI script in `ui_testing/`.

Pet project while learning pytest, requests, Allure and a bit of Docker. Layout is intentional: tests shouldn't know about URLs and raw JSON if you can avoid it.

## Run

```bash
git clone https://github.com/GeorgeKalyaev/pytest.git
cd pytest

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

pip install -r requirements.txt

python -m pytest test_petstore_api.py -v
```

Allure output (optional):

```bash
python -m pytest test_petstore_api.py --alluredir=allure-results
```

## Docker

```bash
docker build -t pytest-petstore .
docker run --rm pytest-petstore
```

Runs `pytest -v` inside the container. API tests only — UI stuff needs Playwright browsers locally.

## Structure

```
conftest.py              ← session fixture (autouse — setup/teardown for all tests)

test_petstore_api.py     ← API scenarios, asserts
        ↓
pet_store_api.py         ← petCreate, petFindbyId, petUpdate, petDelete
        ↓
api_client.py            ← GET / POST / PUT / DELETE (requests)
        ↓
pet_store_models.py      ← Pet, DeletedPet, PetNotFoundError (Pydantic)
        ↓
data_generator.py        ← test data (Faker)

ui_testing/              ← Playwright UI demo (TodoMVC)
requirements.txt
Dockerfile
```

E2E: create → get → update → get → delete → get (404). Mock test for `petFindbyId` uses `responses` — no real HTTP.

## Notes

- Public demo API — fixed ids (e.g. `333444`) can clash with data from other people. If E2E flakes, try a random id or re-run.
- `.venv`, `allure-results`, `__pycache__` are in `.gitignore`.

## Stack

pytest · requests · pydantic · faker · allure-pytest · responses · Playwright (ui_testing)