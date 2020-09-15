from django.shortcuts import render
from .models import *
from django.db.models import Count, Q

# Create your views here.

def home(request):

    # Filter Operation
    queryset = None

    # Get table name
    table_name = request.GET.get('table_name')
    # Get column name
    column_name = request.GET.get('column_name')

    """ Match table name & related column name & fetch relevant data """

    if table_name == 'MetaTable':
        if column_name == 'Sample':
            queryset = MetaDataTable.objects.values('sample')
        if column_name == 'Group':
            queryset = MetaDataTable.objects.values('group')
        if column_name == 'Diet':
            queryset = MetaDataTable.objects.values('diet')

    elif table_name == 'OtuTable':
        if column_name == 'Seq':
            queryset = OtuTable.objects.values('seq')
        if column_name == 'Sa1':
            queryset = OtuTable.objects.values('sa_1')
        if column_name == 'Sa2':
            queryset = OtuTable.objects.values('sa_2')

    elif table_name == 'TaxonomicTable':
        if column_name == 'Kingdom':
            queryset = TaxonomicTable.objects.values('kingdom')
        if column_name == 'Phylum':
            queryset = TaxonomicTable.objects.values('phylum')
        if column_name == 'Family':
            queryset = TaxonomicTable.objects.values('family')

    else:
        pass

    
    # Merge Operation
    q_join_1 = None
    q_join_2 = None
    
    # Get table1 name
    table_1 = request.GET.get('table_1')
    # Get table2 name
    table_2 = request.GET.get('table_2')
    # Get query type
    q_type = request.GET.get('q_type')

    """ Merge table1 & table2 by performing a SQL join operation """

    if table_1 == 'MetaTable' and table_2 == 'OtuTable' and q_type == 'Join':
        q_join_1 = OtuMetaTable.objects.select_related('seq_id', 'sample_id')

    elif table_1 == 'TaxonomicTable' and table_2 == 'OtuTable' and q_type == 'Join':
        q_join_2 = TaxonomicTable.objects.select_related('seq')
    
    else:
        pass

    # Search Operation
    search_queryset = None

    # Get search term
    search_term = request.GET.get('search_term')

    """ Match the search term & fetch relevant data """

    if search_term == 'sample':
        search_queryset = MetaDataTable.objects.values('sample')
    elif search_term == 'group':
        search_queryset = MetaDataTable.objects.values('group')
    elif search_term == 'diet':
        search_queryset = MetaDataTable.objects.values('diet')
    elif search_term == 'seq':
        search_queryset = OtuTable.objects.values('seq')
    elif search_term == 'sa_1':
        search_queryset = OtuTable.objects.values('sa_1')
    elif search_term == 'sa_2':
        search_queryset = OtuTable.objects.values('sa_2')
    elif search_term == 'kingdom':
        search_queryset = TaxonomicTable.objects.values('kingdom')
    elif search_term == 'phylum':
        search_queryset = TaxonomicTable.objects.values('phylum')
    elif search_term == 'family':
        search_queryset = TaxonomicTable.objects.values('family')
    else:
        pass
        
    context = {
        'queryset':queryset,
        'q_join_1':q_join_1,
        'q_join_2':q_join_2,
        'search_queryset':search_queryset,  
    }
    
    return render(request, 'index.html', context)
