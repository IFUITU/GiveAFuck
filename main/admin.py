from django.contrib import admin
from  .models import Game, Post_Img, Category, Platform
# Register your models here.

def is_bonus(modeAdmin, request, queryset):
    queryset.update(bonus=Game.bonus_active)
is_bonus.short_description = "BONUS"

def is_post(modelAdmin, request, queryset):
    queryset.update(bonus=Game.bonus_inactive)
is_post.short_description = 'Just POST'

class ImgInstatnceInine(admin.TabularInline):
    model = Post_Img

class GameAdmin(admin.ModelAdmin):
    inlines = [ImgInstatnceInine]
    actions = [is_bonus, is_post]
    list_display = ('title', 'platform', 'pub_date', 'bonus')
admin.site.register(Game,GameAdmin)

admin.site.register(Category)
admin.site.register(Platform)
