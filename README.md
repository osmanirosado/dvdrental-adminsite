# DVD Rental Admin Site

Example project to explore Django admin site features using DVD Rental PostgreSQL sample database.

## Configuring the website

Start db service to setup DVD Rental database.

```shell script
docker-compose up db
```

Wait until the database system is ready to accept connections.

Apply database migrations for Django applications.

```shell script
docker-compose run web python manage.py migrate
```

Create a super user for Django admin site.

```shell script
docker-compose run web python manage.py createsuperuser
```

## Running the website

Start web service.

```shell script
docker-compose up
```

Open a web browser and go to http://localhost:8096.
