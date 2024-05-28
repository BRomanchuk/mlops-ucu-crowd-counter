FROM python:3.10
EXPOSE 5555

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install libgl1 -y

COPY . .

CMD ["python", "app.py"]