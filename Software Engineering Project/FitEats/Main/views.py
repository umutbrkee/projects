from django.http import HttpResponse
from django.shortcuts import render,redirect
from . forms import RegisterForm, LoginForm
from.models import CustomUser
from django.contrib.auth import login,authenticate,logout
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponseNotFound
import json
import random
from django.contrib.auth.decorators import login_required



# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Do any additional processing of form data here
            user.save()
            
            return redirect("Main:LoginUrl")

    else:
        form = RegisterForm()
    return render(request, 'Register/Register.html', {'form': form})
    
def Login(request):
    if request.user.is_authenticated:
        return HttpResponseNotFound("Sayfa bulunamadı.")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("Main:ProfileUrl")


            else:
                # Şifre yanlış, hata mesajı göster
                    form.add_error(None, "Şifre yanlış")
                    print(password)
                    
            
    else:
        form = LoginForm()
    return render(request, 'Login/Login.html', {'form': form})


@login_required
def Logout(request):
    logout(request)
    return redirect('Main:LoginUrl') 




def Ingredients(request):
    if request.method == 'POST':

        ingredientName = request.POST["ingredientName"]
        ingredientName = ingredientName.split(" ")

        context = {
                'ingredientName' : ingredientName[-1]
                }

        return render(request,"Ingredients/Ingredients.html", context)
    return render(request,"Ingredients/Ingredients.html")

@login_required
def Profile(request):
    user_id = request.session.get('user_id', None)

    return render(request, 'Profile/Profile.html')
    
   
def Recipes(request):    

    with open('Main/recipies.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    
    recipes = data['Recipe']
    recipes = list(recipes.values())

    ingredients = data['Ingredient']
    ingredients = list(ingredients.values())
    ingredientsList = []
    for i in range(len(ingredients)):
        ingredientsList.append(ingredients[i]['Turkish Name'])
    ingredientsList.sort()
    ingredientsList = ingredientsList[18:]
    

    if 'submit-form1' in request.POST:
            ingredientsNames = request.POST["searchIngredients"]

            ingredientsNames = ingredientsNames.split(', ')

            print(ingredientsNames)
            print(len(ingredientsNames)-1)
            listRecipe = []

            for i in range(len(recipes)-1):
                for j in range(len(ingredientsNames)):
                    if (recipes[i]['IngridientNames'].find(ingredientsNames[j]) != -1) and (j == len(ingredientsNames)-1):
                        listRecipe.append(recipes[i])
                    elif recipes[i]['IngridientNames'].find(ingredientsNames[j]) != -1:
                        print("asdsdasd")
                    else:
                        break
                    

            for i in range(len(listRecipe)):
                temp = listRecipe[i]['PrepDetails'].split(";")
                listRecipe[i]['People'] = temp[0]
                listRecipe[i]['Time'] = temp[1]

            context = {
                'recipies' : listRecipe,
                'ingredients' : ingredientsList
                }

            return render(request,"Recipes/Recipes.html", context)
    
    elif 'submit-form2' in request.POST:
            recipeCategory = request.POST["searchCategory"]
        
            listRecipe = []

            for i in range(len(recipes)-1):
                if recipes[i]['MainCategory'].find(recipeCategory) != -1:
                    listRecipe.append(recipes[i])

            for i in range(len(listRecipe)):
                temp = listRecipe[i]['PrepDetails'].split(";")
                listRecipe[i]['People'] = temp[0]
                listRecipe[i]['Time'] = temp[1]

            context = {
                'recipies' : listRecipe,
                'ingredients' : ingredientsList
                }

            return render(request,"Recipes/Recipes.html", context)

    elif request.user.is_authenticated:

            ingredients = data['Ingredient']
            ingredients = list(ingredients.values())

            # tatlılar silinecek

            listRecipe = []

            kalori = request.user.tdee/3
            print(kalori)
            while 300 < kalori:
                temp = random.choice(recipes)
            
                ingredientNames = temp['IngridientNames'].split(";")
                ingredientNames.pop()
                

                value = float(0)

                for i in range(len(ingredientNames)-1):
                    for j in range(len(ingredients)-1):
                        if ingredients[j]['Turkish Name'] == ingredientNames[i]:
                            value += float(ingredients[j]['Calorie'])
                            break
                
                recipePorsion = temp['PrepDetails'].split(' ')

                if (value/(float(recipePorsion[0])) < 600) and temp['MainCategory'] != 'Tatlı':
                    listRecipe.append(temp)
                    kalori -= value/(float(recipePorsion[0]))
                    print(value/(float(recipePorsion[0])))
                else:
                    continue
            
            for i in range(len(listRecipe)):
                temp = listRecipe[i]['PrepDetails'].split(";")
                listRecipe[i]['People'] = temp[0]
                listRecipe[i]['Time'] = temp[1]
             
            context = {
               'recipies' : listRecipe,
                'ingredients' : ingredientsList
                }

            return render(request,"Recipes/Recipes.html", context)
        
    else:
        recipes = data['Recipe']

        randomRecipes = []

        for i in range(6):
            randomRecipes.append(random.choice(list(recipes.values())))
            
            temp = randomRecipes[i]['PrepDetails'].split(";")
            randomRecipes[i]['People'] = temp[0]
            randomRecipes[i]['Time'] = temp[1]

        
        print("bb")
        context = {
            'recipies' : randomRecipes,
            'ingredients' : ingredientsList
            }
        
        return render(request,"Recipes/Recipes.html", context)

def FullRecipe(request):
    if request.method == 'POST':
        recipeName = request.POST["name"]
        recipeIngridients = request.POST["ingridients"]
        recipeDetails = request.POST["details"]
        recipeImage = request.POST["image"]

        recipeIngridients = recipeIngridients.split("●")
        recipeIngridients.pop(0)

        recipeDetails = recipeDetails.split(".) ")
        recipeDetails.pop(0)

        for i in range(len(recipeDetails)-1):
            recipeDetails[i] = recipeDetails[i][:-2]

        context = {
            'recipeName' : recipeName,
            'recipeIngridients' : recipeIngridients,
            'recipeDetails' : recipeDetails,
            'recipeImage' : recipeImage,
            }

        return render(request,"FullRecipe/FullRecipe.html", context)
