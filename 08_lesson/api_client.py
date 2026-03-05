import requests
from typing import Dict, Any


class YougileProjectAPI:
    """Клиент для работы с проектами в Yougile API"""

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def create_project(self, data: Dict[str, Any]) -> requests.Response:
        """Создание проекта (POST /api-v2/projects)"""
        url = f"{self.base_url}/api-v2/projects"
        return requests.post(url, json=data, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        """Получение проекта по ID (GET /api-v2/projects/{id})"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str,
                       data: Dict[str, Any]) -> requests.Response:
        """Обновление проекта (PUT /api-v2/projects/{id})"""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.put(url, json=data, headers=self.headers)
