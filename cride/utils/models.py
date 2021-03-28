"""Django custom utilities"""

# Django model
from django.db import models


class CRideModel(models.Model):

    """
    CRideModel: 

    Custom Base model, from which every other model
    in the project will inherit.

    This class provides the following tables:

    created(DateTimeField): Stores the date and time the object was created
    modified(DateTimeField): Stores the last date and time the object was modified
    """

    created = models.DateTimeField(
        "created at",
        # Records the date automatically
        auto_now_add=True,

        help_text="Date time in which the object was created"
    )


    modified = models.DateTimeField(
        "created at",
        # Records the date each time the model hits "save()"
        auto_now=True,
        help_text="Date time in which the object was modified"
    )

    class Meta:
        """Meta class: Abstract class"""

        abstract = True

        # Latest by =  last object that has been created
        get_latest_by = "created" 

        # Last created will be the latest
        # Also applies for modified
        ordering = ["-created", "-modified"]


