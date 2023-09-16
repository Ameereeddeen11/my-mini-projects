from django.core.exceptions import ValidationError
import magic
from django.utils.translation import gettext_lazy as _
from PIL import Image

def file_validators(image):
    accept = ['image/png', 'image/jpeg', 'image/jpg']
    file_type = magic.from_buffer(image.read(), mime=True)
    
    #if file_type not in accept:
    #    raise ValidationError("Unsupported file type")
    #else:        
    #    max_width = 600
    #    max_height = 600
#
    #    image = Image.open(image)
    #    width, height = image.size
    #    if width > max_width or height > max_height:
    #        raise ValidationError(f"Obrázek má příliš velké rozměry. Maximální rozměry jsou {max_width}x{max_height} px.")
    #    return image
    
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