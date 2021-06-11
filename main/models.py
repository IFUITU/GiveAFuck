from django.db import models
import os
from django.conf import settings
from datetime import datetime
from pathlib import Path
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    file_name = filename.split('.')[:1]
    folders = {'png':'img', 'jpeg':'img', 'svg':'img', 'jpg':'img', 'rar':'files','exe':'files', 'apk':'android', 'zip':'files','mp4':'video'}
    
    # print(file_name, ext)
    return "{}-{:%Y}/{:%Y-%m-%d-%H:%M}-{}.{}".format(
        folders.get(ext, 'media'), datetime.now(), datetime.now(), file_name,ext
    )


# class CustomManager(models.Manager):
#     def get_queryset(self):
#         return super(CustomManager, self).get_queryset().defer('platform',)

class Game(models.Model):
    bonus_active = True
    bonus_inactive = False

    title = models.CharField(max_length=200)
    bonus = models.BooleanField( choices=((bonus_active,'bonus'),(bonus_inactive,'Just Post')) , null=True, default=bonus_inactive, blank=True )
    desc = models.TextField(verbose_name='Description', max_length=1000)
    category = models.ManyToManyField('Category', blank=True, default=None ,related_name='category')
    platform = models.ForeignKey("Platform", on_delete=models.RESTRICT, default=None, null=True)
    count_dwnd = models.IntegerField(blank=True, default=16)
    likes = models.IntegerField(blank=True ,default=14)
    file = models.FileField(upload_to=get_upload_path, blank=True, null=True)
    title_img = models.ImageField(upload_to=get_upload_path, blank=True)
    # user = models.ForeignKey('user.User', )
    age_limit = models.SmallIntegerField(default=16)
    rated_user = models.IntegerField(blank=True, default=0)
    oponion = models.IntegerField(blank=True, default=0)
    stars = models.IntegerField(blank=True, default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    # if bonus: # crrectirovichka?
    video = models.FileField(upload_to=get_upload_path,blank=True, null=True, verbose_name='Video Stream')
  
    # objects = CustomManager()
    
    def __str__(self):
        return self.title

    @property #?????
    def image_url(self):
        if self.title_img:
            return os.path.join(settings.MEDIA_URL, str(self.title_img))
        return Path(settings.STATIC_URL).joinpath("img/rabbit.png")

    @property
    def ext(self):
        extension = self.video.name
        # print(extension,'/'*30)
        return extension

    
    @property
    def filesize(self): 
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext
    
    def save(self, **kwargs):
        print("SAVECALL".center(30))
        if not self.title_img.closed:
            img = Image.open(self.title_img)
            img.thumbnail((300, 300), Image.ANTIALIAS)
            tmp = BytesIO()
            img.save(tmp, 'png')
            self.title_img = File(tmp, '{}.png'.format(self.title))
          
        return super(Game, self).save(**kwargs)

    #if we created def(**args) how to call this method by sending arguments in template?

class Post_Img(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE, blank=True)
    img = models.ImageField(upload_to=get_upload_path)

    def save(self, **kwargs):
        
        if not self.img.closed:
            photo = Image.open(self.img)
            photo.thumbnail((300, 300), Image.ANTIALIAS)
            tmp = BytesIO()
            photo.save(tmp, 'png')
            self.img = File(tmp ,'t.png')
        return super().save(**kwargs)

class Category(models.Model):
    name_eng = models.CharField(max_length=50)

    def __str__(self):
        return self.name_eng
    
class Platform(models.Model):
    name_eng = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    def __str__(self):
        return self.name_eng