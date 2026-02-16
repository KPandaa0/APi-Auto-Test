import pytest
from core.auth import get_auth_token
from core.api_client import ApiClient

@pytest.fixture(scope="session")
def auth_token() -> str:
    return get_auth_token()

@pytest.fixture
def api_client(auth_token: str) -> ApiClient:
    client = ApiClient(token=auth_token)  # Передаем токен через конструктор
    return client


