from django.shortcuts import render

def index(request):
    #listings = listings.objects.order_by('-list_date').filter(is_publishde)
    context = {
        'title': "Ecommerce"

            }
    return render (request, 'pages/index.html', context)


