from django import forms
from recipes.models import Post
from utils.utils_forms.django_forms import add_attr

class AuthorPostForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        add_attr(self.fields.get('description'), 'class', 'span-2'),# tem que estar no css isto ocupa as 2 posicoes na lista do grid
        add_attr(self.fields.get('post_field'), 'class', 'span-2'),
        #add_attr(self.fields.get('cover'), 'class', 'span-2'),/ o widget faz exatamete isto !!
    
    class Meta:
        model = Post
        fields ='title', 'speciality','description', 'post_field' , 'cover'

        widgets={
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'speciality': forms.Select(
                choices=(
                    ('value', 'Anesthesiology'),
                    ('value', 'Allergy and Immunology'),
                    ('value', 'Cardiovascular Disease'),
                    ('value', 'Dermatology'),
                    ('value', 'Emergency Medicine'),
                    ('value', 'Family Medicine'),
                    ('value', 'Gastroenterology'),
                    ('value', 'Geriatrics'),
                    ('value', 'Hematology'),
                    ('value', 'Infectious Disease'),
                    ('value', 'Internal Medicine'),
                    ('value', 'Medical Genetics'),
                    ('value', 'Nephrology'),
                    ('value', 'Neurology'),
                    ('value', 'Nuclear Medicine'),
                    ('value', 'Obstetrics and Gynecology'),
                    ('value', 'Oncology'),
                    ('value', 'Ophthalmology'),
                    ('value', 'Orthopedic Surgery'),
                    ('value', 'Otolaryngology (ENT)'),
                    ('value', 'Pain Medicine'),
                    ('value', 'Pathology'),
                    ('value', 'Pediatrics'),
                    ('value', 'Physical Medicine and Rehabilitation'),
                    ('value', 'Plastic Surgery'),
                    ('value', 'Preventive Medicine'),
                    ('value', 'Psychiatry'),
                    ('value', 'Pulmonology'),
                    ('value', 'Radiology'),
                    ('value', 'Rheumatology'),
                    ('value', 'Sleep Medicine'),
                    ('value', 'Sports Medicine'),
                    ('value', 'Surgery'),
                    ('value', 'Thoracic Surgery'),
                    ('value', 'Urology'),
                    ('value', 'Vascular Surgery'),
                    ('value', 'Other'),
                ),
            ),
        }