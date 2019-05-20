from django.test import TestCase
from django.utils.text import slugify
from django.utils import timezone
from posts.models import Post
from posts.forms import PostForm


class PostFormTestCase(TestCase):

    def test_valid_form(self):
        title = 'A new title'
        slug = 'some-prob-unique-slug-by-this-test-abc-123'
        obj = Post.objects.create(title=title, slug=slug, publish=timezone.now(), content='Stuff')
        data = {'title': obj.title, 'slug': obj.slug, 'publish': obj.publish, 'content': 'Stuff'}
        form = PostForm(data=data)  # PostForm(request.POST)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertNotEqual(form.cleaned_data.get('content'), 'Another Item')
