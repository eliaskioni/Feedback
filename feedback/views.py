from django.shortcuts import render
from django.contrib.auth import login as feedback_login, logout as feedback_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from feedback.forms import CompanyForm, EmployeeCreateForm, FeedbackForm, EmployeeEditForm
from feedback.models import Company, Feedback
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.user.is_authenticated():
        companies = Company.objects.all()
        employees = User.objects.all().filter(is_superuser = False)
        return render(request, 'feedback/index.html', {'companies':companies,
                                    'employees':employees})
    else:
        return HttpResponseRedirect(reverse('feedback:login'))

def login(request):
    #checks if the user is already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('feedback:index'))
    #if the user is not logged in displays the log in form
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                feedback_login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('feedback:index'))  #admin page
                else:
                    return HttpResponseRedirect(reverse('feedback:companies_list'))  #employee page
        else:
            form = AuthenticationForm(request)
        return render(request, 'feedback/login.html', {'form': form })

def logout(request):
    #logs out a given user request and redisplay the logging form
    feedback_logout(request)
    return HttpResponseRedirect(reverse('feedback:login'))

def new_company(request):
    if request.user.is_active:
        if request.method == "POST":
            form = CompanyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('feedback:index'))
        else:
            form = CompanyForm()
        return render(request, 'feedback/new_company.html', {'form': form })
    else:
        return HttpResponseRedirect(reverse('feedback:index'))

def company_edit(request, id):                   # changed to company edit
    company = Company.objects.get(pk=id)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feedback:index'))
    else:
        form = CompanyForm(instance=company)
    return render(request, 'feedback/company_edit.html', {'form': form, 'company': company })

def company_delete(request, id):
    company = Company.objects.get(pk=id)
    company.delete()
    return HttpResponseRedirect(reverse('feedback:index'))

def new_employee(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = EmployeeCreateForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(
                username = form.cleaned_data['first_name'],
                password = form.cleaned_data['password'],
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('feedback:index'))
        else:
            form = EmployeeCreateForm()
        return render(request, 'feedback/new_employee.html', {'form': form })
    else:
        return HttpResponseRedirect(reverse('feedback:login'))

def employee_edit(request, id):
    if request.user.is_superuser:
        employee = User.objects.get(pk=id)
        if request.method == "POST":
            form = EmployeeEditForm(request.POST, instance=employee)
            if form.is_valid():
                employee.username = form.cleaned_data['username']
                employee.first_name = form.cleaned_data['last_name']
                if form.cleaned_data['password'] == '':
                    pass
                else:
                    employee.set_password(form.cleaned_data['password'])
                employee.save()
                return HttpResponseRedirect(reverse('feedback:index'))
        else:
            form = EmployeeEditForm(instance=employee)
        return render(request, 'feedback/employee_edit.html', {'form': form, 'employee': employee,
                                                                 'companies': Company.objects.all() })
    else:
        return HttpResponseRedirect(reverse('feedback:index'))

def employee_delete(request, id):
    employee = User.objects.get(pk=id)
    employee.delete()
    return HttpResponseRedirect(reverse('feedback:index'))

def employee_detail(request, id):
    employee = User.objects.get(pk=id)
    return render(request, 'feedback/employee_detail.html', {'employee': employee })

def add_company(request, company_id, employee_id):
    if request.user.is_authenticated():
        company = Company.objects.get(pk=company_id)
        employee = User.objects.get(pk=employee_id)
        company.employees.add(employee)

        if request.user.is_superuser:
            return HttpResponseRedirect(reverse('feedback:employee_edit',args=(employee.id,)))
        else:
            return HttpResponseRedirect(reverse('feedback:companies_list'))
    else:
        pass

def remove_company(request, company_id, employee_id):
    if request.user.is_superuser:
        company = Company.objects.get(pk=company_id)
        employee = User.objects.get(pk=employee_id)
        company.employees.remove(employee)
        return HttpResponseRedirect(reverse('feedback:employee_edit', args=(employee.id,)))
    else:
        return HttpResponseRedirect(reverse('feedback:companies_list'))

def companies_list(request):
    companies = Company.objects.all()
    return render(request, 'feedback/companies_list.html', {'companies': companies })

def company_feedbacks(request, id):
    company = Company.objects.get(pk=id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback.objects.create(
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            phone_number = form.cleaned_data['phone_number'],
            comment = form.cleaned_data['comment'],
            company = company
            )
            return HttpResponseRedirect(reverse('feedback:company_feedbacks', args=(company.id,)))
    else:
        form = FeedbackForm()
    return render(request, 'feedback/company_feedback.html', {'company': company,
                                                              'form': form  })

def employee_homepage(request):
    return render(request, 'feedback/employee_homepage.html')

def company_detail(request, id):
    company = Company.objects.get(pk=id)
    return render(request, 'feedback/company_detail.html', {'company': company })

def employees_list(request):
    if request.user.is_authenticated():
        employees = User.objects.all()
        return render(request, 'feedback/employees_list.html', {'employees': employees})
    else:
        return HttpResponseRedirect(reverse('feedback:companies_list'))

def customer_feedback(request, company_id):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
    else:
        return HttpResponseRedirect(revrse('feedback:homepage'))

def homepage(request):
    return HttpResponseRedirect(reverse('feedback:companies_list'))
