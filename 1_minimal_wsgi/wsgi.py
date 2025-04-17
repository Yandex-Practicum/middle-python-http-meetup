def application(environ, start_response):
    print(f'{environ.get("X-Real-IP", environ.get("HTTP_X_REAL_IP"))=}')
    print(f'{environ.get("X-Forwarded-For", environ.get("HTTP_X_FORWARDED_FOR"))=}')
    print(f'{environ.get("X-Forwarded-Proto", environ.get("HTTP_X_FORWARDED_PROTO"))=}')
    print(f'{environ.get("Host", environ.get("HTTP_HOST"))=}')

    print(f'{environ["QUERY_STRING"]=}')

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    print(f'{environ["wsgi.input"].read(request_body_size)=}')

    server = None

    if 'gunicorn.socket' in environ:
        server = 'gunicorn'
    elif 'uwsgi.version' in environ:
        server = 'uwsgi'

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [f"<h1'>Hello from Ilias ({server})!</h1>".encode()]
