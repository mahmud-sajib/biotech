from django.db import models

# Create your models here.
from django.utils import timezone
from django.shortcuts import reverse # import reverse to get URL in the right form
# Create your models here.


# creat table to list all incomming files for download and information
#---------------------------------------------------------------------------

class dataOverwiewFATMAL(models.Model):
    File_ID = models.IntegerField(primary_key=True)
    File = models.TextField(null=True)
    File_Type =  models.CharField(max_length=255, blank=True)
    Responsible_Person_1 = models.TextField(null=True, blank=True)
    Email_1 = models.EmailField(max_length=254)
    Responsible_Person_2 = models.TextField(null=True, blank=True)
    Email_2 = models.EmailField(max_length=254)
    Short_Info = models.TextField(null=True, blank=True)
    Cohort_Sample_Name = models.CharField(max_length=255, blank=True)
    Download_Link = models.FileField(upload_to='media')
    def __str__(self):
        return self.Responsible_Person_1 + " : " + self.Email_1
        return self.Responsible_Person_2 + " : " + self.Email_2

# OtuTable Model
#--------------------------------

class OtuTable(models.Model):
    hash = models.CharField(max_length=255, null=True)
    sa_5594 = models.CharField(max_length=255, null=True)
    sa_5902 = models.CharField(max_length=255, null=True)
    sa_5596 = models.CharField(max_length=255, null=True)
    sa_5903 = models.CharField(max_length=255, null=True)
    sa_5898 = models.CharField(max_length=255, null=True)
    sa_5604 = models.CharField(max_length=255, null=True)
    sa_5894 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v17 = models.CharField(max_length=255, null=True)
    sa_5619 = models.CharField(max_length=255, null=True)
    sa_blank = models.CharField(max_length=255, null=True)
    sa_5608 = models.CharField(max_length=255, null=True)
    sa_5615 = models.CharField(max_length=255, null=True)
    sa_5897 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v11 = models.CharField(max_length=255, null=True)
    sa_5605 = models.CharField(max_length=255, null=True)
    sa_5620 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v15 = models.CharField(max_length=255, null=True)
    sa_5901 = models.CharField(max_length=255, null=True)
    sa_5896 = models.CharField(max_length=255, null=True)
    sa_5900 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v16 = models.CharField(max_length=255, null=True)
    sa_5616 = models.CharField(max_length=255, null=True)
    sa_5597 = models.CharField(max_length=255, null=True)
    sa_5904 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v11 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v9 = models.CharField(max_length=255, null=True)
    sa_5899 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v13 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v15 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v16 = models.CharField(max_length=255, null=True)
    sa_5598 = models.CharField(max_length=255, null=True)
    sa_5610 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v12 = models.CharField(max_length=255, null=True)
    sa_5595 = models.CharField(max_length=255, null=True)
    sa_5618 = models.CharField(max_length=255, null=True)
    sa_5607 = models.CharField(max_length=255, null=True)
    sa_5895 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v14 = models.CharField(max_length=255, null=True)
    sa_5611 = models.CharField(max_length=255, null=True)
    sa_5613 = models.CharField(max_length=255, null=True)
    sa_5612 = models.CharField(max_length=255, null=True)
    sa_5603 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v9 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v13 = models.CharField(max_length=255, null=True)
    sa_5609 = models.CharField(max_length=255, null=True)
    sa_5621 = models.CharField(max_length=255, null=True)
    sa_5601 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v12 = models.CharField(max_length=255, null=True)
    sa_5622 = models.CharField(max_length=255, null=True)
    sa_inoc_a_v10 = models.CharField(max_length=255, null=True)
    sa_5593 = models.CharField(max_length=255, null=True)
    sa_5905 = models.CharField(max_length=255, null=True)
    sa_5614 = models.CharField(max_length=255, null=True)
    sa_5606 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v17 = models.CharField(max_length=255, null=True)
    sa_5599 = models.CharField(max_length=255, null=True)
    sa_5617 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v10 = models.CharField(max_length=255, null=True)
    sa_inoc_ref_v14 = models.CharField(max_length=255, null=True)
    sa_5600 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.hash



# creat metadata table
#------------------------

class metadata(models.Model):
    sample = models.CharField(max_length=255, blank=True)
    Index_1 = models.CharField(max_length=255, blank=True)
    Index_2 = models.CharField(max_length=255, blank=True)
    Group = models.CharField(max_length=255, blank=True)
    Diet = models.CharField(max_length=255, blank=True)
    Cage = models.CharField(max_length=255, blank=True)
    Type = models.CharField(max_length=255, blank=True)
    Orgin_Diet = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.sample


# creat reference table
#-----------------------

class reference_sequence(models.Model):
    hash = models.ForeignKey(OtuTable, on_delete=models.SET_NULL, null=True, related_name='reference_sequence', max_length = 255)
    hash_seq = models.CharField(max_length=255, null=True)
    Sequence = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Sequence


# creat a otu table
#-----------------------

class otu_metad_id(models.Model): #what arguments should be passed to create an instance of URLField.
    otu_hash = models.ForeignKey(OtuTable, db_index=False, db_column= 'otu_hash', on_delete=models.SET_NULL, null=True)
    meta_hash = models.ForeignKey(metadata, db_index=False, db_column= 'meta_hash', on_delete=models.SET_NULL, null=True)
    value =  models.IntegerField(null = True)

    def __str__(self):
        return f"{self.otu_hash} | {self.meta_hash}"

#creat taxonomic table
#----------------------

class taxonomic(models.Model):
    hash = models.ForeignKey(OtuTable, on_delete=models.SET_NULL, null=True, related_name='taxonomics', max_length = 255)
    Kingdom = models.CharField(max_length=255, blank=True)
    Phylum = models.CharField(max_length=255, blank=True)
    Class = models.CharField(max_length=255, blank=True)
    Order = models.CharField(max_length=255, blank=True)
    Family = models.CharField(max_length=255, blank=True)
    Genus = models.CharField(max_length=255, blank=True)
    Species = models.CharField(max_length=255, blank=True)
    hash_seq = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.Kingdom

