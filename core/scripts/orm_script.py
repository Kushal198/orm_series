from django.db import connection
from django.db.models.functions import Lower
from core.models import Rating, Restaurant, Sale


def run():
    # restaurant = Restaurant.objects.filter(name='Pizzeria 1')
    # print(restaurant)
    # print(restaurant.get())
    chinese = Restaurant.TypeChoices.CHINESE
    italian = Restaurant.TypeChoices.ITALIAN
    mexican = Restaurant.TypeChoices.MEXICAN
    # restaurants = Restaurant.objects.filter(restaurant_type=chinese, name__startswith='C')
    # print(restaurants)
    # restaurants = Restaurant.objects.filter(restaurant_type__in=[chinese, italian, mexican])
    # restaurants = Restaurant.objects.exclude(restaurant_type=chinese)
    # restaurants = Restaurant.objects.filter(name__lt='E')
    # # restaurants = Restaurant.objects.filter(longitude__gt=0)
    # sale = Sale.objects.filter(income__range=(50,60))
    # restaurants = Restaurant.objects.order_by('name').reverse()
    # restaurants = Restaurant.objects.order_by(Lower('name')).reverse()
    # sale = Sale.objects.order_by('-datetime')
    # restaurants = Restaurant.objects.order_by('date_opened')[:5]
    # restaurants = Restaurant.objects.order_by('date_opened')[2:5] #limit 3 offset 2
    # restaurants = Restaurant.objects.earliest('date_opened')
    # restaurants = Restaurant.objects.latest()
    ratings = Rating.objects.filter(restaurant__name__startswith='C')
    sales = Sale.objects.filter(restaurant__restaurant_type=chinese)
    print(sales)
    print(connection.queries)