from django.test import TestCase, Client
from django.test.client import Client
from Tetris.models import UserProfile,Leaderboard,Score
from django.contrib.auth.models import User

class UserProfileMethodTests(TestCase):

    def test_UserProfile_model(self):
                user = User(username="tester", password="none")
                user.save()
                user_profile = UserProfile(user=user, picture="profile_images/test.png", bio="test bio")
                user_profile.save()
                self.assertEquals(user_profile, UserProfile.objects.get(user=user))
                self.assertEqual((user_profile.user ==user), True)
                self.assertEqual((user_profile.picture == "profile_images/test.png"), True)
                self.assertEqual((user_profile.bio == "test bio"), True)


class LeaderboardMethodTests(TestCase):

    def test_Leaderboard_model(self):
                leaderboard = Leaderboard(seed="666", plays=3, challanges=2, likes=1)
                self.assertEqual((leaderboard.seed =="666"), True)
                self.assertEqual((leaderboard.plays ==3), True)
                self.assertEqual((leaderboard.challanges ==2), True)
                self.assertEqual((leaderboard.likes ==1), True)


class URLTests(TestCase):

    def test_about_url(self):
        c = Client()
        response = c.get('/#about/')
        response.content

    def test_edit_profile_url(self):
        c = Client()
        response = c.get('/edit_profile/')
        response.content

    def test_userpage_url(self):
        c = Client()
        response = c.get('/userpage/')
        response.content


    def test_leaderboard_url(self):
        c = Client()
        response = c.get('/leaderboard/')
        response.content

    def test_play_url(self):
        c = Client()
        response = c.get('/play/')
        response.content
