from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Here we define a basic view response, just return text Hello World
def home(request):

    all_boards = Board.objects.all()
    # board_names = list()

    # for board in all_boards:
    #     board_names.append(board.name)

    # response_html = '<br>'.join(board_names)

    # return HttpResponse(response_html)

    # Use DJango template that we defined in home.html to render request
    return render(request, 'home.html', {'boards': all_boards})
