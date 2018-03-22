from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class Row1(MiddlewareMixin):
	def process_request(self,request):
		print('中间件1请求',request)
	def process_response(self,request,response):
		print('中间件1返回',request,'---',response)
		return response
	def process_view(self,request,callback,callback_args,callback_kwargs):
		print('中间件1view',request,'callback:',callback,'callback_args:',callback_args,'callback_kwargs:',callback_kwargs)

