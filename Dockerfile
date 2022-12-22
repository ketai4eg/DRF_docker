FROM python:3.10

COPY ./requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

# RUN python3 manage.py migrate

# RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src

EXPOSE 6060

WORKDIR src

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


# CMD ["python3", "manage.py", "runserver", "0.0.0.0:6060"]