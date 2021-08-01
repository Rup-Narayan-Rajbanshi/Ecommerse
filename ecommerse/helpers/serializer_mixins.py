
class CustomValidationMessageForSerializerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].error_messages['required'] = "{} is required.".format(
                    field.replace('_', ' ').capitalize())
