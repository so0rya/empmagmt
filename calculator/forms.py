from django import forms

class OperationForm(forms.Form):
    num1=forms.IntegerField(label="Number 1")
    num2=forms.IntegerField(label="Number 2")
    def clean(self):
        # super().clean()
        cleaned_data=super().clean()
        n1=cleaned_data.get("num1")
        n2=cleaned_data.get("num2")
        if n1<0:
            msg="Number Invalid"
            self.add_error("num1",msg)
        if n2<0:
            msg="Number Invalid"
            self.add_error("num2",msg)