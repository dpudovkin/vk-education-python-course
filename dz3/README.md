## Запуск NGINX
```bash
sudo nginx  -c  ~/vk/education/dz3/nginx/nginx.conf
```

## Запуск Gunicorn
```bash
gunicorn myapp:app
```

## Apache Benchmark
```bash
ab -n 10000 -c 100  http://127.0.0.1:8000 > test/gunicorn.txt
ab -n 10000 -c 100  http://127.0.0.1:8080/index.html > test/nginx.txt
ab -n 10000 -c 100  http://127.0.0.1:8080/api > test/gunicorn_nginx_proxy.txt
```

