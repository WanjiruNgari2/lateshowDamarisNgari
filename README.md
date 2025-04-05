# lateshowDamarisNgari
This challenge contains a flask based API that manages episodes, guests and appearances of a show.


## setup instructions
1.create a private github repository with a readme and clone it to your text editor: 
       git clone https://github.com/your-usernamlateshow-your-name.git
       cd lateshow-your-name

2. create a virtual environment :
            python3 -m venv venv
            source venv/bin/activate

3. install dependencies you will need to run this app:
            pip install flask flask_sqlalchemy flask_migrate

4. create a folder (app) and inside it create files you will work with eg, models.py, seed.py, routes.py, config.py and init.py.

create a run.py that will run your app after development

5. this challenge uses this database, so just download it:
  https://moringa.instructure.com/courses/955/files/519127?wrap=1



### Actual code
Get into every file and code the requirements.Here is a guide:

init.py will initializethe whole project 

 models.py will contain the actual tables and thier relationships with each other.

routes.py must show various routes the user will use as the URL, so write the methods every route will use to communicate with th database.

seed.py file "plant" the tables as you specified in models.py and crete them all


#### run migrations and run the run.py 
tis will initialize the flask app and add all changes made:
                flask db init
                flask db migrate -m "Initial migration"
                flask db upgrade


then on your terminal run :
        python3 app/seed.py 
        python3 app/run.py so the app starts running


##### Testing
Use Postman to test all routes with their appropriate methods ie GET, POST, DELETE 

###### Author
Incase you have any questions or comments reach me at: 
names: Damaris Ngari
email: wanjirungari2@gmail.com
github repo: https://github.com/WanjiruNgari2/lateshowDamarisNgari.git

HAPPY CODING!!!!!!!









