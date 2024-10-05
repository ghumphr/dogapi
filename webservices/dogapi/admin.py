from django.contrib import admin
from .models import Dog
from .models import Breed

# Register your models here.

# adapted from https://mlhale.github.io/CYBR8470/modules/webservices/
class DogAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy',)
    
    # Add search functionality for specific fields
    search_fields = ('name', 'breed',)

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'breed',)

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy',)

# Register the model and admin class
admin.site.register(Dog, DogAdmin)

class BreedAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds',)
    
    # Add search functionality for specific fields
    search_fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds',)

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds',)

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Breed instance
    fields = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds',)

# Register the model and admin class
admin.site.register(Breed, BreedAdmin)

