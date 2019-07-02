from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from stdnum import isbn


def ISBNValidator(raw_isbn):
    isbn_to_check = raw_isbn.replace('-', '').replace(' ', '')

    if len(isbn_to_check) != 10 and len(isbn_to_check) != 13:
        raise ValidationError(_(u'Invalid ISBN: Wrong length'))

    if not isbn.is_valid(isbn_to_check):
        raise ValidationError(_(u'Invalid ISBN: Failed checksum'))

    if isbn_to_check != isbn_to_check.upper():
        raise ValidationError(_(u'Invalid ISBN: Only upper case allowed'))

    return True
