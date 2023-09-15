from django.contrib import admin
# 명시적 상대경로 (.models)
from .models import Article

# 모델 클래스를 admin site에 등록
# 외우는 법 : admin site에 등록(register)한다
admin.site.register(Article)