# dotdot: reborn

this is the "2.0" version of the dot matrix printer robot interface, hopefully more extensible this time.

the goal is mostly to be an exercise in writing a flask application.

## things to keep in mind

this api will directly interface with a printer, for local testing, we are using an `epson lq-1500` dot matrix printer.

## api endpoints

- `/` [GET]: tests api functionality.
- `/print` [POST] send escaped and formatted POST data to printer. 
  - `/print/test` [POST] prints predefined test page to printer.  
  - `/print/raw` [POST] sends raw POST data to printer.
  - `/print/ascii` [POST] take input test and convert to large ASCII art text.
  - `/print/image` [POST] take input image and convert to ASCII art. (maybe just directly output??)
- `/bell` [POST] rings the printer bell.

## setup

this project was setup using a python virtual enviroment and flask.

1. clone the repository with `$ git clone git@github.com:makeopensource/dotdotbot.git`
2. then change into the directory `$ cd dotdotbot`
3. setup your python virtual enviroment `$ python3 -m venv venv`
4. activate your new virtual enviroment with`$ .venv/bin/active`
5. install requirements using pip `$ pip install -r requirements`
6. finally, run the app using flask `$ flask run`

