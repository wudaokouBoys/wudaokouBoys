from django import forms
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length = 50)
    file = forms.FileField(label = 'file')
    print(file)
    print(title)
    print(88)