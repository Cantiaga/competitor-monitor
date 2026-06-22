# 🔍 Мониторинг конкурентов - AI Ассистент

MVP приложение для анализа конкурентной среды с поддержкой мультимодальности (текст и изображения).

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-purple.svg)

## 📋 Описание

Приложение позволяет:
- **Анализировать текст конкурентов** — получать структурированную аналитику с сильными/слабыми сторонами, уникальными предложениями и рекомендациями
- **Анализировать изображения** — баннеры, скриншоты сайтов, упаковки товаров с оценкой визуального стиля
- **Парсить сайты** — автоматически извлекать и анализировать контент по URL
- **Хранить историю** — последние 10 запросов сохраняются для быстрого доступа

## 🚀 Быстрый старт

### 1. Клонирование и установка зависимостей

```bash
# Клонируйте репозиторий
cd competitor-monitor

# Создайте виртуальное окружение
python -m venv venv

# Активируйте окружение
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Установите зависимости
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
OPENAI_VISION_MODEL=gpt-4o-mini
```

Получить API ключ: https://platform.openai.com/api-keys

### 3. Запуск приложения

```bash
# Запуск сервера
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Приложение будет доступно по адресу: http://localhost:8000

## 📁 Структура проекта

```
competitor-monitor/
├── backend/
│   ├── __init__.py
│   ├── main.py              # FastAPI приложение
│   ├── config.py            # Конфигурация
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py       # Pydantic модели
│   └── services/
│       ├── __init__.py
│       ├── openai_service.py    # Работа с OpenAI API
│       ├── parser_service.py    # Парсинг веб-страниц
│       └── history_service.py   # Управление историей
├── frontend/
│   ├── index.html           # HTML страница
│   ├── styles.css           # Стили
│   └── app.js               # JavaScript логика
├── requirements.txt         # Зависимости Python
├── env.example.txt          # Пример .env файла
├── history.json             # Файл истории (создаётся автоматически)
├── README.md                # Этот файл
└── docs.md                  # Документация API
```

## 🔧 Функциональность

### Анализ текста (`/analyze_text`)
- Принимает текст конкурента (минимум 10 символов)
- Возвращает:
  - Оценка визуального стиля (0-10)
  - Целевая аудитория
  - Сильные стороны
  - Слабые стороны
  - Уникальные предложения
  - Рекомендации по улучшению
  - Общее резюме

### Анализ изображений (`/analyze_image`)
- Принимает изображения: PNG, JPG, GIF, WEBP
- Возвращает:
  - Описание изображения
  - Целевая аудитория
  - Маркетинговые инсайты
  - Оценку визуального стиля (0-10)
  - Рекомендации

### Парсинг сайтов (`/parse_demo`)
- Принимает URL сайта
- Извлекает: title, h1, первый абзац
- Автоматически анализирует извлечённый контент

### История (`/history`)
- Хранит последние 10 запросов
- Сохраняет тип запроса, краткое описание, время

## 🛠️ Технологии

- **Backend**: FastAPI, Python 3.9+
- **AI**: OpenAI GPT-4o-mini (или GPT-4o, GPT-4-turbo)
- **Frontend**: Vanilla JS, CSS3
- **Парсинг**: BeautifulSoup4, httpx
- **Валидация**: Pydantic

## 📖 API Документация

После запуска сервера доступна интерактивная документация:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Подробная документация API в файле [docs.md](docs.md)

## ⚠️ Требования

- Python 3.9+
- OpenAI API ключ (https://platform.openai.com/api-keys)
- Интернет-соединение для работы AI и парсинга

## 📝 Лицензия

MIT License

