# from http.client import responses # Эта строка не используется, можно удалить
from core.api_client import ApiClient
from core.config import Config

def get_auth_token() -> str:
    # Проверяем, что переменные окружения заданы
    email = Config.USER_EMAIL
    password = Config.USER_PASSWORD
    if not email or not password:
        raise ValueError("USER_EMAIL and USER_PASSWORD must be set as environment variables.")

    client = ApiClient() # Теперь использует BASE_URL из config
    payload = {
        "email": email, # Используем переменные из config (через env)
        "password": password
    }
    response = client.post("api/auth/login", json=payload)

    # Лучше использовать более общую проверку или логировать статус
    if response.status_code != 200:
        print(f"Auth failed with status {response.status_code}: {response.text}")
        response.raise_for_status() # Это вызовет исключение с деталями

    data = response.json()
    token = data["data"]["token"]
    if not token:
        raise ValueError("Token not found in response")
    return token