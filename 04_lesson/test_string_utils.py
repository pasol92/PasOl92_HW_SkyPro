import pytest
from string_utils import StringUtils


class TestStringUtils:
    def setup_method(self):
        """Инициализация объекта перед каждым тестом"""
        self.utils = StringUtils()

    # === TESTS FOR capitalize ===

    def test_capitalize_positive_non_empty(self):
        """Позитивный: не пустая строка"""
        assert self.utils.capitalize("тест") == "Тест"
        assert self.utils.capitalize("123") == "123"
        assert self.utils.capitalize("04 апреля 2023") == "04 апреля 2023"

    def test_capitalize_empty_string(self):
        """Негативный: пустая строка"""
        assert self.utils.capitalize("") == ""

    def test_capitalize_whitespace_only(self):
        """Негативный: строка с пробелом"""
        assert self.utils.capitalize(" ") == " "

    def test_capitalize_none(self):
        """Негативный: None"""
        with pytest.raises(AttributeError):
            self.utils.capitalize(None)

    def test_capitalize_non_string(self):
        """Негативный: не строка (число, список)"""
        with pytest.raises(AttributeError):
            self.utils.capitalize(123)
        with pytest.raises(AttributeError):
            self.utils.capitalize([])

    # === TESTS FOR trim ===

    def test_trim_positive_non_empty(self):
        """Позитивный: не пустая строка с пробелами в начале"""
        assert self.utils.trim("  тест") == "тест"
        assert self.utils.trim("  123") == "123"
        assert self.utils.trim("  04 апреля 2023") == "04 апреля 2023"

    def test_trim_empty_string(self):
        """Негативный: пустая строка"""
        assert self.utils.trim("") == ""

    def test_trim_whitespace_only(self):
        """Негативный: строка с пробелом (только пробелы)"""
        assert self.utils.trim("   ") == ""

    def test_trim_no_leading_spaces(self):
        """Позитивный: строка без ведущих пробелов"""
        assert self.utils.trim("тест") == "тест"

    def test_trim_none(self):
        """Негативный: None"""
        with pytest.raises(AttributeError):
            self.utils.trim(None)

    def test_trim_non_string(self):
        """Негативный: не строка (число, список)"""
        with pytest.raises(AttributeError):
            self.utils.trim(123)
        with pytest.raises(AttributeError):
            self.utils.trim([])

    # === TESTS FOR contains ===

    def test_contains_positive_found(self):
        """Позитивный: символ есть в строке"""
        assert self.utils.contains("тест", "т") is True
        assert self.utils.contains("123", "2") is True
        assert self.utils.contains("04 апреля 2023", "а") is True

    def test_contains_negative_not_found(self):
        """Негативный: символа нет"""
        assert self.utils.contains("тест", "х") is False
        assert self.utils.contains("123", "а") is False

    def test_contains_empty_string_input(self):
        """Негативный: входная строка пустая"""
        assert self.utils.contains("", "а") is False

    def test_contains_empty_symbol(self):
        """Негативный: искомый символ — пустая строка"""
        # По логике Python: '' в любой строке даёт True
        assert self.utils.contains("тест", "") is True

    def test_contains_none_input(self):
        """Негативный: None вместо строки"""
        with pytest.raises(TypeError):
            self.utils.contains(None, "а")

    def test_contains_none_symbol(self):
        """Негативный: None вместо символа"""
        with pytest.raises(TypeError):
            self.utils.contains("тест", None)

    def test_contains_non_string_input(self):
        """Негативный: не строка на входе"""
        with pytest.raises(TypeError):
            self.utils.contains(123, "а")
        with pytest.raises(TypeError):
            self.utils.contains([], "а")

    def test_contains_non_string_symbol(self):
        """Негативный: не строка как символ поиска"""
        with pytest.raises(TypeError):
            self.utils.contains("тест", 123)
        with pytest.raises(TypeError):
            self.utils.contains("тест", [])

    # === TESTS FOR delete_symbol ===

    def test_delete_symbol_positive_simple(self):
        assert self.utils.delete_symbol("тест", "т") == "ес"
        assert self.utils.delete_symbol("123", "2") == "13"
        assert self.utils.delete_symbol("04 апреля 2023", "а") == "04 преля 2023"

    def test_delete_symbol_substring(self):
        """Позитивный: удаление подстроки"""
        assert self.utils.delete_symbol("тест", "те") == "ст"
        assert self.utils.delete_symbol("04 апреля 2023", "апр") == "04 еля 2023"

    def test_delete_symbol_not_found(self):
        """Позитивный: символа/подстроки нет"""
        assert self.utils.delete_symbol("тест", "х") == "тест"
        assert self.utils.delete_symbol("123", "а") == "123"

    def test_delete_symbol_empty_string(self):
        """Негативный: входная строка пустая"""
        assert self.utils.delete_symbol("", "а") == ""

    def test_delete_symbol_empty_symbol(self):
        """Негативный: удаляемый символ — пустая строка"""
        # replace("", "") не меняет строку
        assert self.utils.delete_symbol("тест", "") == "тест"

    def test_delete_symbol_none_input(self):
        """Негативный: None вместо строки"""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(None, "а")

    def test_delete_symbol_none_symbol(self):
        """Негативный: None вместо символа"""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol("тест", None)

    def test_delete_symbol_non_string_input(self):
        """Негативный: не строка на входе"""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(123, "а")
        with pytest.raises(AttributeError):
            self.utils.delete_symbol([], "а")

    def test_delete_symbol_non_string_symbol(self):
        """Негативный: не строка как символ удаления"""
        with pytest.raises(AttributeError):
            self.utils.delete_symbol("тест", 123)
        with pytest.raises(AttributeError):
            self.utils.delete_symbol("тест", [])
