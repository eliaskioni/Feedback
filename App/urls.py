from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^new_company/$', views.new_company, name='new_company'),
    url(r'^company_edit/(?P<id>[0-9]+)/$', views.company_edit, name='company_edit'),
    url(r'^company_delete/(?P<id>[0-9]+)/$', views.company_delete, name="company_delete"),
    url(r'^companies_list/$', views.companies_list, name='companies_list'),
    url(r'^company_detail/(?P<id>[0-9]+)/$', views.company_detail, name="company_detail"),
    url(r'^company_feedbacks/(?P<id>[0-9]+)/$', views.company_feedbacks, name='company_feedbacks'),
    url(r'^customer_feedback/(?P<company_id>[0-9]+)/$', views.customer_feedback, name='customer_feedback'),
    url(r'^new_employee/$', views.new_employee, name="new_employee"),
    url(r'^employee_detail/(?P<id>[0-9]+)/$', views.employee_detail, name="employee_detail"),
    url(r'^employee_edit/(?P<id>[0-9]+)/$', views.employee_edit, name='employee_edit'),
    url(r'^employee_delete/(?P<id>[0-9]+)/$', views.employee_delete, name="employee_delete"),
    url(r'^employees_list/$', views.employees_list, name='employees_list'),
    url(r'^add_company/(?P<company_id>[0-9]+)/(?P<employee_id>[0-9]+)/$', views.add_company, name='add_company'),
    url(r'^remove_company/(?P<company_id>[0-9]+)/(?P<employee_id>[0-9]+)/$', views.remove_company, name='remove_company'),
]
