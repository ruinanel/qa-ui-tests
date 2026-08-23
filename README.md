# UI-автотесты (Playwright + Page Object)

![UI tests](https://github.com/ruinanel/qa-ui-tests/actions/workflows/tests.yml/badge.svg)
![Allure UI report](https://github.com/ruinanel/qa-ui-tests/actions/workflows/allure.yml/badge.svg)

📊 **Live Allure-отчёт:** https://ruinanel.github.io/qa-ui-tests/ (обновляется в CI)


E2E-автотесты веб-интерфейса на Python с паттерном **Page Object Model**.
Тестируемый сайт — [saucedemo.com](https://www.saucedemo.com) (демо-магазин).

## Стек
- Python 3.12
- Playwright — управление браузером
- pytest + pytest-playwright
- Page Object Model — страницы как классы

## Структура
```
qa-ui-tests/
├── pages/                  # Page Objects (страницы как классы)
│   ├── base_page.py        # BasePage — общий родитель
│   ├── login_page.py       # страница логина
│   └── inventory_page.py   # страница товаров
├── tests/
│   ├── conftest.py         # фикстура login_page
│   ├── test_login.py       # примеры
│   └── test_your_turn.py
├── pytest.ini
└── requirements.txt
```

## Запуск
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m playwright install chromium   # скачать браузер (один раз)

pytest -v                # headless (без окна)
pytest -v --headed       # с открытым браузером — видно, что происходит
pytest -v --slowmo 500   # замедлить действия (мс) — удобно смотреть
```

## Что покрыто
- Успешный вход
- Негативные сценарии: неверный пароль, заблокированный пользователь, пустые поля
- Проверка страницы товаров после входа
- Паттерн Page Object: локаторы и действия внутри классов страниц, тесты — только бизнес-шаги
