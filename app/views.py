from django.shortcuts import render
from .models import *
from django.db.models import Count, Q

# Create your views here.

def home(request):

    # Filter Operation
    queryset = None

    table_name = request.GET.get('table_name')
    column_name = request.GET.get('column_name')

    if table_name == 'MetaTable':
        if column_name == 'Sample':
            queryset = MetaDataTable.objects.values('sample')

    elif table_name == 'OtuTable':
        if column_name == 'Seq':
            queryset = OtuTable.objects.values('seq')

    elif table_name == 'TaxonomicTable':
        if column_name == 'Kingdom':
            queryset = TaxonomicTable.objects.values('kingdom')

    else:
        pass

    
    # Merge Operation
    q_join_1 = None
    q_join_2 = None
    
    table_1 = request.GET.get('table_1')
    table_2 = request.GET.get('table_2')
    q_type = request.GET.get('q_type')

    if table_1 == 'MetaTable' and table_2 == 'OtuTable' and q_type == 'Join':
        q_join_1 = OtuMetaTable.objects.select_related('seq_id', 'sample_id')

    elif table_1 == 'TaxonomicTable' and table_2 == 'OtuTable' and q_type == 'Join':
        q_join_2 = TaxonomicTable.objects.select_related('seq')
    
    else:
        pass

    # Search Operation
    search_queryset = None

    search_term = request.GET.get('search_term')

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
