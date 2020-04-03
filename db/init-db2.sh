#!/bin/bash
set -e

# Problem:
# Django 2.2 does not support composite primary keys
# Solution:
# Replace each composite primary keys by a unique together constraint and a simple auto increment surrogate key
# References:
# https://www.postgresqltutorial.com/postgresql-unique-constraint/
# https://dba.stackexchange.com/questions/103074/drop-primary-key-without-dropping-an-index
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "dvdrental" <<-EOSQL

CREATE UNIQUE INDEX CONCURRENTLY film_actor_unique
    ON film_actor (film_id, actor_id);
ALTER TABLE film_actor
    DROP CONSTRAINT film_actor_pkey,
    ADD CONSTRAINT film_actor_unique UNIQUE USING INDEX film_actor_unique,
    ADD COLUMN film_actor_id SERIAL PRIMARY KEY;

CREATE UNIQUE INDEX CONCURRENTLY film_category_unique
    ON film_category (film_id, category_id);
ALTER TABLE film_category
    DROP CONSTRAINT film_category_pkey,
    ADD CONSTRAINT film_category_unique UNIQUE USING INDEX film_category_unique,
    ADD COLUMN film_category_id SERIAL PRIMARY KEY;

EOSQL
