import json
from datetime import datetime


# Загрузка данных из JSON-файла
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# Генерация отчета о наиболее популярных категориях товаров, проданных в декабре
def generate_report(data):
    # Создаем словарь для подсчета количества товаров в каждой категории
    categories_count = {}

    # Проходимся по каждому заказу
    for order in data:
        # Преобразуем дату и время заказа в объект datetime
        ordered_at = datetime.fromisoformat(order["ordered_at"])

        # Проверяем, что заказ был сделан в декабре
        if ordered_at.month == 12:
            # Проходимся по каждому товару в заказе
            for item in order["items"]:
                # Получаем имя категории товара
                category_name = item["category"]["name"]
                # Увеличиваем счетчик товаров в данной категории
                categories_count[category_name] = categories_count.get(category_name, 0) + 1

    # Получаем список наиболее популярных категорий и сортируем его по алфавиту
    popular_categories = sorted(categories_count.keys())

    # Формируем отчет в формате JSON
    report = {"categories": popular_categories}
    return json.dumps(report, ensure_ascii=False)


# Загружаем данные из файла JSON
input_data = load_data("input.json")
# Генерируем отчет
report = generate_report(input_data)
# Выводим отчет
print(report)
