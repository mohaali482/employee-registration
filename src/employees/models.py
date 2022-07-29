import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.choices import Choices
from phonenumber_field.formfields import PhoneNumberField

class Employee(models.Model):
    martial_status_choices = Choices(
        ("single", _("Single")),
        ("married", _("Married")),
    )

    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)

    # Basic information
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    birth_date = models.DateTimeField(_("Birthdate"), auto_now=False, auto_now_add=False)
    martial_status = models.CharField(_("Martial Status"), max_length=10, choices=martial_status_choices)
    ssn_code = models.CharField(_("SSN code"), max_length=250)
    # Location information
    address = models.CharField(_("Address"), max_length=50)
    city = models.CharField(_("City"), max_length=250)
    post_code = models.CharField(_("Post Code"), max_length=12)

    # Contact details
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    personal_phone = PhoneNumberField()
    home_phone = PhoneNumberField()

    # Image
    image = models.ImageField(_("Image"), upload_to='employees/employee/')

    class Meta:
        verbose_name = _("employee")
        verbose_name_plural = _("employees")

    def __str__(self):
        return str(self.first_name + self.last_name)
