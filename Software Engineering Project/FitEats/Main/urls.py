from django.urls import path,include
from . import views

app_name = 'Main'
urlpatterns = [
    path('',views.Register,name="Register"),
    path('Ingredients/',views.Ingredients,name="IngredientsUrl"),
    path('Profile/',views.Profile,name="ProfileUrl"),
    path('Login/',views.Login,name="LoginUrl"),
    path('Register/',views.Register,name="RegisterUrl"),
    path('Logout/',views.Logout,name="LogoutUrl"),
    path('Recipes/',views.Recipes,name="RecipesUrl"),
    path('FullRecipe/',views.FullRecipe,name="FullRecipeUrl"),
]