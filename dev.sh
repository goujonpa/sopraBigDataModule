# source venv
source venv/bin/activate

# database start command
alias database_start='pg_ctl -D /usr/local/var/postgresql/data/ -l /usr/local/var/postgresql/psql.log start'

alias startproj='python manage.py supervisor'
