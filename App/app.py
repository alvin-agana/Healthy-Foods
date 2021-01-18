from flask import Flask, redirect, url_for, render_template, request
import requests

app = Flask(__name__)
#arr = [1,2,3,4,5,6,7]

#API CALLS
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
headers = {
    'x-rapidapi-key': "afa2ad2932msh58fc2754c6724d0p152481jsn59c06d6a4090",
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}


@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('home.html')

"""
@app.route('/recipe', methods=['GET','POST'])
def recipe():
    #zipcode = request.form['zipcode']
    zipcode = "94587"
    food = "pasta"
    diet = "vegetarian"

    querystring = {"query":food,"diet":diet,"number":"10","type":"main course"}

    r = requests.get('https://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=' + zipcode)
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    foodinfo = response.json()
    marketinfo = r.json()
    return render_template('recipe.html', z=marketinfo['results'], f=foodinfo['results'], enumerate=enumerate)
"""


@app.route('/recipe', methods=['GET','POST'])
def recipe():
    # spoonacular api call
    ingredient = request.form['ingredient']
    diet = request.form['diet']
    querystring = {"query":ingredient,"diet":diet,"number":"10","type":"main course"}
    foodresponse = requests.request("GET", url, headers=headers, params=querystring)
    foodinfo = foodresponse.json()

    # farmers market api call
    zipcode = request.form['zipcode']
    r = requests.get('https://search.ams.usda.gov/farmersmarkets/v1/data.svc/zipSearch?zip=' + zipcode)
    marketinfo = r.json()
    return render_template('recipe.html', ingredient=ingredient, z=marketinfo['results'], f=foodinfo['results'], b=foodinfo['baseUri'], enumerate=enumerate)



if __name__ == "__main__":
    app.run(debug=True)
