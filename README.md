
# QA Portfolio by Anton Krupnov

Добро пожаловать в моё портфолио QA-инженера! Здесь собраны примеры ручного и автоматизированного тестирования, включая:
- автотесты на Python с использованием Pytest
- тестирование API
- генерация отчётов через Allure
- запуск тестов через GitHub Actions (CI/CD)
- документация, баг-репорты, чек-листы, тест-кейсы

---

## Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Как запустить](#как-запустить)
- [Allure-отчёт](#allure-отчёт)
- [Документация](#документация)
- [Контакты](#контакты)

---

## Технологии

- Python 3.10+
- Pytest
- Requests
- Allure
- Postman
- GitHub Actions
- JSON, Markdown
- Ручное тестирование: баг-репорты, чек-листы, тест-кейсы

---

## Структура проекта

```
QA_portfolio/
│
├── tests/                  # Автоматические тесты
├── docs/                   # Документы (чек-листы, баги, кейсы)
├── allure-report/          # Allure отчёты
├── .github/workflows/      # CI (GitHub Actions)
├── postman/                # Коллекции и окружения Postman
├── requirements.txt        # Зависимости проекта
└── README.md
```

---

## Как запустить

1. Клонируйте проект:
```bash
git clone https://github.com/Krupn0v/QA_portfolio.git
cd QA_portfolio
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Запустите тесты:
```bash
pytest -v
```

4. Для генерации Allure-отчёта:
```bash
pytest --alluredir=allure-results/
allure serve allure-results/
```

---

## Allure-отчёт



[Allure-отчёт](https://krupn0v.github.io/QA_portfolio/) будет автоматически собираться в GitHub Actions при каждом пуше.
Можно просматривать его локально командой `allure serve`.

---

## Документация

- `docs/test-cases` — тест-кейсы
- `docs/checklists` — чек-листы
- `docs/bug-reports` — баг-репорты

---

## Контакты

- Telegram: [@krupn0v](https://t.me/krupn0v)
- Email: antonkrupnov2710@gmail.com

---

**Спасибо за просмотр!**  
Если у вас есть вопросы или предложения — буду рад пообщаться.
