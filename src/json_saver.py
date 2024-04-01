import json
from src.vacancy import Vacancy

class JSONSaver:
    def __init__(self, filename):
        self.filename = filename

    def write_vacancies(self, vacancies):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        with open(self.filename, encoding="utf-8") as file:
            vacancies = json.load(file)
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append(Vacancy(vacancy["name"],
                                          vacancy["url"],
                                          vacancy["salary_from"],
                                          vacancy["salary_to"],
                                          vacancy["currency"],
                                          vacancy["description"],
                                          vacancy["responsibility"]))
        return list_vacancies

