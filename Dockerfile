FROM python

# set a directory for the app
WORKDIR /app/webservices

# install dependencies
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN rm requirements.txt
RUN pip install django
RUN pip install djangorestframework
RUN pip install psycopg2

# tell the port number the container should expose
EXPOSE 8000

