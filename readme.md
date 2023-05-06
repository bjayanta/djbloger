# Blog

## Installation

1. Create Virtual environment and Start
2. Install all packages from requirements.txt file
3. Configure database

## Generate random secret key

```bash
python manage.py shell

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

## Environment Variables

Step 1: Installation:

```bash
pip install python-dotenv
```

Step 2: Configure into base.py:

```python
from dotenv import load_dotenv
import os

# Load ".env" file
load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "True"
```

Step 3: Create .env file

## Testing

Step 1: Installation

```bash
pip install pytest
pip install pytest-cov
```

Step 2: Create pytest.ini file

insert all the code bellow into the "pytest.ini" file

```ini
[pytest]
DJANGO_SETTINGS_MODULE = blog.settings.local
python_files = test_*.py
```

Step 3: Create tests into "tests" directory in apps

For example:

```py
def test_example():
    assert 1 == 1
```

Step 4: Run test

```bash
pytest
```

or

```bash
pytest --cov
```

or, Generate report (HTML) in root directory

```bash
pytest --cov-report html --cov=./
```

## Code formatter

Step 1: Black is the uncompromising Python code formatter.

```bash
pip install black
```

Step 2: Create .vscode directory

Step 3: Create settings.json file into the .vscode directory

Step 4: Install linting tool

```bash
pip install flake8
```

Step 5: Insert all the code bellow into the "settings.json" file

```json
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "88"
    ],
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length",
        "88",
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
}
```

## MySQL Configure

Step 1: Installation

```bash
pip install mysqlclient
```

Step 2: Goto settings file and configure

```py
"default": {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "<database name>",
    "USER": "<username>",
    "PASSWORD": "<password>",
    "HOST": "localhost",
    "PORT": "3306",
}
```

## Factory

Step 1: Installation

```bash
pip install factory-boy
```

Thank you.
