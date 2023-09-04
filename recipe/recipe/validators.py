from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import magic
from django.utils.translation import gettext_lazy as _
from PIL import Image

ext_validator = FileExtensionValidator(['png', 'jpg'])

def file_validators(value):
    accept = ['image/png', 'image/jpeg']
    file_type = magic.from_buffer(value.read(1024), mime=True)
    
    if file_type not in accept:
        raise ValidationError("Unsupported file type")
        
def validate_image_dimensions(value):
    max_width = 800
    max_height = 600

    image = Image.open(value)
    width, height = image.size
    if width > max_width or height > max_height:
        raise ValidationError(f"Obrázek má příliš velké rozměry. Maximální rozměry jsou {max_width}x{max_height} px.")

def validate_int(value):
    if value <= 0:
        raise ValidationError(
            _("The reacipe must be for more than %(value) people"),
            params={"value": value},
        )