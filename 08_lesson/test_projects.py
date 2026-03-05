from api_client import YougileProjectAPI
import uuid


class TestProjectAPIMethods:
    """Тесты для методов работы с проектами Yougile API"""

    def test_create_project_positive(self, api_client: YougileProjectAPI,
                                     project_data: dict):
        response = api_client.create_project(project_data)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        response_data = response.json()
        assert 'id' in response_data
        project_id = response_data['id']
        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()['title'] == project_data['title']

    def test_create_project_negative_missing_title(self, api_client:
                                                   YougileProjectAPI):
        """Негативный тест: попытка создания
        проекта без обязательного поля title"""
        invalid_data = {"description": "Missing title field"}
        response = api_client.create_project(invalid_data)
        assert response.status_code in [
            400, 422], f"Expected 400 or 422, got {response.status_code}"

    def test_get_project_positive(self, api_client: YougileProjectAPI,
                                  project_data: dict):
        """Позитивный тест: получение существующего проекта"""
        # Создаём проект для получения
        create_response = api_client.create_project(project_data)
        project_id = create_response.json()['id']

        # Получаем проект по ID
        response = api_client.get_project(project_id)
        assert response.status_code == 200

        response_data = response.json()
        assert response_data['id'] == project_id
        assert response_data['title'] == project_data['title']

    def test_get_project_negative_not_found(self, api_client:
                                            YougileProjectAPI):
        """Негативный тест: попытка получения несуществующего проекта"""
        non_existent_id = str(uuid.uuid4())
        response = api_client.get_project(non_existent_id)
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_update_project_positive(self, api_client: YougileProjectAPI,
                                     project_data: dict,
                                     updated_project_data: dict):
        """Позитивный тест: обновление существующего проекта"""
        # Создаём проект для обновления
        create_response = api_client.create_project(project_data)
        assert create_response.status_code == 201, f"Create failed: {create_response.text}"
        project_id = create_response.json()['id']

        # Обновляем проект
        response = api_client.update_project(project_id, updated_project_data)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Body: {response.text}"

        get_response = api_client.get_project(project_id)
        assert get_response.status_code == 200
        assert get_response.json()['title'] == updated_project_data['title']

    def test_update_project_negative_invalid_id(self, api_client:
                                                YougileProjectAPI,
                                                updated_project_data: dict):
        """Негативный тест: попытка обновления с некорректным ID"""
        invalid_id = "invalid-id-format"
        response = api_client.update_project(invalid_id, updated_project_data)
        assert response.status_code in [
            400, 404], f"Expected 400 or 404, got {response.status_code}"
