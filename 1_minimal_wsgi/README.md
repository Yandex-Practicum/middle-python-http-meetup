# Local run

## Requirements

```shell
pip install -r requirements.txt
```

## uWSGI

```shell
uwsgi --module wsgi:application --http-socket 0.0.0.0:8000 --honour-stdin --workers 1 --enable-threads
```

## Gunicorn

```shell
gunicorn -c infra/gunicorn.conf.py
```
