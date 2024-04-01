from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """
    абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, text):
        pass

    @abstractmethod
    def filter_vacancies(self, text):
        pass

class HeadHunter(AbstractAPI):
    """
    Подключается к API и получает вакансии по ключевому слову
    """

    def get_vacancies(self, text):
        """
        Получает вакансии по ключевому слову из API сервиса поиска вакансий
        """
        params = {"text": text, 'per_page': 20, "only_with_salary": "true"}
        vacancies = requests.get("https://api.hh.ru/vacancies", params=params).json()
        return vacancies["items"]

    def filter_vacancies(self, text):
        """
        Выбирает необходтмые значения из полученного списка вакансий и добавляет в словарь vacancies_filter
        """
        vacancies = self.get_vacancies(text)
        vacancies_filter = []
        for vacancy in vacancies:
            if vacancy["salary"]["currency"] != "RUR":
                continue
            if vacancy['snippet']['requirement'] == None:
                vacancy['snippet']['requirement'] = "-"
            if "<highlighttext>" in vacancy['snippet']['requirement']:
                vacancy['snippet']['requirement'] = "".join(vacancy['snippet']['requirement'].split("<highlighttext>"))
            if "</highlighttext>" in vacancy['snippet']['requirement']:
                vacancy['snippet']['requirement'] = "".join(vacancy['snippet']['requirement'].split("</highlighttext>"))
            if vacancy["salary"]["from"] == None:
                vacancy["salary"]["from"] = 0
            if vacancy["salary"]["to"] == None:
                vacancy["salary"]["to"] = 0
            if vacancy['snippet']['responsibility'] == None:
                vacancy['snippet']['responsibility'] = "-"
            vacancies_filter.append({
                "name": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": vacancy["salary"]["from"],
                "salary_to": vacancy["salary"]["to"],
                "currency": vacancy["salary"]["currency"],
                "description": vacancy['snippet']['requirement'],
                'responsibility': vacancy['snippet']['responsibility']
            })
        return vacancies_filter

