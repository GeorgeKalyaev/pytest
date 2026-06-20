import pytest
@pytest.fixture(scope="session", autouse=True)
def prepare_test():
    print("Preparing test environment...")
    yield
    print("Cleaning up test environment...")

