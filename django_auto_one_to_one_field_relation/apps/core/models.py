from django.db.models.fields.related import (
    OneToOneField, ReverseOneToOneDescriptor,
)


class AutoSingleRelatedObjectDescriptor(ReverseOneToOneDescriptor):
    """
    Auto create non exist relation
    """
    def __get__(self, instance, type=None):
        try:
            return super(AutoSingleRelatedObjectDescriptor, self).__get__(instance, type)
        except self.RelatedObjectDoesNotExist:
            kwargs = {
                self.related.field.name: instance,
            }
            rel_obj = self.related.related_model.objects.create(**kwargs)
            setattr(instance, self.related.get_cache_name(), rel_obj)
            return rel_obj


class AutoOneToOneField(OneToOneField):
    related_accessor_class = AutoSingleRelatedObjectDescriptor
