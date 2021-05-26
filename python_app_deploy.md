# **Deploy**

## ***uwsgi + nginx***

1. **install nginx uwsgi**
> Sudo apt-get install nginx
>
> Pip install uwsgi
2. **Create wsgi.py**

- Content of wsgi.py
```python
from app import app
If __name__ == ‘__main__’:
    app.run()
```

- Test wsgi.py: 
> uwsgi --socket 0.0.0.0:5000 protocol http -w wsgi:app

3. **create app.ini**

- Content of app.ini:
```
[uwsgi]
module = wsgi:app

process = <n_process>
master = true

socket = app.socket
chmod-socket = 666

vacuum = true
die-or-term = true
```
4. **Create custom.service in /etc/systemd/system/custom.service**

- Content of custom.service:
```
[Unit]
Description=uWSGI instance to serve myproject
After=network.target

[Service]
User=<user>
Group=www-data
WorkingDirectory=<path to project>
Environment="PATH=<path to python environment>"
ExecStart=<path to uwsgi command> --ini app.ini

[Install]
WantedBy=multi-user.target
```

5. **Create custom.conf in /etc/nginx/site-available/custom.conf**

- Content of custom.conf
```
server {
    listen 80;
    server_name <your ip>;
    location / {
        include uwsgi_params;
        uwsgi_pass unix:<path to app.socket>
    }
}
```