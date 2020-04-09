# LEOCET

LEOCET is part of a student project at CentraleSupélec. This software simulates body orbits in the LEO and estimates the probability of a collision between a satellite and debris.

## Install and configure the project

To install and enable the project on your computer you have to follow these steps :
1. Check that *git* and *Python 3.7* are properly installed and functionnal on your computer;
2. On *GitHub* click on "Clone or download" button then copy the link;
3. On your computer, open a terminal as administrator and navigate to the director where you want to install *LEOCET*;
4. In the terminal compute the following command `git clone <GitHub_link>`;

Now the project is downloaded on our machine. To run the app you have to install the dependencies. For this we recommand the creation of a virtual environment. To achieve that follow these steps :
1. Check that the python package manager *pip* is properly installed on your computer;
2. In a terminal enter the command `pip install virtualenv`;
3. Then enter the command `virtualenv -p python3 env`;
4. To lanch the virtual environment enter the command : `source env/bin/activate` if your OS is MacOS or Linux and 'env\scripts\activate' if your OS is Window
5. Finally enter the command `pip install -r requirements.txt`;
6. To leave the virtual environment enter the command `deactivate`.

Now the project is fully functional. You can run it by entering the command `python app.py` in the directory *app*.

## Project structure

## Participate in the maintenance and development of the project

### Best practices

In order to ensure that the project code reamins readable and usable, a number of rules must be followed. The main rules are the followings :
* Use virutalenv as python interpreter.
* When you have to install an new package use *pip* package manager (use the command `pip install <package_name>`) and don't forget to update the file *requirements.txt* (use the command `pip freeze > requirements.txt` in the virtual environment).
* Comply with PEP8 conventions by using *pylint* (see [here](https://www.pylint.org/))

### What's left to code?

This project is obviously not totally achieved! There are many thing that could be completed. The trajectory predictor is a basic one and you can try to improve it.
