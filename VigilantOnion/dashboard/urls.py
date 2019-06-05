from django.conf.urls import include, url
# importando o processo de login e logout padrão do django
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
# Fazendo importação das views do app dashboard
from .views import *

app_name = 'VigilantOnion'

urlpatterns = [
	url(r'^$', user_login , name='login'),
	url(r'^$', dashboard , name='dashboard'),
	url(r'^user/logout/$', logoutUser , name='logout'),
	url(r'^register/url/$', registerurl, name='newurl'),
	url(r'^register/url/(?P<pk>\d+)/delete/$', del_urls, name='del_urls'),
	url(r'^all/url/(?P<pk>\d+)/delete/$', del_urls_edit, name='del_urls_edit'),
	url(r'^register/source/$', registersource, name='registersource'),
	url(r'^register/source/(?P<pk>\d+)/delete/$', del_source, name='del_source'),
	url(r'^edit/source/(?P<pk>\d+)/$', edit_source, name='edit_source'),
	url(r'^register/category/$', registercategory, name='newcategory'),
	url(r'^register/category/(?P<pk>\d+)/delete/$', del_category, name='del_category'),
	url(r'^register/category/term/$', registerterm, name='newterm'),
	url(r'^register/category/term/(?P<pk>\d+)/delete/$', del_category_term, name='del_category_term'),
	url(r'^register/company/$', registercompany, name='newcompany'),
	url(r'^register/company/(?P<pk>\d+)/delete/$', del_company, name='del_company'),
	url(r'^register/company/keyword/$', registerkeyword, name='newkeyword'),
	url(r'^register/company/keyword/(?P<pk>\d+)/delete/$', del_keyword, name='del_keyword'),
	url(r'^edit/urls/(?P<pk>\d+)/$', urls_detail, name='editurls'),
	url(r'^edit/category/(?P<pk>\d+)/$', category, name='editcategory'),
	url(r'^edit/category/term/(?P<pk>\d+)/$', category_term, name='editcategoryterm'),
	url(r'^edit/company/(?P<pk>\d+)/$', company_category, name='editcompany'),
	url(r'^edit/company/term/(?P<pk>\d+)/$', company_category_term, name='editcompanyterm'),
	url(r'^users/register/$', register_user, name='registrar'),
	url(r'^users/all/$', all_users, name='all_users'),
	url(r'^users/all/(?P<pk>\d+)/delete/$', del_user, name='del_user'),
	url(r'^users/edit/(?P<pk>\d+)/$', user_detail, name='user_edit'),
	url(r'^all/urls/$', all_urls, name='all_urls'),
	url(r'^search/$', search, name='search')


]
