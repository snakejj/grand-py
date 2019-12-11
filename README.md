# Grandpy

Grandpy is a website which allows anyone to find the address of a place, with a map and a little anecdote on it or something close to it, simply by asking a question like you would ask a human.

The address on which you can test it is here : https://samir-grandpy.herokuapp.com/

It uses a parser to get the location within the sentence it receive.

Grandpy is written in Python 3 with Flask, Javascript, HTML5 and CSS3.

## External ressources

The project rely on Wikipedia's API and HERE's API.
The script clean the user input and use the cleaned input to request the address and the gps coordinates of the place from HERE's API. The script then send the gps coordinates to the Wikipedia's API to get an article which gps coordinates are the closest to the gps coordinate of the place the user searched for.

It also uses the gps coordinates to display a map of the location thanks to the HERE's Map API (Javascript).

The script then takes all the informations and display them on the page.

## Dependencies

Use pipenv to 
install all the dependencies contained in the Pipfile.lock. 
Here are the steps :

1. Open the command prompt.  
2. cd to the project directory's root, where pipfile.lock is located
3. Run this command in your shell:  

```bash
pipenv install
```

## Configuration :

To work on the project, you will need to add a .env at the root of the project folder, and adding these values :

HERE_APP_ID = your api key for HERE'S "Places API"  
HERE_APP_CODE = your api code for HERE'S "Places API"  
HERE_JS_MAP = your api key for HERE'S "Marker on the Map API"  
FLASK_APP = the name of the entrancy file for Flask
FLASK_DEBUG = set to 1 in Debug mode, and 0 if not

## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Copyleft](https://www.gnu.org/licenses/copyleft.fr.html)