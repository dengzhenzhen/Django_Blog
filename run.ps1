if(Test-Path .\db.sqlite3){
    python .\manage.py runserver
}
else{
    python .\manage.py makemigrations
    python .\manage.py migrate
    $text = 'Create a superuser so that you can manage your blog on yoursite/admin'
    $text
    python .\manage.py createsuperuser
    python .\manage.py runserver
    
}