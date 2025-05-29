import requests
from bs4 import BeautifulSoup

def get_drom_ads():
    url = 'https://auto.drom.ru/'  # Главная страница авто
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Ошибка доступа: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Найти все ссылки на объявления
    ads = soup.find_all('a', href=True, limit=20)  # Ищем все ссылки

    car_list = []
    for ad in ads:
        link = ad['href']
        if "auto.drom.ru" in link and "catalog" not in link:  # Проверяем, что это не каталог
            title = ad.text.strip() or "Автомобиль без названия"
            car_list.append(f"{title}: {link}")

    if not car_list:
        print("❌ Объявления не найдены.")
        return None

    return car_list

# Функция записи в файл
def save_to_file(data):
    with open("drom_ads.txt", "w", encoding="utf-8") as file:
        for line in data:
            file.write(line + "\n")

if __name__ == "__main__":
    ads = get_drom_ads()
    if ads:
        save_to_file(ads)
        print("✅ Объявления успешно сохранены в drom_ads.txt!")
    else:
        print("⚠️ Ошибка: объявления не получены.")
