
from django.http import HttpResponse
import datetime,json
from django.views.generic.base import View,TemplateView
from django.views.generic import DetailView,ListView
from books.models import Book,Author
from django.db import models
from django.db.models import manager
from django.db.models.query import QuerySet

def current_datetime(request):
	now=datetime.datetime.now()
	html="<html><body>It is now %s.</body></html>"%now
	return HttpResponse(html)

class Date_Minin(object):
	def get(self,request,*args,**kwargs):
		print('in get()')
		return super(Date_Minin,self).get(request,*args,**kwargs)
class Date_Minin1(object):
	def get(self,request,*args,**kwrgs):
		print('in Date_Minin1 get')
		return super(Date_Minin1,self).get(request,*args,**kwrgs)
class Date_Minin2(object):
	def get1(self):
		print('in Date_Minin2 get')
		return True
class Detail_View(DetailView):
	pid='pid'
	html="<html><body>it is now :%s.</body></html>"%pid
	def get(self,request,*args,**kwargs):
		print(request,args,kwargs)
		html1="<body>%s,%s</body>"%(kwargs,args)
		return HttpResponse(html1)
	def get_queryset(self,*args):
		print(args)
class Date_View(View):#(Date_Minin,Date_Minin2,DetailView):
	now=datetime.datetime.now()
	html="<html><body>it is now :%s.</body></html>"%now
	def get(self,request,*args,**kwargs):
		print('in get_object()')
		data=Author.objects.all()

		print(data)
		#return HttpResponse(self.html)
		return HttpResponse(json.simplejson.dumps(list(data)),content_type='application/json',**kwargs)
class Serial():
#	def __init__(self,data):
#		self.data=data
	def data_inspct(self,data):
		print('models',models.Model)
		if isinstance(data,models.Model):
			obj_dict={}
			concrete_model=data._meta.concrete_model
			print(concrete_model)
			for field in concrete_model._meta.local_fields:
				obj_dict[field.name]
		elif isinstance(data,QuerySet):
			print('QuerySet')
			convert_data=[]
			for obj in data:
				convert_data.append(self.data_inspct(obj))
			return convert_data
		elif isinstance(data,manager.Manager):
			print('manager')
		else:
			print('aaa')
	def __call__(self,data):
		self.data=data
		self.object=self.data_inspct(self.data)

class Temp_View(TemplateView):
	template_name='home.html'
	def get_context_data(self,**kwargs):
		context=super(Temp_View,self).get_context_data(**kwargs)
		context['arthor']=Author.objects.all()
		return context
	'''
	def dispatch(self,request,*args,**kwargs):
		print('dispatch in')
		obj=super(Date_View,self).dispatch(request,*args,**kwargs)
		print(obj)
		print('dispath out')
		return obj
	def get(self,request,*args,**kwagrs):
		return super(Date_View,self).get(request,*args,**kwagrs)# HttpResponse(self.html)
	'''
