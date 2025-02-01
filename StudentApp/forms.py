from django import forms
from .models import Students

class StudentsInfo(forms.ModelForm):
    name = forms.CharField(max_length=50,label="名前",initial="サイチゲン")
    age = forms.IntegerField(label="年齢",initial=29)
    grade = forms.IntegerField(label="学年",initial=3)
    picture = forms.FileField(label="写真",required=False)
    
    class Meta:
        model = Students
        fields = "__all__"
        
# 編集フォーム
class StudentUpdateForm(forms.Form):
    name = forms.CharField(max_length=50,label="名前",initial="サイチゲン")
    age = forms.IntegerField(label="年齢",initial=29)
    grade = forms.IntegerField(label="学年",initial=3)
    picture = forms.FileField(label="写真",required=False)
    
    class Meta:
        model = Students
        fields = "__all__"

# 削除フォーム
class StudentDeleteForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput) #画面に表示しないように