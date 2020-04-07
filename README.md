# Course repository for: Special Course in Computer Science: Advanced Topics in Systems for Big Data and Machine Learning


This project includes the course project and [study logs](https://github.com/jonatanvm/s4ml-project/tree/master/uploads/study-logs) done during the course.

### How to run

Clone repository  

`git clone git@github.com:jonatanvm/s4ml-project.git`

`cd s4ml-project`

Start and initialize new virtual environment  

`virutualenv venv`

`source venv/bin/activate`

Install requirements (and update pip)  

`pip install --upgrade pip`
`pip install -r requirements.txt`

The easiest way to run the project by using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).  

If you have it installed simply create and `.env` file in the root folder with the contents:

`SECRET_KEY=YOURSECRETKEY`

Then you can just run the project with:

`heroku local`

#### _Hard way_

If you don't have Heroku CLI you need to run all the subprocesses individually:

```
export DJANGO_SETTINGS_MODULE='s4project.settings'
export SECRET_KET=YOURSECRET
python manage.py runserver
python get_price_data.py
python run_models.py
```

If you run `get_price_data.py` and `run_models.py` in different terminals you need to run `export DJANGO_SETTINGS_MODULE='s4project.settings'` in each terminal.


### Uploading model

On the main page click **Add model**.

The attached python script must have two methods: `run_test` and `predict`

`run_test` takes an array of the most recent data as a parameter and must return a tuple `rmse, mae, r2, profit, accuracy, parameters`
, where all the values are floats except `paremeters` which is a dictionary of the parameters of the model.

`predict(X, y, p)` takes the price data `y`, the time data `X` and value to predict `p` as arguments and must return the tuple `prediction, parameters` where `prediction` is the predicted value and `parameters` is a dict of parameters used in the model.