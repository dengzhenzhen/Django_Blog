# A Single Django Blog

This is a single blog demo built by Django.

## 1.Why I do this?
Daily work is so boring that I'm afraid of losing my python skills. So I'm tring to make some interesing demos for fun after work. The following plan is to update frontend and backend functions.

## 2.What's is made of?

|frontend        | backend|
|:--------------:|:------:|
|only HTML and JS| Django |
Django version: 2.0.7

python version : Anaconda 4.3.30

Check your python and django version
```powershell
PS C:\Users\BENCH\Documents\GitHub\Django_Blog> conda -V

conda 4.3.30

PS C:\Users\BENCH\Documents\GitHub\Django_Blog> python
Python 3.6.6 |Anaconda custom (64-bit)| (default, Jun 28 2018, 11:27:44) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import django
>>> django.VERSION
(2, 0, 7, 'final', 0)
>>>

```
I'm not sure if it can run in other environment successfully.

## 3.How to use?

### 1.Excute run.ps1 in powershell

### 2.If you don't want to run a powershell script on your shell, you could choose this:

-  Open powershell(or cmd with your like)
-  cd to project dir and excute following commands
   ```powershell
   python manage.py migrate
   python manage.py runserver   
   ```
   You should run 'migrate' command to init database when you run the server first time, then a database file db.sqlite3 would be created. You can start server using only 'runserver' command afterward.

   Default port is 8080, you can use 
   ```powershell
   python manage.py runserver 80
   ```
   to assign a port which your server runs on.

## 4. What to update in following versions?

- Complte frontend
- Beautfy  and modify frontend pages
- Add about page
- Try to refactoring frontend with frontend framework, 
for example, Vue
- Deploy this blog on a linux server with a shell file run.sh

## 5. Contact information
E-mail: zhenzhendeng2012@gmail.com

Wechat:
 <img src="https://dengzhenzhen.github.io/img/715e7edc65904110b0bb9b52e24272b1-560x560.jpg" width = "80" height = "80" alt="图片名称" align=center />

