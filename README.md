# Janus Theme

A professional, enterprise-grade Django theme based on the Janus Design System.

## Installation

1.  **Package the theme**:
    Run this command inside the `janus_theme` folder (where `setup.py` is):
    ```bash
    pip install .
    ```
    Or to build a distributable wheel:
    ```bash
    python setup.py sdist bdist_wheel
    pip install dist/django-janus-theme-0.1.0.tar.gz
    ```

2.  **Add to Installed Apps**:
    In your `settings.py`:
    ```python
    INSTALLED_APPS = [
        ...
        'janus_theme',
        'django.contrib.admin',
        ...
    ]
    ```

3.  **Configure Templates**:
    Ensure your `TEMPLATES` setting enables `APP_DIRS`:
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,  # This must be True
            ...
        },
    ]
    ```

## Usage

Extend the base template in your views:

```html
{% extends "layouts/base.html" %}

{% block content %}
    <h1>My Project Page</h1>
{% endblock %}
```

## Customization


## Workflow & Distribution (Come usarlo su più progetti)

Hai 3 modi principali per distribuire questo tema sui tuoi progetti:

### 1. Metodo Git (Consigliato per Produzione)
Carica questa cartella su un repository privato (GitHub/GitLab).
Poi, nei tuoi progetti Django (o nel `requirements.txt`), installalo così:

```bash
pip install git+https://github.com/tuo-username/janus_theme.git
```
*Vantaggio:* Versionamento sicuro e facile deploy sui server.

### 2. Metodo Locale (Per Sviluppo)
Se lavori sullo stesso computer, installalo in modalità "editable". Le modifiche al tema si riflettono subito su tutti i progetti.

```bash
pip install -e /Users/lusva/Desktop/clienti/datastrike/janus_theme
```

### 3. Metodo File (Senza Git)
Crea un file `.whl` distribuibile:
```bash
python setup.py bdist_wheel
```
Prendi il file generato in `dist/` e installalo ovunque:
```bash
pip install django_janus_theme-0.1.0-py3-none-any.whl
```

