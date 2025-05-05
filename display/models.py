from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Carousel(models.Model):
    title = RichTextField()
    description = RichTextField()
    image_content = RichTextUploadingField()

