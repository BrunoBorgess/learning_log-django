from django.shortcuts import render


def index(request):
    """ Página principal Learning_Log """
    return render(request, 'learning_logs/index.html')