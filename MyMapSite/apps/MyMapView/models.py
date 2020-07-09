import datetime

from django.db import models
from django.utils import timezone

class Showcode(models.Model):
    MyMapView_title = models.CharField('название статьи', max_length = 100)
    MyMapView_text = models.TextField('текст статьи')
    Pub_date = models.DateTimeField('дата публикации', default=timezone.now)

    def __str__(self):
        return self.MyMapView_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Showcode, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 300)
    pub_date = models.DateTimeField('дата публикации', default=timezone.now)

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(hours = 8))

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий к статье'
        verbose_name_plural = 'Комментарии к статье'

class Image(models.Model):
    img = models.TextField('ссылка на изображение')
    about_img = models.TextField('описание')
    where = models.CharField('координаты', max_length = 20)

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'

    def __str__(self):
        return self.where

class Imgcomment(models.Model):
    article = models.ForeignKey(Image, on_delete = models.CASCADE)
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 300)
    pub_date = models.DateTimeField('дата публикации', default=timezone.now)

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(hours = 8))

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий к скриншоту'
        verbose_name_plural = 'Комментарии к скриншоту'