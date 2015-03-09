from django.shortcuts import render
from django.http import HttpResponse
#from Tetris.models import Page
#from Tetris.models import Category
#from Tetris.forms import CategoryForm
#from Tetris.forms import PageForm
#from Tetris.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    #TODO RETURN PAGE
    return HttpResponse("TEMP")

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
        while pointer >= 1000007:
            pointer -= 1000007
        pieces += line[pointer]
        pointer += frontno

    returnPieces = ""
    for p in pieces:
        returnPieces+=str(p)+","
    return HttpResponse(returnPieces[:-1])

def leaderboard(request, seed):
    return HttpResponse("TEMP")

def userpage(request, username):
    return HttpResponse("TEMP")

def challenge(reuest, seed, username):
    return HttpResponse(seed + ":" + username)

@login_required
def score(request, seed, score):
    return HttpResponse("TEMP")
