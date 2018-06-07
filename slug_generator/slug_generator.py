import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, random_digits_size=3, new_slug=None):
    """
        We assume the instance is a model with a title and a slug field where the slug will be created based on the title field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=random_digits_size)
        )
        return unique_slug_generator(instance, random_digits_size=random_digits_size, new_slug=new_slug)
    return slug
