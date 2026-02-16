import requests
from core.config import Config

class ApiClient:
    def __init__(self, base_url=Config.BASE_URL, token: str | None = None):
        self.base_url = base_url
        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def set_token(self, token: str) -> None:
        #Установить\обновить токен авторизации
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def clear_token(self):
        self.session.headers.pop("Authorization", None)

    def _make_url(self, path: str) -> str:
        return self.base_url.rstrip("/") + "/" + path.lstrip("/")


    def get(self, path:str,json:dict | None = None , params: dict | None = None  , **kwargs)-> requests.Responce:
        url = self._make_url(path)
        return self.session.get(url, json=json , params=params, timeout=Config.TIMEOUT, **kwargs)

    def post(self, path:str,json:dict | None = None , params: dict | None = None  , **kwargs)-> requests.Responce:
        url = self._make_url(path)
        return self.session.post(url, json=json , params=params, timeout=Config.TIMEOUT, **kwargs)

    def put(self, path:str,json:dict | None = None , params: dict | None = None  , **kwargs)-> requests.Responce:
        url = self._make_url(path)
        return self.session.put(url, json=json , params=params, timeout=Config.TIMEOUT, **kwargs)

    def delete(self, path:str,json:dict | None = None , params: dict | None = None  , **kwargs)-> requests.Responce:
        url = self._make_url(path)
        return self.session.delete(url, json=json , params=params, timeout=Config.TIMEOUT, **kwargs)