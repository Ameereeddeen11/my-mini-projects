import magic
from django.core.exceptions import ValidationError
from PIL import Image

def validate_file_type(image):
    mime = magic.from_buffer(image.read(), mime=True)
    if mime not in ['image/jpg', 'image/png']:
        raise ValidationError('Unsupported file type')
    
def validate_int(for_how_many_people):
    if for_how_many_people <= 0:
        raise ValidationError(("The reacipe must be for more than %(value) people"),
            params={"value": for_how_many_people},
        )

def validate_image_dimensions(image):
    max_width = 800
    max_height = 600

    image = Image.open(image)
    width, height = image.size
    if width > max_width or height > max_height:
        raise ValidationError(f"Obrázek má příliš velké rozměry. Maximální rozměry jsou {max_width}x{max_height} px.")
