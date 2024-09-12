'''Этот тестовый модуль последовательно создаёт, проверяет наличие
и удаляет репозиторий на сайте https://api.github.com/user/repos,
выводя в консоль соответствующую информацию'''
import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
GITHUB_API_URL = "https://api.github.com/user/repos"

def create_repository(repo_name):
    '''Функция создаёт репозиторий'''
    response = requests.post(
        GITHUB_API_URL,
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        json={"name": repo_name, "private": False},
        timeout=10
    )
    response.raise_for_status()  # Генерирует исключение для неудачного запроса
    return response

def check_repository_exists(repo_name):
    '''Функция проверяет наличие репозитория'''
    response = requests.get(
        GITHUB_API_URL,
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        timeout=10
    )
    response.raise_for_status()  # Генерирует исключение для неудачного запроса
    repositories = response.json()
    return any(repo['name'] == repo_name for repo in repositories)

def delete_repository(repo_name):
    '''Функция удаляет репозиторий'''
    response = requests.delete(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}",
        auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        timeout=10
    )
    response.raise_for_status()  # Генерирует исключение для неудачного запроса
    return response

def main():
    # Создание репозитория
    print("Создание репозитория...")
    try:
        create_response = create_repository(REPO_NAME)
        print("Репозиторий успешно создан.")
    except requests.exceptions.HTTPError as e:
        print("Ошибка при создании репозитория:", e.response.json())

    # Проверка наличия репозитория
    print("Проверка наличия репозитория...")
    if check_repository_exists(REPO_NAME):
        print("Репозиторий найден.")
    else:
        print("Репозиторий не найден.")

    # Удаление репозитория
    print("Удаление репозитория...")
    try:
        delete_response = delete_repository(REPO_NAME)
        print("Репозиторий успешно удален.")
    except requests.exceptions.HTTPError as e:
        print("Ошибка при удалении репозитория:", e.response.json())

if __name__ == "__main__":
    main()
