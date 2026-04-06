from django.shortcuts import render


def tictactoe(request):
    return render(request, 'game/tictactoe.html')
