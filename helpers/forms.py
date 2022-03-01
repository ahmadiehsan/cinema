from django.forms.widgets import Input


# TODO (ehsan) is it required?
class DateInput(Input):
    input_type = 'date'
