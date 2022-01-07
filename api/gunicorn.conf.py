import multiprocessing

wsgi_app = 'wsgi:app'
errorlog = 'gunicorn.log'
loglevel = 'debug'
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 3