"""
    Create by Ahmad Ibrahim 
    at ١١‏/٣‏/٢٠٢٢ - ٤:٢١ م
"""
from django.shortcuts import render, redirect
from codes_source.settings import *
from main_site.models import UserProfile as Students, Student, Nationalities, Systems
from django.http import Http404


def all_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        get_items = Students.objects.filter(is_student=True)
        items = []
        for item in get_items:
            get_student = Student.objects.get(user=item)
            send_item = {
                'id': item.id,
                'username': item.username,
                'name': item.first_name,
                'pending': item.pending,
                'system': get_student.system.name_ar,
                'team': get_student.team.name_ar,
                'created_at': item.created_at,
                'created_by': item.created_by,
                'updated_at': item.updated_at,
                'updated_by': item.updated_by,
            }
            items.append(send_item)
        send_data = {
            'nameSite': nameSite[get_ln],
            'items': items
        }
        return render(request, 'pages/dashboard/students/all/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def add_web(request):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        get_nationalities = Nationalities.objects.filter(status=True)
        get_systems = Systems.objects.filter(status=True)
        send_data = {
            'nameSite': nameSite[get_ln],
            'get_nationalities': get_nationalities,
            'get_systems': get_systems,
        }
        return render(request, 'pages/dashboard/students/add/{}.html'.format(get_ln), send_data)
    else:
        return redirect('login_web')


def edit_web(request, id):
    if request.user.is_authenticated and request.user.is_active and request.user.is_staff or request.user.is_superuser :
        get_ln = request.user.ln
        try:
            item = Teams.objects.get(id=id)
        except:
            item = None
        if item:
            # get_systems = Systems.objects.filter(status=True)
            send_data = {
                'nameSite': nameSite[get_ln],
                # 'get_systems': get_systems,
                'item': item,
            }
            return render(request, 'pages/dashboard/students/edit/{}.html'.format(get_ln), send_data)
        else:
            return Http404
    else:
        return redirect('login_web')
