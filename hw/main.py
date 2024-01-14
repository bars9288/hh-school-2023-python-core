from wine import Wine
from beer import Beer
from market import Market

krasnoe_beloe = Market([],[],'Красное Белое после 22-00')

# Девушкам завезли Вино
krasnoe_beloe.wines.append(Wine('Солнечная долина','1990-05-15'))
krasnoe_beloe.wines.append(Wine('Коктебель','2000-05-15'))
krasnoe_beloe.wines.append(Wine('777','2023-05-15'))
krasnoe_beloe.wines.append(Wine('Шато Бриньон','1995-05-15'))
krasnoe_beloe.wines.append(Wine('Совиньон Блан','1980-05-15'))

# Парням завезли Пиво
krasnoe_beloe.beers.append(Beer('КерСари','2020-05-15'))
krasnoe_beloe.beers.append(Beer('Балтика','2021-05-15'))
krasnoe_beloe.beers.append(Beer('Крушовице','2019-05-15'))
krasnoe_beloe.beers.append(Beer('Василеостровская пивоварня','2021-05-15'))   # <= Очень вкусное пиво кстати !!
krasnoe_beloe.beers.append(Beer('Афанасий','2021-05-15'))


result_task1 = krasnoe_beloe.get_drinks_sorted_by_title()
result_task2 = krasnoe_beloe.has_drink_with_title('777')
result_task3 = krasnoe_beloe.get_drinks_by_production_date('1900-01-01','1999-12-31')