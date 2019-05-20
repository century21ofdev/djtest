from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from posts.models import Post
from posts.views import post_update, post_create

User = get_user_model()


class PostViewAdvancedTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='abc123test123',
            email='abc123test123@gmail.com',
            password='pwtest123#$$$',
            is_staff=True,
            is_superuser=True,
        )

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    # def test_user_auth(self):
    #     obj = self.create_post(title='Another new title post')
    #     edit_url = reverse('posts:update', kwargs={'slug': obj.slug})
    #     request = self.factory.get(edit_url)
    #     request_user = self.user
    #     response = post_update(request, slug=obj.slug)
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_user_post(self):
    #     request = self.factory.post("/posts/create/")
    #     request_user = self.user
    #     response = post_create(request)
    #     self.assertEqual(response.status_code, 200)
