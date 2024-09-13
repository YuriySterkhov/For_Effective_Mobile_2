# GitHub API Test

Этот проект предназначен для автоматического тестирования работы с GitHub API на Python. Он включает в себя создание, проверку наличия и удаление репозитория на GitHub.

## Настройка переменных окружения

1. Сверните окно CLI Windows.
2. Используя проводник Windows, найдите и откройте в клонированном репозитории папку GitHub API.
3. Командой контекстного меню "Открыть с помощью" откройте файл env. в "Блокнот".

Содержимое файла .env:

GITHUB_USERNAME=your_github_username

GITHUB_TOKEN=your_github_token

REPO_NAME=your_test_repository_name

Замените your_github_username, your_github_token и your_test_repository_name на ваши реальные данные.
4. Сохраните изменения в файле .env.
5. Закройте окно "Блокнот".
6. Разверните окно CLI Windows.

## Установка

1. Убедитесь, что в CLI Windows открыта папка GitHub API.
2. Командами CLI Windows
    - установите виртуальное окружение: `python -m venv venv`
    - активируйте виртуальное окружение: `venv\Scripts\activate`
    - установите в виртуальное окружение дополнительные пакеты: `pip install -r requirements.txt`

## Запуск теста

Командой CLI Windows запустите тест: `python test_api.py`

## Ожидаемый результат

Тест последовательно создаёт, проверяет наличие и удаляет репозиторий на GitHub,
сопровождая действия соответствующими сообщениями в окне CLI Windows.

## Завершение работы

1. Командой CLI Windows деактивируйте виртуальное окружение: `venv\Scripts\deactivate`.
2. Закройте окно CLI Windows.
3. Удалите ваши реальные данные из файла env.