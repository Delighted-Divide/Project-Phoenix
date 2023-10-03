from django.shortcuts import render

# Create your views here.


def dashboard(request):

    context = {
        'pname': "Dashboard",
        'user': request.user
    }
    return render(request, "dashboard.html", context)
