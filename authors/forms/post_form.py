from django import forms
from recipes.models import Post, Speciality
from utils.utils_forms.django_forms import add_attr, ValidationError
from collections import defaultdict # permite que eu gere um valor padrao para qualquer campo
from utils.strings.strings import is_positive_number
class AuthorPostForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['speciality'].queryset = Speciality.objects.all() # aqui vou bsucar os meus campos todos das especialidades

        self._my_errors = defaultdict (list) # a chav padrao tem uma lista vazia por definicao porque s campos podem ter mais que um erro

        add_attr(self.fields.get('description'), 'class', 'span-2'),# tem que estar no css isto ocupa as 2 posicoes na lista do grid
        add_attr(self.fields.get('post_field'), 'class', 'span-2'),
        add_attr(self.fields.get('category'), 'class', 'span-2'),
        #add_attr(self.fields.get('cover'), 'class', 'span-2'),/ o widget faz exatamete isto !!
    
    class Meta:
        model = Post
        fields =['title','speciality','category','description', 'post_field' , 'cover']

        widgets={
             'cover': forms.FileInput(
                 attrs={
                     'class': 'span-2'
                 }
             ),
         }
        
    # aceder ao titulo e dar erros!!
    def clean(self,*args, **kwargs):
        super_clean= super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data # fico com os dados do formularios aqui guardados
        title = cleaned_data.get('title')# vou buscar o campo title
        description = cleaned_data.get('description')

        if len(title) < 5: # verifico o tamanho do titulo e < 5 
            self._my_errors['title'].append('Title must have at least 5 chars')
        
        if title == description:
            self._my_errors['title'].append('Cannot be equal to description')
            self._my_errors['description'].append('Cannot be equal to title')


        if self._my_errors:
            raise ValidationError(self._my_errors) # aqui da me os erros


        return super_clean
    
    def clean_description(self):
        field_name = 'description'
        field_value = self.cleaned_data.get(field_name)

        if not is_positive_number(field_value):
            self._my_errors[field_name].append('Must be a positive number or you cant use the signal - !')

        return field_value