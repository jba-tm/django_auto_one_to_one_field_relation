# django_auto_one_to_one_field_relation

Auto create one to one relation object instance

Example: 

user -> cart 

By default, related field 


    ...
    class Cart(models.Model):
         owner = AutoOneToOneField(settings.AUTH_USER_MODEL,
                                  related_name='cart', on_delete=models.CASCADE,
                                  null=True,
                                  blank=True,
                                  verbose_name=settings.OWNER_FIELD_NAME)

    ...