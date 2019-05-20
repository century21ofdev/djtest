from django.test import TestCase
from django.utils.text import slugify
# Create your tests here.
from posts.models import Post


class PostModelTestCase(TestCase):
    def setUp(self) -> None:
        Post.objects.create(title='A new title', slug='some-prob-unique-slug-by-this-test-abc-123')

    def create_post(self, title='This title'):
        return Post.objects.create(title=title)

    def test_post_title(self):
        obj = Post.objects.get(slug='some-prob-unique-slug-by-this-test-abc-123')
        self.assertEqual(obj.title, 'A new title')
        self.assertTrue(obj.content == "")  # maybe i want to change

    def test_post_slug(self):
        # generating title
        title1 = 'another title abc'
        title2 = 'another title abc'
        slug1 = slugify(title1)
        slug2 = slugify(title2)
        obj1 = self.create_post(title=title1)
        obj2 = self.create_post(title=title2)
        self.assertEqual(obj1.slug, slug1)
        self.assertNotEqual(obj2.slug, slug2)

    def test_post_qs(self):
        title1 = 'another title abc'
        obj1 = self.create_post(title=title1)
        qs = Post.objects.filter(title=title1)
        self.assertTrue(qs.count(), 3)
        qs2 = Post.objects.filter(slug=obj1.slug)
        self.assertEqual(qs2.count(), 1) # it should be only one
