### Fondation
Real Estate project

### configure virtual env:

* install virtual env package
* python3 -m pip install --user virtualenv
* create env
* python3 -m venv env
* activate env:
* source env/bin/activate
* deactivate env:
* deactivate


update requirements
* pip freeze > requirements.txt

run app:
* flask run or python fondation.py

### DB cmd
* flask db init
* flask db migrate -m "users table"
* flask db upgrade
* flask db downgrade
* flask shell


chrome reload ctrl + shift + R
shift + F5
Cmd + shift + R


### google cloud
https://cloud.google.com/sdk/docs/

* gcloud app deploy
* gcloud app browse
* gcloud app logs tail -s default


https://fondation.appspot.com/

### links
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
* https://www.jhanley.com/google-cloud-run-getting-started-with-python-and-flask/
* https://code.visualstudio.com/docs/python/tutorial-flask
* https://www.jhanley.com/google-cloud-run-getting-started-with-python-and-flask/
* https://medium.com/@zainqasmi/build-and-deploy-a-python-flask-application-on-google-cloud-using-app-engine-and-cloud-sql-a3c5bde5ef4a