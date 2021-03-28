"""
Circles model
"""

# Django
from django.db import models

# Base model
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """
    Circle Model

    A circle is a private group rides are offered and taken by it's members.

    To join a Circle a user must receive an unique invitation code from an existing circle member.
    """

    name = models.CharField(
        "circle name",
        max_length=140
    )

    slug = models.SlugField(
        unique=True,
        max_length=40
    )

    description = models.CharField(
        "circle description",
        max_length=255
    )

    picture = models.ImageField(
        upload_to="circles/pictures",
        blank=True,
        null=True
    )

    # Stats
    rides_offered = models.PositiveIntegerField(
        default=0
    )

    rides_taken = models.PositiveIntegerField(
        default=0
    )

    verified = models.BooleanField(
        "verified circle",
        default=False,
        help_text="Verified circles are also know as official communities"
    )

    is_public = models.BooleanField(
        "public",
        default=True,
        help_text="If a circle isn't private it means that just the members know about it, and doesn't allow external users to join"
    )

    is_limited = models.BooleanField(
        "limited",
        default=False,
        help_text="Limited groups can grow up to a fixed number of members"
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text="If circle is limited, this will be the limit of members"
    )

    class Meta(CRideModel.Meta):
        """Ordering by the numbers of rides"""

        ordering = ["-rides_taken", "-rides_offered"]

    def __str__(self):
        return self.name