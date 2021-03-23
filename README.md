# Stroke Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Future scope of project](#future-scope)

## Demo
Link: [https://stroke-pred.herokuapp.com/](https://stroke-pred.herokuapp.com/)

[![](https://imgur.com/hrzeTu2)](https://stroke-pred.herokuapp.com/)

[![](https://imgur.com/4kHueRv)](https://stroke-pred.herokuapp.com/)

## Overview
This is a Flask app which is helpful in stroke prediction based on certain attributes like age , hypertension ,heartdisease etc.

## Motivation
I'm glad that I have used this Pandemic situation for something which is productive,I have started learning data science and here I wanted to work on some real life data and did some projects regarding data science.This is one of my projects which helped me in learning new concepts and that is the motivation behind the deployment of this app.

## Installation
The Code is written in Python 3.7.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Here for this project I have used Heroku platform for deployment and it is free of cost and very needy for beginners. You can either link your github accout or you can use heroku cmd to deploy your model. Here my model is deployed from the github.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── static 
│   ├── css
├── template
│   ├── Index.html
├── Procfile
├── README.md
├── app.py
├── classification_model_design.ipynb
├── updated_model.sav
├── requirements.txt
├── eda.ipynb
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/Mandal-21/Flight-Price-Prediction/issues) here by including your search query and the expected result

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End 
