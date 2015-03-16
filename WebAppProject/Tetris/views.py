from django.shortcuts import render
from django.http import HttpResponse
from Tetris.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    #TODO RETURN PAGE
    return render(request, 'Tetris/index.html')
def play(request):
    #TODO RETURN PAGE
    return render(request, 'Tetris/play.html')
def game(request, seed):
    # IMPORTANT #
    # NUMBER BELLOW HOW DEEP TO GO #
    # EDIT FOR BALANCING #
    nopiecestotake = 69
    #-----------------#
    f = file("piecelist.txt")
    line = f.readline()
    f.close()
    pieces = ""
    frontno = 1
    #-----------------#
	#Reading the randomised pieces list from the file.
    f = file("piecelist.txt")
    line = f.readline()
    f.close()

    # Make it MUCH easier to compute, might change later if we come up with a more effecit calc
    if len(seed) > 13:
        seed = seed[:13]
    for i in seed:
        frontno *= ord(i)
        while frontno >= 1000007:
            print "OverFlow"
            frontno -= 1000007
    pointer = frontno

    while len(pieces) < nopiecestotake:
        if pointer >= 1000007:
            pointer = pointer%1000007
        pieces += line[pointer]
        pointer += frontno

    returnPieces = ""
    for p in pieces:
        returnPieces+=str(p)+","
    return HttpResponse(returnPieces[:-1])

def leaderboard(request, seed):
    context_dict = {}
    try:
        leaderboard = Leaderboard.objects.get(seed=seed)
        scores = Score.objects.filter(leaderboard = leaderboard).order_by('-score')
        context_dict['scores'] = scores
        context_dict['leaderboard'] = leaderboard
    except leaderboard.DoesNotExist:
        pass
    return HttpResponse("TEMP")

def userpage(request, username):
    return HttpResponse("TEMP")


def challenge(request, seed, username):
    #Get's best score from user
    leaderboard = Leaderboard.objects.get(seed=seed)
    user = UserProfile.objects.get(user=username)
    bestScore = Score.objects.filter(leaderboard=leaderboard).filter(user=user).order_by('-score')[0]
    return HttpResponse(seed + ":" + username)

@login_required
def score(request, seed, score, username):
    l = Leaderboard.objects.get(seed=seed)
    u = UserProfile.objects.get(user=username)
    s = Score.objects.get_or_create(leaderboard = l,user = u, score = int(score))
    return s
