from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 카테고리
class Category(BaseModel):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '%s' % self.name


def main_img_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ' '.join(arr)
    extension = filename.split('.')[-1]
    return 'media/tickets/{}.{}'.format(pid, extension)

# 공연 태그정보
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.name


# 상품
class Show(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, db_index=True)
    price = models.PositiveIntegerField(default=0)
    short_desc = models.CharField(max_length=500)
    contents = RichTextUploadingField(config_name='default', blank=True, null=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, allow_unicode=True)
    display_available = models.BooleanField('제품 공개', default=True)
    order_available = models.BooleanField('주문 가능', default=True)
    total_seats = models.PositiveIntegerField(default=0, blank=True, null=True)
    tags = TaggableManager(blank=True)
    main_img = ProcessedImageField(upload_to = main_img_path,
                                   processors = [ResizeToFill(
                                       width=228, height=340, upscale=True)],
                                   format='JPEG',
                                   options={'quality':90},
                                   blank=True,
                                   null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'shows'