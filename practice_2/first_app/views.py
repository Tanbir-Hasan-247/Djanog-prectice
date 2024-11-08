from django.shortcuts import render

# Create your views here.
def page(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "desciption": "A popular Canadian treat, BeaverTails are fried dough pastries often topped with a variety of sweet options, from cinnamon sugar to chocolate."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "desciption": "Perfect for a hearty breakfast, these potatoes are seasoned and cooked to a crispy finish, often served alongside eggs and bacon."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "desciption":"A classic dessert, butter tarts are filled with a rich, buttery, and sugary filling in a flaky pastry crust."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "desciption":"Montreal's signature smoked meat, similar to pastrami, is served on rye bread with mustard for a traditional deli experience."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "desciption":"A layered dessert with a crumbly base, custard-flavored middle layer, and a chocolate topping, originally from Nanaimo, British Columbia."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "desciption": "Similar to shepherd's pie, this dish is made with layers of ground meat, corn, and mashed potatoes."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "desciption": "A classic Quebecois dessert made with cake batter and a hot caramel sauce that soaks into the cake as it bakes."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "desciption": "Perhaps Canada's most famous dish, poutine consists of French fries topped with cheese curds and smothered in gravy."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "desciption":"A traditional Acadian dish made from grated potatoes and meat, often chicken or pork, baked to a crispy golden finish."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "desciption": "A comforting soup made with split peas, often flavored with ham or bacon, popular in Quebec during the colder months."
        }
    ]
    return render(request,'index.html', {'meals' : meals})