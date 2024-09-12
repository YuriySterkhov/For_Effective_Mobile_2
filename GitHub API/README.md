# GitHub API Test

Этот проект предназначен для автоматического тестирования работы с GitHub API на Python. Он включает в себя создание, проверку наличия и удаление репозитория на GitHub.

## Установка зависимостей

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Клонируйте репозиторий на свой компьютер:
                                            git clone https://github.com/your_username/your_project.git
                                            cd your_project
3. Установите необходимые зависимости:   
                                            pip install -r requirements.txt

## Настройка переменных окружения

Создайте файл `.env` в корне проекта и заполните его следующими переменными:

GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
REPO_NAME=your_test_repository_name

Замените `your_github_username`, `your_github_token` и `your_test_repository_name` на ваши реальные данные.

## Запуск теста

Запустите скрипт:
                                            python test_api.py

Скрипт создаст репозиторий, проверит его наличие и удалит его после проверки.

### Инструкция по использованию

1. Создайте репозиторий на GitHub, чтобы получить ваш токен.
2. Заполните файл `.env` своими данными.
3. Установите зависимости из `requirements.txt`.
4. Запустите скрипт `test_api.py` для выполнения теста.