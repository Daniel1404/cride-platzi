"""Custom User Model"""

from django.db import models

from django.contrib.auth.models import AbstractUser


# Phone Validator

from django.core.validators import RegexValidator

# Local CRide models

from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):

    """
    CRide Custom user:

    Extends the CRideModel and therefore has the following fields:

    created(DateTimeField)
    modified(DateTimeField)

    Extends the Django's Abstract user and modifies:

    Username(email)

    Adds some other functionality.
    """

    PHONE_REGEX = RegexValidator(
        regex=r'\+?1?\d{9,16}$',
        message="Phone number must be entered in the format: +999999999, up to 16 digits allowed"
    )

    email = models.EmailField(
        "email address",
        max_length=254,
        unique=True,

        # If the a user tries to create a user that already, has been created with
        # the given email, an error will be raised

        error_messages={
            "unique": "Some user with that email already exists"
        }
    )


    phone_number = models.CharField(
        "phone number",
        validators=[PHONE_REGEX],
        max_length=18,
        blank=True,
        null=True
    )


    is_client =  models.BooleanField(
        "client",
        default=True,
        help_text=(
            "Help to distinguish users and perform queries"
            "Clients are the main type of clients"
        )
    )

    is_verified = models.BooleanField(
        "verified",
        default=False,
        help_text=("Set to true when the user has verified it's email address")
    )

    def __str__(self):
        """Return username"""

        return self.username

    def get_short_name(self):
        """Return username"""
        
        return self.username


    USERNAME_FIELD = ("email")

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
