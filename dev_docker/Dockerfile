FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./app/requirements.txt
COPY . .
CMD [ "python", "main.py" ]