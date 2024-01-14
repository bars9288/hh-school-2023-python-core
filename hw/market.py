from datetime import date
import time


# Написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Begin")
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"End {total_time:.2f} sec.")
        return result
    return wrapper


class Market:
    together_all_drinks = []
    together_all_drinks_titels = []
    def __init__(self, wines: list, beers: list, title):
        self.wines = wines if(len(wines) > 0) else []
        self.beers = beers if(len(beers) > 0) else []
        self.title = title


# Метод получения списка напитков (вина и пива) отсортированных по title - СПИСОК ОБТЕКТОВ
    @logger
    def get_drinks_sorted_by_title(self):
        if (len(self.together_all_drinks) == 0):
            self.together_all_drinks = self.wines + self.beers
        def sort_key(s):
            return s.title

        for tmp in self.together_all_drinks:
                self.together_all_drinks_titels.append(tmp.title)

        return sorted(self.together_all_drinks, key=sort_key)


# Проверяет наличие напитка в магазине за О(1)
    @logger
    def has_drink_with_title(self, title):
        return title in self.together_all_drinks_titels


# Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date
    @logger
    def get_drinks_by_production_date(self, from_date, to_date):
        result = []
        from_date = date.fromisoformat(from_date)
        to_date = date.fromisoformat(to_date)

        for tmp in self.together_all_drinks:
            drink_date = date.fromisoformat(tmp.production_date)

            if (from_date < drink_date < to_date):
                result.append(tmp)
        return result