from django.core.exceptions import ValidationError
import magic
from django.utils.translation import gettext_lazy as _
from PIL import Image

def file_validators(image):
    accept = ['image/png', 'image/jpeg', 'image/jpg']
    file_type = magic.from_buffer(image.read(), mime=True)
    
    if file_type not in accept:
        raise ValidationError("Unsupported file type")
    return image
    
def validate_image_dimensions(image):
    pass    

def validate_file_size(image):
    filesize = image.size

    if filesize > 2 * 1024 * 1024:
        raise ValidationError("Size of image can't be more then 2Mb")
    return image

def validate_int(value):
    if value <= 0:
        raise ValidationError(
            _("The reacipe must be for more than %(value) people"),
            params={"value": value},
        )