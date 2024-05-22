from io import BytesIO
from PIL import Image
from django.core.validators import RegexValidator
from django.core.files import File
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_filters import rest_framework as filters

GROUPS_OPTIONS = [
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
    ('patreon-on-site', 'Patreon (on-site)'),
    ('patreon-remote', 'Patreon (remote)'),
]

TYPE_OPTIONS = [
    ('book', 'Book'),
    ('article', 'Article'),
    ('document', 'Document'),
    ('audiobook', 'Audiobook'),
    ('audio', 'Audio'),
    ('video', 'Video'),
    ('podcast', 'Podcast'),
]

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True )
    slug = models.SlugField()

    class Meta:
        ordering = (['name'])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Item(models.Model):
    user_groups = models.CharField(max_length=20, choices=GROUPS_OPTIONS)
    type = models.CharField(max_length=20, choices=TYPE_OPTIONS, default='book')
    isbn = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^.{13}$', 'ISBN must be exactly 13 characters')],
        unique=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    is_external = models.BooleanField(default=False, blank=True)
    file_url =  models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    slug = models.SlugField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = (['-date_added'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(500, 500)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def get_file(self):
        if self.file:
            return 'http://127.0.0.1:8000' + self.file.url
        return ''

class ItemFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="publication_date", lookup_expr='gte')
    to_date = filters.DateFilter(field_name="publication_date", lookup_expr='lte')
    type = filters.MultipleChoiceFilter(field_name="type", choices=TYPE_OPTIONS)
    # author = filters.MultipleChoiceFilter(field_name="author", choices=get_authors())
    # publisher = filters.MultipleChoiceFilter(field_name="publisher", choices=get_publishers())

    class Meta:
        model = Item
        fields = ['from_date', 'to_date', 'type']

@receiver(pre_save, sender=Item)
def save_profile(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = "-".join(instance.title.lower().split())