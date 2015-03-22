from django.test import TestCase, Client
from django.test.client import Client
from Tetris.models import UserProfile,Leaderboard,Score
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from populate import populate
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


class ScoreMethodTests(TestCase):

    def test_Leaderboard_model(self):
                user = User(username="tester", password="none")
                leaderboard = Leaderboard(seed="666", plays=3, challanges=2, likes=1)
                score = Score(leaderboard=leaderboard, user=user, score=300)
                self.assertEqual((score.leaderboard ==leaderboard), True)
                self.assertEqual((score.user ==user), True)
                self.assertEqual((score.score ==300), True)

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

    def test_game_url(self):
        c = Client()
        response = c.get('/game/300')
        response.content

    def test_seeded_leaderboard_url(self):
        c = Client()
        response = c.get('/leaderboard/300')
        response.content

    def test_leaderboard_url(self):
        c = Client()
        response = c.get('/leaderboard/')
        response.content

    def test_play_url(self):
        c = Client()
        response = c.get('/play/')
        response.content

    def test_score_url(self):
        c = Client()
        response = c.get('/score/300')
        response.content

class IndexViewTests(TestCase):

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class LeaderboardViewTests(TestCase):

    def test_leaderboard_no_scores(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no scores present.")
        self.assertQuerysetEqual(response.context['scores'], [])


    def test_leaderboard_with_scores(self):
        user = User(username="tester", password="test")
        user.save()
        leaderboard = Leaderboard(seed="666", plays=3, challanges=2, likes=1)
        leaderboard.save()
        score = Score(leaderboard=leaderboard, user=user, score=300)
        score.save()
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        num_leaderboards = len(response.context['scores'])
        self.assertEqual(num_leaderboards, 1)

class PlayViewTests(TestCase):

    def test_play(self):
        response = self.client.get(reverse('play'))
        self.assertEqual(response.status_code, 200)


class AboutViewTests(TestCase):

    def test_about(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

class EditProfileViewTests(TestCase):

    def test_edit_profile(self):
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 302)

class UserpageViewTests(TestCase):

    def test_Userpage(self):
        response = self.client.get(reverse('userpage'))
        self.assertEqual(response.status_code, 302)



class PopulateTest(TestCase):

    def test_populate(self):
        populate()
        self.assertIsNotNone(User.objects.get(username="test0"))
        self.assertIsNotNone(Leaderboard.objects.get(seed="test0", plays=4, challanges=0))
        lead=Leaderboard.objects.get(seed="test0", plays=4, challanges=0)
        usr=User.objects.get(username="test0")
        self.assertIsNotNone(Score.objects.get(leaderboard=lead, user=usr, score=10))