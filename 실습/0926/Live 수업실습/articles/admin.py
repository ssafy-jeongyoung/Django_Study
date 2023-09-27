from django.contrib import admin
from .models import Article
# 관리자 페이지에서 Article 보고싶다... 
admin.site.register(Article)