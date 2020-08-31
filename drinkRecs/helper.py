import requests
import pandas as pd
import datetime
import json
import numpy as np
import os

apiKey = os.getenv('COCKTAILDB_API_KEY')

ingredient_request_url = "https://www.thecocktaildb.com/api/json/v2/"+str(apiKey)+"/list.php"
parameters={
    "i": "list"
}
#response = requests.get(ingredient_request_url, params=parameters)

#print(response.json())

search_request_url = "https://www.thecocktaildb.com/api/json/v2/"+str(apiKey)+"/filter.php"
lookup_request_url = "https://www.thecocktaildb.com/api/json/v2/"+str(apiKey)+"/lookup.php" 

other_url = "https://www.thecocktaildb.com/api/json/v2/"+str(apiKey)+"/filter.php?a=Alcoholic"
lookup_request_url = "https://www.thecocktaildb.com/api/json/v2/"+str(apiKey)+"/lookup.php"

df_dist=pd.read_csv("drinkRecs/df_distance.csv")
df_dist=df_dist.set_index("drinkId")

def find_distance(drink_id, df_distance):
    distances=[]
    matrix=df_distance.as_matrix()
    index=list(df_distance.index).index(drink_id)
    for i in range(0,len(df_distance)):
        distances.append([list(df_distance.index)[i],np.linalg.norm(matrix[index,:]-matrix[i,:])])
    df_distances = pd.DataFrame(distances)
    df_distances.columns=["id","dist"]
    df_distances=df_distances.sort_values(["dist"])
    return df_distances
        
def findTop5(df_distances):
    return df_distances['id'][1:6]
