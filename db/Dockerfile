FROM osmanirosado/dvdrental-database:2019.05

# Postgres docker image documentation fragment:
# "... initialization files will be executed in sorted name order as defined by the current locale, ..."
COPY init-db2.sh /docker-entrypoint-initdb.d/init-db2.sh
