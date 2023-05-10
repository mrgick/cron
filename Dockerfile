FROM python:3.10.9-slim

WORKDIR /cr

COPY ./requirements.txt /cr/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /cr/requirements.txt

COPY ./app /cr/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]