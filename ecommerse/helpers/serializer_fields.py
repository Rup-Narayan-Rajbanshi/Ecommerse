from rest_framework import serializers
from rest_framework.fields import (
    get_attribute, is_simple_callable
)
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __


def file_representation(self, value):
    from chowk.settings import PROXY_URL

    if not value:
        return None

    use_url = getattr(self, 'use_url', True)
    if use_url:
        try:
            url = value.url
        except AttributeError:
            return None
        build_url = PROXY_URL + url
        # request = self.context.get('request', None)
        # if request is not None:
        #     build_url = request.build_absolute_uri(url)
        #     build_url = build_url.replace('192.168.88.15', 'demo.rosebayconsult.com')
        #     build_url = build_url.replace('127.0.0.1', 'demo.rosebayconsult.com')
        #     build_url = build_url.replace('localhost', 'demo.rosebayconsult.com')
        #     return build_url
        return build_url

    return value.name


class ImageFieldWithURL(serializers.ImageField):

    def to_internal_value(self, data):
        # import os
        # from project.settings import MEDIA_ROOT
        request = request_context(self)
        if isinstance(data, str):
            return data
        return super(ImageFieldWithURL, self).to_internal_value(data)

    def to_representation(self, value):
        value = file_representation(self, value)
        return value


class FRelatedField(serializers.PrimaryKeyRelatedField):
    default_error_messages = {
        'required': _('This field is required.'),
        'does_not_exist': _('Invalid idx "{pk_value}" - object does not exist.'),
        'incorrect_type': _('Incorrect type. Expected idx value, received {data_type}.'),
    }

    def get_attribute(self, instance):
        if self.use_pk_only_optimization() and self.source_attrs:
            # Optimized case, return a mock object only containing the pk attribute.
            try:
                instance = get_attribute(instance, self.source_attrs[:-1])
                value = instance.serializable_value(self.source_attrs[-1])
                if is_simple_callable(value):
                    # Handle edge case where the relationship `source` argument
                    # points to a `get_relationship()` method on the model
                    value = value().idx
                else:
                    value = getattr(instance, self.source_attrs[-1]).id
                return IDXOnlyObject(idx=value)
            except AttributeError:
                pass

    def to_representation(self, obj):
        return obj.idx

    def to_internal_value(self, data):
        try:
            return self.queryset.get(id=data)
        except ObjectDoesNotExist:
            self.fail('does_not_exist', pk_value=data)
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)