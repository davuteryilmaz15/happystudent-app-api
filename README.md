# django-blog-app

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/davuteryilmaz15/happystudent-app-api.git
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

For sending email via smtp add email and password to settings.py file.
```
SMTP_EMAIL = {
    'from_addr_email': 'example@gmail.com',
    'from_addr_password' : 'secret',
}
```
After all these steps, you can start testing and developing this project. 

#### That's it! Happy Coding!
