class Vacancy:
    def __init__(self, name, url, salary_from, salary_to, currency, desc, resp):
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.desc = desc
        self.resp = resp

    def __str__(self):
        return f"""Название вакансии: {self.name}
Ссылка: {self.url}
Зарплата от {self.salary_from} до {self.salary_to} {self.currency}
Требования: {self.desc}
Описание работы: {self.resp}"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    # def __gt__(self, other):
    #     return self.salary_to > other.salary_to


