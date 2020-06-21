# make-flask-api
Cli to create rest api structure

## Note: 

* This project use [Poetry](https://python-poetry.org/) as  packaging and dependency management
* This project was created to work with [blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/), [Pluggable Views](https://flask.palletsprojects.com/en/1.1.x/views/), [marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) and [sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)(Read pleace)
* It provides a standard method to be implemented with url rule, this method allows to perform the operations based on a CRUD
* Install [nerdfonts](https://www.nerdfonts.com)

## Install
1. clone repositoy
2. access the folder
3. execute this command "sudo cp mfa /usr/local/bin"

## Options

| flags  |   |
|---|---|
| -n  [name]| Create new project|
| -i| Init in the current folder|
| -d| Create new docker file for [devcontainer](https://code.visualstudio.com/docs/remote/containers) plugin of vscode|
| -p| Install dependency with [poetry](https://python-poetry.org/)|

## Examples

mfa -n app  //creates a new project named app
mfa -i  //initialize the project in the current folder
mfa -p //Install dependency
mfa -id //initialize and create docker file
mfa -pd //iInstall dependency and create docker file
mfa -n app -d // new project and create docker file
mfa -n app -p // new project and Install dependency

## Important
If you have ideas for improvements you are free to make suggestions or do it yourself, all contributions are welcome
