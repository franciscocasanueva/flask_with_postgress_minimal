FROM python:3
EXPOSE 5000
WORKDIR /usr/scr/app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app .

CMD ["python", "app.py"]