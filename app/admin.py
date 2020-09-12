from django.contrib import admin
from .models import MetaDataTable, OtuTable, OtuMetaTable, TaxonomicTable

# Register your models here.

class MetaDataTableAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('id', 'sample', 'index_1', 'index_2', 'group', 'diet', 'cage', 'sample_type', 'orgin_diet')
    
    # Columns having links
    list_display_links = ('id', 'sample')

class OtuTableAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('id', 'seq', 'sa_1', 'sa_2', 'sa_3', 'sa_4', 'sa_5', 'sa_6', 'sa_7', 'sa_8', 'sa_9', 'sa_10', 'sa_11', 'sa_12', 'sa_13', 'sa_14', 'sa_15')
    
    # Columns having links
    list_display_links = ('id', 'seq')

class OtuMetaTableAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('id', 'seq_id', 'sample_id', 'value')
    
    # Columns having links
    list_display_links = ('id', 'seq_id')

class TaxonomicTableAdmin(admin.ModelAdmin):
    # Display columns in horizontal list
    list_display = ('id', 'seq', 'kingdom', 'phylum', 'taxonomy_class', 'order', 'family', 'genus', 'species')
    
    # Columns having links
    list_display_links = ('id', 'seq')
    
admin.site.register(MetaDataTable, MetaDataTableAdmin)
admin.site.register(OtuTable, OtuTableAdmin)
admin.site.register(OtuMetaTable, OtuMetaTableAdmin)
admin.site.register(TaxonomicTable, TaxonomicTableAdmin)