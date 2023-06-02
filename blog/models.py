from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


def slugify(s):
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))


class Post(models.Model):
    """
    class - значит поддерживает методы.
    модель содержит поля.
    Поля имеют настройки поведения.
    улучшения:
    добавить tags, slug
    добавить в админку настроек
    добавить db_index
    лайки, сохранение лайков
    """

    # мета опции
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'

    # поля модели # настройки полей
    title = models.CharField(max_length=200,
                             help_text="не более 200 символов",
                             db_index=True, verbose_name='Название')
    # content = models.TextField(max_length=5000, blank=True, null=True, help_text="не более 5000 символов")
    content = RichTextField(blank=True, null=True, help_text="не более 5000 символов", max_length=5000, verbose_name='Содержимое')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=50)
    likes_post = models.ManyToManyField(User, related_name='post_likes', blank=True, verbose_name='Лайки')
    
    saves_posts = models.ManyToManyField(User, related_name="blog_posts_save", blank=True, verbose_name='Сохранённые посты пользователя')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def total_likes_post(self):
        return self.likes_post.count()

    def total_saves_posts(self):
        return self.saves_posts.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug, 'pk': self.pk})
    # методы модели

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def prepopulated_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)