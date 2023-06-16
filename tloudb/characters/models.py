from django.db import models
from multiselectfield import MultiSelectField
from multiselectfield.validators import MaxValueMultiFieldValidator

class Character(models.Model):
    STATUS_CHOICES = (
        ('Alive', 'Alive'),
        ('Deceased', 'Deceased'),
        ('Unknown', 'Unknown'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    )

    name = models.CharField(max_length=80, verbose_name="First name", help_text="Enter character's first name")
    surname = models.CharField(max_length=80, blank=True, null=True, verbose_name="Surname", help_text="If known enter character's surname")
    description = models.CharField(max_length=300, verbose_name="Description", help_text="Enter a short description")
    lore = models.TextField(verbose_name="Backstory/Lore", help_text="Enter characters backstory/lore")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='Unknown', verbose_name="Status", help_text="Select character's status")
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Unknown', verbose_name='Gender', help_text="Enter character's gender")
    photo = models.ImageField(upload_to="characters", null=True, blank=True, verbose_name='Photo of character', help_text='Upload characters picture')
    affiliation = models.ManyToManyField('Groups', blank=True, verbose_name='Affiliation')
    appears = models.ManyToManyField('Games', verbose_name='Appears in')

    class Meta:
        ordering = ['name']
        verbose_name = 'Character',
        verbose_name_plural = 'Characters'

    def __str__(self):
        if(self.surname == None):
            return f'{self.name}'
        else:
            return f'{self.name} {self.surname}'
    
class Groups(models.Model):
    name = models.CharField(max_length=80, verbose_name="Group name", help_text="Enter group's name")
    description = models.TextField(blank=True, null=True, help_text="Enter groups description")

    class Meta:
        ordering = ['name']
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return f'{self.name}'
    
class Games(models.Model):
    PLATFORMS_CHOICES = (
        ('PS3', 'Playstation3'),
        ('PS4', 'Playstation4'),
        ('PS5', 'Playstation5'),
        ('PC', 'Computer')
    )

    name = models.CharField(max_length=80, verbose_name="Game name", help_text="Enter game's full name")
    isDLC = models.BooleanField(verbose_name="is DLC", help_text="Is this game a DLC?")
    released = models.DateField(verbose_name="released", help_text="Release date of this game")
    platforms = MultiSelectField(choices=PLATFORMS_CHOICES, default=['PS3'], verbose_name='platform', validators=[MaxValueMultiFieldValidator(4)] )

    class Meta:
        ordering = ["released"]
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return f'{self.name}'