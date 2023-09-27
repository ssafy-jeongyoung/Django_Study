from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea())
    
class ArticleForm(forms.ModelForm):
    # model 등록
    class Meta:  # 메타 데이터
        model = Article
        fields = '__all__'
        
        # 특정 요소만 출력
        # fields = ('title', )
        
        # 제외
        # exclude=('title',)
