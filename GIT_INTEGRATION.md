# Guida all'Integrazione tramite Git

Questa guida spiega come utilizzare **Janus Theme** in qualsiasi nuovo o esistente progetto Django utilizzando Git. Questo è il metodo più professionale per gestire il design system centralizzato.

## Prerequisiti

Assicurati che il codice del tema (`janus_theme`) sia stato caricato su un repository Git (GitHub, GitLab, Bitbucket, etc.).

---

## Passo 1: Installazione

Nel tuo **nuovo progetto Django**, modifica il file `requirements.txt`.
Aggiungi la riga seguente per dire a `pip` di scaricare il tema direttamente dal repository.

```text
# requirements.txt

Django>=4.0
# ... altre dipendenze ...

# Aggiungi questa riga (sostituisci la URL con la tua reale):
git+https://github.com/IL-TUO-USERNAME/janus_theme.git@main#egg=django-janus-theme
```

*Nota: Se il repository è privato, potresti dover configurare le chiavi SSH o usare un token personale nella URL.*

Esegui l'installazione:
```bash
pip install -r requirements.txt
```

---

## Passo 2: Configurazione

Apri il file `settings.py` del tuo progetto e aggiungilo alla lista `INSTALLED_APPS`.
È importante aggiungerlo **prima** delle app standard se prevedi di sovrascrivere template di default (come il login di admin), altrimenti l'ordine non è critico ma consigliato.

```python
# settings.py

INSTALLED_APPS = [
    'janus_theme',          # <--- AGGIUNGI QUI
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... le tue app ...
]
```

Assicurati che `APP_DIRS` sia attivo nei settings dei template (lo è di default):

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, # <--- Deve essere True
        # ...
    },
]
```

---

## Passo 3: Utilizzo nei Template

Ora il tema è disponibile. Non devi copiare nessun file CSS o HTML.
Crea le tue viste e nei template HTML estendi semplicemente `layouts/base.html`.

Esempio `home.html`:

```html
{% extends "layouts/base.html" %}

{% block title %}Nuovo Progetto - Home{% endblock %}

{% block content %}
    <div class="card">
        <h1>Benvenuto!</h1>
        <p>Questa pagina eredita automaticamente lo stile Janus.</p>
        <button class="btn btn-primary">Bottone Prova</button>
    </div>
{% endblock %}
```

---

## Come Aggiornare il Tema

Se apporti modifiche al repository centrale del tema (es. cambi un colore o aggiungi un componente), per scaricare l'aggiornamento nel tuo progetto esegui:

```bash
pip install --upgrade --force-reinstall git+https://github.com/IL-TUO-USERNAME/janus_theme.git@main#egg=django-janus-theme
```
