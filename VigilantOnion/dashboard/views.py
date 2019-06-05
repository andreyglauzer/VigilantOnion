from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q, Case, When
import datetime
import collections
from .models import *
from .forms import *

app_name = 'VigilantOnion'

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],
				   password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/')
				else:
					return HttpResponse('Disabled account')
			else:
				messages.error(request, 'Error')
	else:
		form = LoginForm()


	today = datetime.datetime.now()
	month = today.month

	months = {
		  "1":"January",
		  "2":"Febuary",
		  "3":"March",
		  "4":"April",
		  "5":"May",
		  "6":"June",
		  "7":"July",
		  "8":"August",
		  "9":"September",
		  "10":"October",
		  "11":"November",
		  "12":"December"
	}

	for months_number in months.items():
		if int(months_number[0]) == month:
			month_one = months_number[1]
		elif int(months_number[0])  == month-1:
			month_two = months_number[1]
		elif int(months_number[0]) == month-2:
			month_three = months_number[1]

	sucess = UrlOnion.objects.filter(status=1)
	errors = UrlOnion.objects.filter(status=0)
	total = UrlOnion.objects.all().order_by('-last_date')


	sucess_month_one = UrlOnion.objects.filter(last_date__month=month, status=1)
	error_month_one = UrlOnion.objects.filter(last_date__month=month, status=0)
	sucess_month_two = UrlOnion.objects.filter(last_date__month=month-1, status=1)
	error_month_two = UrlOnion.objects.filter(last_date__month=month-1, status=0)
	sucess_month_three = UrlOnion.objects.filter(last_date__month=month-2, status=1)
	error_month_three = UrlOnion.objects.filter(last_date__month=month-2, status=0)
	sucess_month_four = UrlOnion.objects.filter(last_date__month=month-3, status=1)
	error_month_four = UrlOnion.objects.filter(last_date__month=month-3, status=0)

	categories = collections.Counter()
	for category in UrlOnion.objects.select_related('categorie').all():
		if category.categorie_id:
			categories[category.categorie]+= 1

	list_numbers = [
		sucess_month_one.count(),
		error_month_one.count(),
		sucess_month_two.count(),
		error_month_two.count(),
		sucess_month_three.count(),
		error_month_three.count(),
		sucess_month_four.count(),
		error_month_four.count(),
	]

	graphic_number = max(list_numbers)

	context = {


		'graphic_number': graphic_number+2,



		'form': form,
		'month_one': month_one,
		'month_two': month_two,
		'month_three': month_three,
		'total': total.count(),
		'sucess': sucess.count(),
		'errors': errors.count(),
		'notseen': total.count()-sucess.count()-errors.count(),
		'visited': total[0:4],
		'categories': categories.most_common(),
		'sucess_month_one': sucess_month_one.count(),
		'error_month_one': error_month_one.count(),
		'sucess_month_two': sucess_month_two.count(),
		'error_month_two': error_month_two.count(),
		'sucess_month_three': sucess_month_three.count(),
		'error_month_three': error_month_three.count(),
		'sucess_month_four': sucess_month_four.count(),
		'error_month_four': error_month_four.count(),



	}

	return render(request, 'dashboard/index.html', context)

@login_required
def dashboard(request):

	template_name = 'dashboard/index.html'

	return render(request, template_name)


@login_required
def registerurl(request):
	template_name = 'dashboard/register/urls.html'
	if request.method == 'POST':
		form = register_url_form(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = register_url_form()
	urls = UrlOnion.objects.filter(status=1)

	context = {
		'form': form,
		'urls': urls,
	}

	return render(request, template_name, context)

@login_required
def registercategory(request):
	template_name = 'dashboard/register/category.html'
	if request.method == 'POST':
		form = NameCategoriesForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = NameCategoriesForm()
	category = NameCategories.objects.all()

	context = {
		'form': form,
		'category': category,
	}

	return render(request, template_name, context)


@login_required
def registerterm(request):
	template_name = 'dashboard/register/category_term.html'
	if request.method == 'POST':
		form = CategoriesForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = CategoriesForm()
	category = Categories.objects.all()
	context = {
		'form': form,
		'category': category,
	}

	return render(request, template_name, context)


@login_required
def registersource(request):
	template_name = 'dashboard/register/source.html'
	if request.method == 'POST':
		form = register_source(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = register_source()
	category = Source.objects.all()

	context = {
		'form': form,
		'category': category,
	}

	return render(request, template_name, context)

@login_required
def registercompany(request):
	template_name = 'dashboard/register/company.html'
	if request.method == 'POST':
		form = CompanyNameForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = CompanyNameForm()
	company = CompanyName.objects.all()

	context = {
		'form': form,
		'company': company
	}

	return render(request, template_name, context)


@login_required
def registerkeyword(request):
	template_name = 'dashboard/register/company_term.html'
	if request.method == 'POST':
		form = CompanyTermForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.save()
			#form.save_m2m()
			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = CompanyTermForm()
	keyword = CompanyTerm.objects.all()

	context = {
		'form': form,
		'keyword': keyword
	}

	return render(request, template_name, context)

@login_required
def urls_detail(request, pk):
	detail_dashboard_view = get_object_or_404(UrlOnion, pk=pk)
	template_name = 'dashboard/edit/urls.html'
	if request.method == 'POST':
		form_edit_dashboard = register_url_form(request.POST, instance=get_object_or_404(UrlOnion, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = register_url_form(instance=get_object_or_404(UrlOnion, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = register_url_form(instance=get_object_or_404(UrlOnion, pk=pk))

	teste = UrlOnion.objects.all()
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,
		 'teste': teste,


	}

	form_edit_dashboard = register_url_form(instance=get_object_or_404(UrlOnion, pk=pk))

	return render(request, template_name, context)


@login_required
def category(request, pk):
	detail_dashboard_view = get_object_or_404(NameCategories, pk=pk)
	template_name = 'dashboard/edit/category.html'
	if request.method == 'POST':
		form_edit_dashboard = NameCategoriesForm(request.POST, instance=get_object_or_404(NameCategories, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = NameCategoriesForm(instance=get_object_or_404(NameCategories, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = NameCategoriesForm(instance=get_object_or_404(NameCategories, pk=pk))
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,
	}

	form_edit_dashboard = NameCategoriesForm(instance=get_object_or_404(NameCategories, pk=pk))

	return render(request, template_name, context)


@login_required
def edit_source(request, pk):
	detail_dashboard_view = get_object_or_404(Source, pk=pk)
	template_name = 'dashboard/edit/source.html'
	if request.method == 'POST':
		form_edit_dashboard = register_source(request.POST, instance=get_object_or_404(Source, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = register_source(instance=get_object_or_404(Source, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = register_source(instance=get_object_or_404(Source, pk=pk))
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,
	}

	form_edit_dashboard = register_source(instance=get_object_or_404(Source, pk=pk))

	return render(request, template_name, context)


@login_required
def category_term(request, pk):
	detail_dashboard_view = get_object_or_404(Categories, pk=pk)
	template_name = 'dashboard/edit/category_term.html'
	if request.method == 'POST':
		form_edit_dashboard = CategoriesForm(request.POST, instance=get_object_or_404(Categories, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = CategoriesForm(instance=get_object_or_404(Categories, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = CategoriesForm(instance=get_object_or_404(Categories, pk=pk))
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,
	}

	form_edit_dashboard = CategoriesForm(instance=get_object_or_404(Categories, pk=pk))

	return render(request, template_name, context)


@login_required
def company_category(request, pk):
	detail_dashboard_view = get_object_or_404(CompanyName, pk=pk)
	template_name = 'dashboard/edit/company.html'
	if request.method == 'POST':
		form_edit_dashboard = CompanyNameForm(request.POST, instance=get_object_or_404(CompanyName, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = CompanyNameForm(instance=get_object_or_404(CompanyName, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = CompanyNameForm(instance=get_object_or_404(CompanyName, pk=pk))
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,


	}

	form_edit_dashboard = CompanyNameForm(instance=get_object_or_404(CompanyName, pk=pk))

	return render(request, template_name, context)


@login_required
def company_category_term(request, pk):
	detail_dashboard_view = get_object_or_404(CompanyTerm, pk=pk)
	template_name = 'dashboard/edit/company_term.html'
	if request.method == 'POST':
		form_edit_dashboard = CompanyTermForm(request.POST, instance=get_object_or_404(CompanyTerm, pk=pk))
		if form_edit_dashboard.is_valid():
			form_edit_dashboard.save()
			form_edit_dashboard = CompanyTermForm(instance=get_object_or_404(CompanyTerm, pk=pk))
			messages.success(request, 'Sucess.')
		else:
			messages.error(request, 'Error')

	form_edit_dashboard = CompanyTermForm(instance=get_object_or_404(CompanyTerm, pk=pk))
	context = {
		 'detail_dashboard_view': detail_dashboard_view,
		 'form_edit_dashboard': form_edit_dashboard,


	}

	form_edit_dashboard = CompanyTermForm(instance=get_object_or_404(CompanyTerm, pk=pk))

	return render(request, template_name, context)

def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/')


# Cadastrar novo usuário
@login_required
def register_user(request):
	template_name = 'dashboard/users/register.html'
	if request.method == 'POST':
		form = register_user_form(request.POST, request.FILES)
		if form.is_valid():
			#user = form.save(commit=False)
			user = form.save()
			user.save()
			#form.save_m2m()

			messages.success(request, 'Sucesso')
		else:
			messages.error(request, 'Erro')

	form = register_user_form()
	context = {
		'form': form,
	}

	return render(request, template_name, context)

#  Lista todos os usuários
@login_required
def all_users(request):
	get_users = CustomUser.objects.all()
	template_name = 'dashboard/users/all.html'

	paginator = Paginator(get_users, 10)
	page = request.GET.get('page')
	users = paginator.get_page(page)

	context = {
		'users': users
	}

	return render(request, template_name, context)

# Deleta os usuários
@staff_member_required
@login_required
def del_user(request, pk):
	template_name = 'VigilantOnion:all_users'
	try:
		u = CustomUser.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Usuário Deletado")

	except table_user.DoesNotExist:
		messages.error(request, "Usuário não existe")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Algo deu errado')
		return render(request, template_name)

	return render(request, template_name)

@login_required
def user_detail(request, pk):
	detail_users_view = get_object_or_404(CustomUser, pk=pk)
	template_name = 'dashboard/users/edit.html'
	if request.method == 'POST':
		form_edit_user = edit_user_form(request.POST, instance=get_object_or_404(CustomUser, pk=pk))
		if form_edit_user.is_valid():
			form_edit_user.save()
			form_edit_user = edit_user_form(instance=get_object_or_404(CustomUser, pk=pk))
			messages.success(request, 'Perfil Atualizado com sucesso.')
		else:
			messages.error(request, 'Ops, algo deu errado.')

	form_edit_user = edit_user_form(instance=get_object_or_404(CustomUser, pk=pk))
	context = {
		 'detail_users_view': detail_users_view,
		 'form_edit_user': form_edit_user,


	}

	form_edit_user = edit_user_form(instance=get_object_or_404(CustomUser, pk=pk))

	return render(request, template_name, context)

@login_required
def all_urls(request):
	template_name = 'dashboard/all/urls.html'

	urls = UrlOnion.objects.all()
	urls_true = []
	for u in urls:
		if u.status == 1:
			urls_true.append(u)
	context = {
		'urls': urls_true,
	}

	return render(request, template_name, context)


# Deleta os usuários
@staff_member_required
@login_required
def del_source(request, pk):
	template_name = 'VigilantOnion:registersource'
	try:
		u = Source.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Source deleted")

	except table_user.DoesNotExist:
		messages.error(request, "Source does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)

# Deleta os usuários
@staff_member_required
@login_required
def del_category(request, pk):
	template_name = 'VigilantOnion:newcategory'
	try:
		u = NameCategories.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Category deleted")

	except table_user.DoesNotExist:
		messages.error(request, "Category does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)

@staff_member_required
@login_required
def del_category_term(request, pk):
	template_name = 'VigilantOnion:newterm'
	try:
		u = Categories.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Category Term deleted")

	except table_user.DoesNotExist:
		messages.error(request, "Category Term does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)

@staff_member_required
@login_required
def del_keyword(request, pk):
	template_name = 'VigilantOnion:newkeyword'
	try:
		u = CompanyTerm.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Keyword Term deleted")

	except table_user.DoesNotExist:
		messages.error(request, "Keyword Term does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)


@staff_member_required
@login_required
def del_company(request, pk):
	template_name = 'VigilantOnion:newcompany'
	try:
		u = CompanyName.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "Company deleted")

	except table_user.DoesNotExist:
		messages.error(request, "Company does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)

@staff_member_required
@login_required
def del_urls(request, pk):
	template_name = 'VigilantOnion:dashboard'
	try:
		u = UrlOnion.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "url deleted")

	except table_user.DoesNotExist:
		messages.error(request, "url does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)


@staff_member_required
@login_required
def del_urls_edit(request, pk):
	template_name = 'VigilantOnion:all_urls'
	try:
		u = UrlOnion.objects.get(pk=pk)
		u.delete()
		return redirect(template_name)
		messages.sucess(request, "url deleted")

	except table_user.DoesNotExist:
		messages.error(request, "url does not exist")
		return render(request, template_name)

	except Exception as e:
		messages.error(request, 'Something went wrong')
		return render(request, template_name)

	return render(request, template_name)



def search(request):
	if request.method == 'GET':
		query= request.GET.get('q')

		found_entries = request.GET.get('submit')

		if query is not None:
			lookups= Q(url__icontains=query) | Q(status__icontains=query)

			resultados = UrlOnion.objects.filter(lookups).distinct()


			cont_result = len(resultados)

			paginator = Paginator(resultados, 20)
			page = request.GET.get('page', 1)
			resultado = paginator.get_page(page)

			context={'resultado': resultado,
					 'found_entries': found_entries,
					 'query': query,
					 'cont_result': cont_result}

			return render(request, 'base/search.html', context)

		else:
			return render(request, 'base/search.html')

	else:
		return render(request, 'base/search.html')
