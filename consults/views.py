from django.shortcuts import render

def consults_view(request):
    return render(request, 'consults_view.html')
