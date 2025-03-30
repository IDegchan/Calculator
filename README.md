# Проект: Калькулятор
Цей проект реалізує калькулятор за допомогою бібліотеки Flet для створення графічного інтерфейсу.<br/>
Проект має тестування за допомогою tox, pytest та ruff.<br/>
Для створення віртуального середовища використано uv.

### Встановлення та налаштування середовища
```bash
pip install uv
uv sync
uv pip install 'flet[all]==0.27.6' --upgrade
uv tool install tox --with tox-uv
uv tool update-shell
```

### Запуск
Для запуску программи введіть: `uv run src/main.py`

Для запуску тестів введіть: `uv tool run tox -q`
