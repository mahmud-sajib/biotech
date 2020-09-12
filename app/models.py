from django.db import models

# Create your models here.

class MetaDataTable(models.Model):
    sample = models.CharField(max_length=50)
    index_1 = models.CharField(max_length=50)
    index_2 = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    cage = models.CharField(max_length=50)
    sample_type = models.CharField(max_length=50)
    orgin_diet = models.CharField(max_length=50)

    def __str__(self):
        return self.sample


class OtuTable(models.Model):
    seq = models.CharField(max_length=100, null=True)
    sa_1 = models.CharField(max_length=50, null=True)
    sa_2 = models.CharField(max_length=50, null=True)
    sa_3 = models.CharField(max_length=50, null=True)
    sa_4 = models.CharField(max_length=50, null=True)
    sa_5 = models.CharField(max_length=50, null=True)
    sa_6 = models.CharField(max_length=50, null=True)
    sa_7 = models.CharField(max_length=50, null=True)
    sa_8 = models.CharField(max_length=50, null=True)
    sa_9 = models.CharField(max_length=50, null=True)
    sa_10 = models.CharField(max_length=50, null=True)
    sa_11 = models.CharField(max_length=50, null=True)
    sa_12 = models.CharField(max_length=50, null=True)
    sa_13 = models.CharField(max_length=50, null=True)
    sa_14 = models.CharField(max_length=50, null=True)
    sa_15 = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.seq

class OtuMetaTable(models.Model):
    seq_id = models.ForeignKey(OtuTable, on_delete=models.SET_NULL, null=True)
    sample_id = models.ForeignKey(MetaDataTable, on_delete=models.SET_NULL, null=True)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.seq_id} | {self.sample_id}" 


class TaxonomicTable(models.Model):
    seq = models.ForeignKey(OtuTable, on_delete=models.SET_NULL, null=True, related_name='taxonomics')
    kingdom = models.CharField(max_length=50)
    phylum = models.CharField(max_length=50)
    taxonomy_class = models.CharField(max_length=50)
    order = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)

    def __str__(self):
        return self.kingdom






