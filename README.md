<h1 align="center">
  COVID APP
  <br>
</h1>

<h4 align="center"><a href="https://www.djangoproject.com/" target="_blank">Django</a> application for monitoring infected and vaccinated students and employees of various faculties at any university in Croatia. The site administrator adds information about students and employees to the database and displays it to other users of the application.

<p align="center">
  <img src="https://media1.giphy.com/media/alZEK9G3DdI1aR25Ak/giphy.gif?cid=790b7611a8c5446d9757471b570dc98903db2791fd22aa4e&rid=giphy.gif&ct=g" alt="wsite" />
</p>




## How To Use

For the project to work you will need to configure Python and Django on your machine. To do so you can run the following:

```bash
sudo apt install python-is-python3 python3-pip pylint
sudo apt install python3-django
```

### Runing the client:
Clone this repository
```bash
$ git clone https://github.com/DBDoco/Covid-APP.git
```

Go into the repository
```bash
$ cd Covid-APP
```

Run client on local machine
```bash
$ ./manage.py runserver
```

## Testing:
```bash
# Model testing
$ ./manage.py test main.test.modelsCjepivo
$ ./manage.py test main.test.modelsFakultet

# Running Factory Boy:
$ ./manage.py setup_test_data
```

## Admin login:
Username: admin<br>
Password: admin
