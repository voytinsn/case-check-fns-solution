# Пример получения сведений о проверке контрагентов из ФНС

## Требования
- должен быть установлен Docker
- должен быть установлен Python 3.9+

## Быстрый старт
Запуск контейнеров с тестовым окружением
```bash
git clone https://github.com/voytinsn/case-check-fns-solution.git
cd case-check-fns-solution
docker compose up -d
```

Теперь можно перейти на http://127.0.0.1:8080/ для просмотра изначального состояния БД crm, возможно придется подождать 15-20 секунд

Перед запуском приложения нужно подготовить файл с переменными окружения
```bash
mv example.env .env
```

Чтобы избежать конфликта зависимостей нужно создать виртуальное окружение для python

MacOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

Windows
```cmd
python -m venv venv
venv\Scripts\activate
```

Запуск приложения
```bash
pip install -r requirements.txt
python src/main.py
```
