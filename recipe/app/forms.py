from django import forms 
from .models import *
from recipe.validators import ext_validator, file_validators, validate_int
#from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
import os 

class RecipeForm(forms.ModelForm):
    for_how_many_people = forms.IntegerField(validators=[validate_int])
    class Meta:
        model = Recipes
        fields = [
            "title",
            "discription",
            "ingredient",
            "instructions",
            "existing_category",
            "own_category",
            "takes_time",
            "for_how_many_people",
            "link_to_youtube"
        ]
class CategoryForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Category
        fields = ["name"]

def validate(value):
    ext = os.path.splitext(value.name)[1]
    valid = ['.png', '.jpg']
    if not ext.lower() in valid:
        raise ValidationError('Unsuposted file type')

class ImageForm(forms.ModelForm):
    image = forms.FileField(
        widget = forms.FileInput(attrs={'class':'form-control-file', 'accept':'.jpg, .png'}),
        validators=[validate]
    )
    
    required = False
    class Meta:
        model = ImagesRecipesOwner
        fields = [
            "image",
        ]
        

    #def clean(self, *args, **kwargs):
    #    image = self.cleaned_data.get("image")
    #    filetype = magic.from_buffer(image.read(1024), mime=True)
    #    if not "image/jpg" in filetype:
    #        raise ValidationError(_('Unsuposted file type'))
    #    return image
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
            "rating"
        ]