import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebAppProject.settings')

import django

django.setup()

import registration.backends.default as reg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from Tetris.models import UserProfile,Leaderboard,Score

def populate():
    test = add_user_test("test")
    userTest0 = add_user("test0")
    userTest1 = add_user("test1")
    userTest2 = add_user("test2")
    userTest3 = add_user("test3")
    userTest4 = add_user("test4")
    leaderTest0 = add_leaderboard("test0",4,0)
    leaderTest1 = add_leaderboard("test1",5,0)
    leaderTest2 = add_leaderboard("test2",25,0)
    leaderTest3 = add_leaderboard("test3",3,0)
    leaderTest4 = add_leaderboard("test4",15,0)
    leaderboards = [leaderTest0,leaderTest1,leaderTest2,leaderTest3,leaderTest4]
    users = [userTest0,userTest1,userTest2,userTest3,userTest4]
    #LeaderBoard 0
    add_score(leaderTest0,userTest0,10)
    add_score(leaderTest0,userTest1,15)
    add_score(leaderTest0,userTest2,20)
    add_score(leaderTest0,userTest3,25)
    #Leaderboard 1
    for u in users:
        add_score(leaderTest1,u,20)
    #Leaderboard 2
    for u in range(25):
        add_score(leaderTest2,users[u%5],u)
    #Leaderboard 3
    for u in range(3):
        add_score(leaderTest3,userTest0,10)
    #Leaderboard 4
    for u in range(15):
        add_score(leaderTest4,users[u%5],u*u)

def add_userProfile(b,username):
    u = add_user(username)
    return UserProfile.objects.get_or_create(user = u, bio = b)

def add_user(username):
    if(authenticate(username = username,password = username + "pass") != None):
        return authenticate(username = username,password = username + "pass")
    User.objects.create_user(username, username + "@test.com", username + "pass")
    return authenticate(username = username,password = username + "pass")

def add_user_test(n):
    if(authenticate(username = n, password = n) != None):
        return authenticate(username = n, passwprd = n)
    User.objects.create_user(username = n, password = n)
    return authenticate(username = n, password = n)

def add_leaderboard(s,p,c):
    return Leaderboard.objects.get_or_create(seed = s, plays = p, challanges = c, likes = 0)[0]

def add_score(l,u,s):
    return Score.objects.get_or_create(leaderboard=l,user=u,score=s)

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
