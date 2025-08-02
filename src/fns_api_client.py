from typing import Dict
import requests


class FnsApiClient:
    """
    Клиент для взаимодействия с API Федеральной налоговой службы (ФНС) России.
    https://api-fns.ru/api_help
    """

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def check(self, req) -> Dict:
        """
        Позволяет получить аналитическую информацию о компании
        https://api-fns.ru/api_help#section_check

        args:
            req (int): ОГРН или ИНН искомой компании
        """
        response = requests.get(
            f"{self.base_url}/check", params={"req": req, "key": self.api_key}
        )

        response.raise_for_status()
        data = response.json()
        return data
