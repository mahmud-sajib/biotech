from django.contrib import admin
from .models import *

admin.site.register(OtuTable)
admin.site.register(metadata)
admin.site.register(reference_sequence)
admin.site.register(otu_metad_id)
admin.site.register(taxonomic)

# Register your models here.
