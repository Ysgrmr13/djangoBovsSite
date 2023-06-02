import datetime
import logging
from blog.models import Post
from django.utils import timezone
import pytest

    
    
# далее разобраться что тестировать, а что нет. 
# Если то не сработало, добавьте так 
# @pytest.mark.django_db(transaction=True)


@pytest.mark.django_db
def test_title_create():
     article = Post.objects.create(title="article1")
     assert article.title == 'article1'

@pytest.mark.django_db
def test_content_create():
    content = Post.objects.create(content='This is a test content')
    assert content.content == 'This is a test content'

@pytest.mark.django_db
def test_date_created_create(): # Здесь мы используем функцию timezone.make_aware() для создания осознанного объекта datetime с учетом часового пояса Django, и затем сравниваем значения полей date_created.
    date_created = Post.objects.create(date_created=timezone.make_aware(datetime.datetime(2023, 5, 30)))
    assert date_created.date_created == timezone.make_aware(datetime.datetime(2023, 5, 30))

@pytest.mark.django_db
def test_date_updated_auto_now():
    # Создаем запись в базе данных
    post = Post.objects.create(title='Test Post', content='Lorem ipsum')

    # Получаем текущую дату и время
    current_datetime = timezone.now()

    # Модифицируем запись (поле date_updated автоматически обновится)
    post.content = 'Updated content'
    post.save()

    # Обновляем объект записи из базы данных
    post.refresh_from_db()

    # Проверяем, что поле date_updated содержит актуальную дату и время
    assert post.date_updated >= current_datetime
