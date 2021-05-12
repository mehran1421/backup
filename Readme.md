# Backup database 

**There are many methods for backup from database Including the use of Docker and ...**

**We used two methods
1- Using the django-dbbackup package
2- Using dumpdata that is available in the database**

# Install required packages and Run django-dbBackup:
**Automatic backup
make file in drive D://my-backup**
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
celery -A backup beat -l info
celery -A backup worker -P gevent --loglevel=INFO
```
**for exclude table**
```
DBBACKUP_CONNECTORS = {
    'default': {
       ...
        'EXCLUDE': 'dbBackup_test',
        ...
    }
}
```
**for remove backup everyday**
```
DBBACKUP_CONNECTORS = {
    'default': {
        ...
        'CLEANUP_KEEP': 5 #1,2,3,... day
    }
}
```
**for backup media file**
```
@shared_task
def backup():
    management.call_command('dbbackup')
    management.call_command('mediabackup')
```


# Install required packages and Run dumpdata way:
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
**for backup from dumpData.Post table**
```
python manage.py dumpdata --indent 2 dumpData.Post > db.json
```
**for exclude table**
```
python manage.py dumpdata --indent 2 --exclude dumpData.Post dumpData > db.json
```
**for save yaml format**
```
pip install pyyaml
python manage.py dumpdata --indent 2 dumbData.Post > db.yaml
```
**we can delete database or write Code below**
```
python manage.py flush
```
**load data from backup**
```
python manage.py loaddata db.json
```