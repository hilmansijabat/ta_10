from django.shortcuts import render


# Create your views here.

# TODO: Create view for index
def index(request):
    context = {
        "name": "Andree Panjaitan",
    }
    return render(request, 'scanning/index.html', context)


def scanning_request(request):
    context = {}
    return render(request, 'scanning/scanning.html', context)
