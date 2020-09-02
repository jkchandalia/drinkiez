# libations
## Overview

libations is a cocktail recommendation system using data from the TheCocktailDB (https://www.thecocktaildb.com/). This database is accessible via API and provides a name and picture of each cocktail along with an ingredients list and a recipe. libations has a simple UI created with Django that allows a user to input an ingredient from a drop down menu and then find cocktails that use the ingredient. 

Once a cocktail is chosen, the application can recommend other cocktails that are similar to the chosen cocktail. 

## Recommendations

Recommendations for new cocktails are made using a similarity score based on overlapping ingredients between cocktails. Future versions of this application will include a more robust representation of the ingredient space (e.g., Absolut Vodka is a type of vodka and Bacardi is a type of rum) as well as an understanding of cocktail archetypes.

## Deployment

This application is packaged as two docker containers, one containing the Django web app, Gunicorn server and a lightweight database and the second containing the Nginx server. libations is deployed using Google Compute Engine and is accessible at http://libations.guru/. 

