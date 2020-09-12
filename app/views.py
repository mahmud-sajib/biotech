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

    
    # q_join = OtuMetaTable.objects.select_related('country', 'country_state', 'city')



    
    

    context = {
        # 'queryset':queryset,
        # # 'diet_queryset':diet_queryset,
        # 'group_queryset':group_queryset
        # 'column_name':column_name,
        'queryset':queryset,
    }
    
    
    return render(request, 'index.html', context)
