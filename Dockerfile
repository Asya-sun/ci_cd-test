FROM python:3.12.8-slim

WORKDIR /app  # Создаём рабочую директорию
COPY . .      # Копируем весь код проекта в /app

CMD ["python", "-m", "unittest", "discover", "tests"]  # Запуск тестов