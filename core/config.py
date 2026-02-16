import os
class Config:
    # Используем os.getenv для получения значений из переменных окружения
    BASE_URL = os.getenv("API_BASE_URL", "https://trustytalents.com").rstrip() # Убираем пробелы в конце

    # Получаем email и пароль из переменных окружения
    USER_EMAIL = os.getenv("USER_EMAIL")
    USER_PASSWORD = os.getenv("USER_PASSWORD")

    TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 100)) # Преобразуем в int, значение по умолчанию 100