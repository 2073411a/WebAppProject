from django.shortcuts import render
from django.http import HttpResponse
from Tetris.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Tetris.forms import *

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

def about(request):
    return render(request, 'rango/about.html')

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

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def userpage(request):
    user = User.objects.get(username=request.user.username)
    context_dict = {}
    try:
        userprofile = UserProfile.objects.get(user=user)
    except:
        userprofile = None

    context_dict['user'] = user
    context_dict['userprofile'] = userprofile

    return render(request, 'Tetris/userpage.html', context_dict)

def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user
                try:
                    profile.picture = request.FILES['picture']
                except:
                    pass
                profile.save()
                return index(request)
    else:
        form = UserProfileForm(request.GET)
    return render(request, 'Tetris/edit_profile.html', {'form': form})


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
