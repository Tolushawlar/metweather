from django.shortcuts import render

def index(requests):
    return render(requests, "MainApp/index.html")
