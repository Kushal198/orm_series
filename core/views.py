from django.db.models import Prefetch, Sum
from django.shortcuts import render

from core.models import Restaurant, Rating, Sale
from django.utils import timezone

# Create your views here.
def index(request):
    #Get all 5 star ratings, fetch all the sales for restaurant with 5-star rating
    month_ago = timezone.now() - timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gt=month_ago)
    )
    # restaurants = Restaurant.objects.prefetch_related('ratings', 'sales') \
    #     .filter(ratings__rating=5) \
    #         .annotate(total=Sum('sales__income'))

    restaurants = Restaurant.objects.prefetch_related('ratings', monthly_sales) \
        .filter(ratings__rating=5) 
    restaurants = restaurants.annotate(total=Sum('sales__income'))

    # restaurants = Restaurant.objects.filter(name__istartswith='c').prefetch_related('ratings', 'sales')
    ratings = Rating.objects.only('rating', 'restaurant__name').select_related('restaurant')
    context = {"restaurants":restaurants, "ratings":ratings}
    print([r.total for r in restaurants])
    return render(request, 'index.html', context)