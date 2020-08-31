from django.shortcuts import render, redirect
from drinkRecs.helper import *
import random
# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    #Get raw ingredients
    parameters={"i": "list"}
    response = requests.get(ingredient_request_url, params=parameters)
    output = response.json()['drinks']
    ingredients = [""]
    for item in output:
        ingredients.append(item['strIngredient1'].replace(" ", "_"))
    #Parse drink info from the dropdown post request
    try:
        drinks = request.session["drinks"]
    except KeyError:
        drinks=""
    try:
        for i, drink in enumerate(drinks):
            parameters = {"i": drink["idDrink"]
            }
            response = requests.get(lookup_request_url, params=parameters)
            drink_output = response['drinks'][0]
            drinks[i]["info"] = drink_output
    except:
        pass
    #Get the post info from the dropdowns
    try:
        primary = request.session["primary"]
    except KeyError:
        primary=""
    try:
        other = request.session["other"]
    except KeyError:
        other=""
    
    context={
        "ingredients":ingredients,
        "drinks": drinks,
        "primary": primary,
        "other":other,
    }
    return render(request, "index.html", context)

def find_cocktail(request):
    f = request.POST
    primary = f["primary"]
    other = f["other"]
    print("primary")
    print(primary)
    print("other")
    print(other)
    if other =="":
        string_param = primary
    else:
        string_param = primary+","+other
    parameters = {"i": string_param}    

    response = requests.get(search_request_url, params=parameters)
    output = response.json()['drinks']
    if output=="None Found":
        output = [{"strDrink": "None found :( Try something less wacky!",}]
    elif len(output)>5:
        output = random.sample(output,5)
    print(output)
    request.session.clear()
    request.session['drinks'] = output
    request.session["primary"] = primary
    request.session["other"] = other
    return redirect("/")

def show_cocktail(request, cocktail_id):
    parameters = {"i": str(cocktail_id)}
    response = requests.get(lookup_request_url, params=parameters)
    print(response.json())
    drink_output = response.json()['drinks'][0]
    full_ingredients = []
    for i in range(1,12):
        if (drink_output["strIngredient"+str(i)] is not None) and (drink_output["strMeasure"+str(i)] is not None):
            ingredient_str = drink_output["strMeasure"+str(i)]+" "+drink_output["strIngredient"+str(i)]
            full_ingredients.append(ingredient_str)
    try:
        similar_drinks = request.session["similar_drinks"]
    except KeyError:
        similar_drinks=""
    print(similar_drinks)
    context = {"drink": drink_output,
            "full_ingredients":full_ingredients,
            "similar_drinks":similar_drinks}
    return render(request, "cocktail.html", context)

def find_similar(request,cocktail_id):
    df_distances = find_distance(int(cocktail_id),df_dist)
    close_cocktail_ids = findTop5(df_distances)
    print(close_cocktail_ids)
    output=[]
    for id in close_cocktail_ids:
        parameters = {"i": str(id)}
        response = requests.get(lookup_request_url, params=parameters)
        drink_output = response.json()['drinks'][0]
        output.append(drink_output)
    
    request.session.clear()
    print("similar")
    print(output)
    request.session['similar_drinks'] = output
    
    return redirect("/cocktail/"+str(cocktail_id))