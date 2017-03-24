FROM python:3.5
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /poke
COPY ./poke /poke
EXPOSE 5000
CMD ["python", "app.py"]