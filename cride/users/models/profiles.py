"""Profile for each user"""

# Models
from django.db import models

# Utils
from cride.utils.models import CRideModel


class Profile(CRideModel):
    """
    Profile Model

    The profile holds the public stats of user's data.
    Like biography, profile picture and statistics.
    """

    user = models.OneToOneField(
        "users.User",
        verbose_name="user",
        on_delete=models.CASCADE
    )

    picture = models.ImageField(
        verbose_name="profile picture",
        upload_to="users/pictures/",
        blank=True,
        null=True
    )

    biography = models.TextField(
        max_length=500,
        default="This user doesn't have a description yet",
        blank=True
    )

    rides_taken = models.PositiveIntegerField(
        default=0
    )

    rides_offered = models.PositiveIntegerField(
        default=0
    )

    reputation = models.FloatField(
        default=5.0,
        help_text="User's reputation is based on it's offered/taken rides quality"
    )

    def __str__(self):
        """Returns the __str__ of the user one to one field"""

        return str(self.user)
    
    
    

