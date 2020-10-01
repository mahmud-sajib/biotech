from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
# from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
# from django import template # import template css, js, html
# import datetime
from .models import *  #import models
# # from .forms import *   #import from forms.py
# from django.core.mail import send_mail, BadHeaderError # import models for email
# from django.views.generic import ListView
# from django.contrib.auth import authenticate, login, logout # import modules for password login
# import csv
# from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# from django.db import connection
from django.db.models import Count, Q


#Contact Email
#-------------------------------

def Contact(request):
    # Retrieve post by id
    if request.method == 'GET':
        # Form was submitted
        form = ContactForm() #get the form from forms.py
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd = form.cleaned_data
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            email = cd['from_email']
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}\'s comments: {cd['comments']}"
            try:
                send_mail(subject, message, from_email, 'amoelmoela@gmail.com', [cd['to']])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'FATMAL/HTML/contact.html', {'form':form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

#overwiev Filter
#-------------------------------------
def data_download(request):
    overwiev = dataOverwiewFATMAL.objects.all()
    overwievFilter = OverwievFilter(request.GET, queryset=overwiev)

    return render(request, 'FATMAL/HTML/overwiev.html', {'overwievFilter': overwievFilter})

# login view
#--------------------------------

def user_login(request):
    if request.method == 'POST':
        form  = LoginForm(request.POST)  #LoginForm from forms.py / #submitted data
        if form.is_valid(): # check whether the form is valid
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password']) #authenticate the user again the database
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully') # display the message
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form':form})

#new view to display a home when users log in to their account
#-------------------------------------------------------------------
@login_required
def home(request):
    return render(request, 'FATMAL/HTML/home.html', {'section':'home'})


# creat a search, filter and merge view
#----------------------------------------

def dataVisual(request):

    # Filter Operation
###########################

    queryset = None

    #Get table name
    table_name = request.GET.get('table_name')
    #Get column name
    column_name = request.GET.get('column_name')

    """ Match table name & related column name & fetch relevant data """
    #MetaData

    if table_name == 'Meta_Table': # random name
        if column_name == 'Sample': # random name
            queryset = metadata.objects.values('sample') #name from models.py
        elif column_name == 'Index_1':
            queryset = metadata.objects.values('Index_1')
        elif column_name == 'Index_2':
            queryset = metadata.objects.values('Index_2')
        elif column_name == 'Group':
            queryset = metadata.objects.values('Group')
        elif column_name == 'Diet':
            queryset = metadata.objects.values('Diet')
        elif column_name == 'Cage':
            queryset = metadata.objects.values('Cage')
        elif column_name == 'Type':
            queryset = metadata.objects.values('Type')
        elif column_name == 'Orgin_Diet':
            queryset = metadata.objects.values('Orgin_Diet')

    #OTU Table

    elif table_name == 'OtuTable':
        if column_name == 'hash':
            queryset = OtuTable.objects.values('hash')
        elif column_name == 'sa_5594':
            queryset = OtuTable.objects.values('sa_5594')
        elif column_name == 'sa_5902':
            queryset = OtuTable.objects.values('sa_5902')

   #Taxonomic Table
    elif table_name == 'Taxonomic_Table':
        if column_name == 'Kingdom':
            queryset = taxonomic.objects.values('Kingdom')
        elif column_name == 'Phylum':
            queryset = taxonomic.objects.values('Phylum')
        elif column_name == 'Family':
            queryset = taxonomic.objects.values('Family')

  #Reference Table
    elif table_name == 'Reference_Sequence_Table':
        if column_name == 'Hash':
            queryset = reference_sequence.objects.values('hash')
        elif column_name == 'Hash_Seq':
            queryset = reference_sequence.objects.values('hash_seq')
        elif column_name == 'Sequence':
            queryset = reference_sequence.objects.values('Sequence')
    else:
        pass

    # Merge Operation
###########################

    q_join_1 = None
    q_join_2 = None
    #q_join_3 = None

    # Get table1 name
    table_1 = request.GET.get('table_1')
    # Get table2 name
    table_2 = request.GET.get('table_2')
    # Get query type
    q_type = request.GET.get('q_type')

    """ Merge table1 & table 2 by performing a SQL join operation """

    if table_1 == 'Meta_Table' and table_2 == "OtuTable" and q_type == 'Join':
        q_join_1 = otu_metad_id.objects.select_related('otu_hash', 'meta_hash')

    elif table_1 == "Taxonomic_Table" and table_2 == "OtuTable" and q_type == 'Join':
        q_join_2 = taxonomic.objects.select_related('hash',)
        print(f"JOIN Q: {q_join_2}")
    else:
        pass

    # Search Operation
    search_queryset = None

    #Get search term
    search_term = request.GET.get('search_term')

    """ Match the search term & fetch relevant data """

    #MetaData
    if search_term == 'sample':
        search_queryset = metadata.objects.values('sample')
    elif search_term == 'Index_1':
        search_queryset = metadata.objects.values('Index_1')
    elif search_term == 'Index_2':
        search_queryset = metadata.objects.values('Index_2')
    elif search_term == 'Group':
        search_queryset = metadata.objects.values('Group')
    elif search_term == 'Diet':
        search_queryset = metadata.objects.values('Diet')
    elif search_term == 'Cage':
        search_queryset = metadata.objects.values('Cage')
    elif search_term == 'Type':
        search_queryset = metadata.objects.values('Type')
    elif search_term == 'Orgin_Diet':
        search_queryset = metadata.objects.values('Orgin_Diet')
    #OTU Data
    elif search_term == 'hash':
       search_queryset = OtuTable.objects.values('hash')
    elif search_term == 'sa_5594':
       search_queryset = OtuTable.objects.values('sa_5594')

    else:
        pass

    context = {'queryset':queryset,
               'q_join_1':q_join_1,
               'q_join_2':q_join_2,
               'search_queryset':search_queryset,
    }

    return render(request, 'dataVisual.html', context)

