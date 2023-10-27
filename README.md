# DVD Rental Admin Site

Example project to explore Django admin site features using DVD Rental PostgreSQL sample database.

## Configuring the website

Apply database migrations.

```shell script
docker compose run web python manage.py migrate
```

Create a super user.

```shell script
docker compose run web python manage.py createsuperuser
```

## Running the website

Start the web service.

```shell script
docker compose up
```

Open a web browser and go to http://localhost:8096.
