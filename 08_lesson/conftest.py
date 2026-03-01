import pytest
from api_client import YougileProjectAPI
from typing import Dict


@pytest.fixture
def base_url() -> str:
    """Базовый URL API. Заменить на реальный перед запуском."""
    return "https://ru.yougile.com"


@pytest.fixture
def auth_token() -> str:
    """Токен авторизации. Заменить на реальный перед запуском (см. README)"""
    return "YOUR_AUTH_TOKEN_HERE"


@pytest.fixture
def api_client(base_url: str, auth_token: str) -> YougileProjectAPI:
    """Фикстура для создания API-клиента"""
    return YougileProjectAPI(base_url, auth_token)


@pytest.fixture
def project_data() -> Dict[str, str]:
    """Данные для создания проекта"""
    return {
        "title": "Test Project",
        "description": "Test description"
    }


@pytest.fixture
def updated_project_data() -> Dict[str, str]:
    """Данные для обновления проекта"""
    return {
        "title": "Updated Project Title",
        "description": "Updated description"
    }
