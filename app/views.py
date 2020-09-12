from django.shortcuts import render
from .models import *
from django.db.models import Count, Q

# Create your views here.

def home(request):
    # queryset = None
    # # diet_queryset = None
    # group_queryset = None
    

    # search_query = request.GET.get('q')
    # search_query = str(search_query).split(",")

    # print(search_query)
    # print(search_query[0])
    # # print(search_query[1:2])
    # print(search_query[-1])

    
    # if search_query[0] == 'sample':
    #     queryset = MetaDataTable.objects.values('sample')
    #     print(queryset)
    
    # # if search_query[1:2] == list('diet'):
    # #     diet_queryset = MetaDataTable.objects.values('diet')
    # #     print(diet_queryset)

    # if search_query[-1] == list('group'):
    #     group_queryset = MetaDataTable.objects.values('group')
    #     print(group_queryset)

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




    
    

    context = {
        # 'queryset':queryset,
        # # 'diet_queryset':diet_queryset,
        # 'group_queryset':group_queryset
        # 'column_name':column_name,
        'queryset':queryset,
        'q_join_1':q_join_1,
        'q_join_2':q_join_2,
        
    }
    
    
    return render(request, 'index.html', context)
