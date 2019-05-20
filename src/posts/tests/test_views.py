from django.core.urlresolvers import reverse
from django.test import TestCase
from posts.models import Post


class PostViewTestCase(TestCase):

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_detail_view(self):
        obj = self.create_post(title='Another Title')
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_update_view(self):
        obj = self.create_post(title='Another Title')
        edit_url = reverse('posts:update', kwargs={'slug': obj.slug})
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 404)
