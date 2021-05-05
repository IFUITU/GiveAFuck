from django.core.management import BaseCommand
from main.models import Game,Post_Img
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        obj = Game.objects.all()
        plt = Post_Img.objects.all()
        plt.delete()
        obj.delete()
        date = datetime.now() #- timedelta(days=30)
        print('All Games deleted ')
