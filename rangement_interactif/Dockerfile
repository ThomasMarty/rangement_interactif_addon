FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app


RUN chmod +x /app/run.sh


EXPOSE 5000
CMD ["/app/run.sh"]
