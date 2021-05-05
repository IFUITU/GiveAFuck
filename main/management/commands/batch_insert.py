from  main.models import Game, Category
from django.core.management import BaseCommand
from datetime import datetime
from itertools import islice

gow_desc = "You know abut this game you can play only on PSP!But Now it is available for  Mobile! via PPSSPP.apk just download and relax!"
ppsspp_desc = 'With this apk you can play PSP 1-2-3 games on your mobile Phone if your phone  RAM is upper than 3GB!'
rar_desc = ''
class Command(BaseCommand):
    def handle(self, *args ,**kwargs):
        batch_size = None
        objs = (
            Game(title='PPSSPP Gold', desc=ppsspp_desc, bonus=False,platform_id=1,file='', count_dwnd=0, likes=4, age_limit=12,rated_user=0,oponion=0,stars=0,
            pub_date=datetime.now()),
            Game(title="God of War", bonus=False, desc=gow_desc,platform_id=1,file='', count_dwnd=0,likes=4, age_limit=12,rated_user=0,oponion=0,stars=0,
            pub_date=datetime.now())
        )
        
        batch = list(islice(objs, batch_size)) 
        Game.objects.bulk_create(batch, batch_size)
# class Command(BaseCommand):

#     def handle(self, *args, **options):
#         batch_size = 100
#         objs = (Category(name_eng='Test %s' % i) for i in range(10))
#         while True:
#             batch = list(islice(objs, batch_size))
#             if not batch:
#                 break
#             Category.objects.bulk_create(batch, batch_size)