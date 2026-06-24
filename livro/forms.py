from django import forms  # type: ignore

from .models import Livros


class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = "__all__"

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields["usuario"].widget = forms.HiddenInput()
        self.fields["emprestado"].widget = forms.HiddenInput()
        self.fields["data_cadastro"].widget = forms.HiddenInput()


class CategoriaLivro(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    descricao = forms.CharField()

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields["descricao"].widget = forms.Textarea()
