from django.shortcuts import render,render_to_response
from django.views.generic import DetailView,ListView
from django.template import RequestContext
import string,random

# Create your views here.
def login(request):
	print('in login')
	return render_to_response('login_form.html')
class LoginView(DetailView):
	def post(self,request,*args,**kwargs):
		print('in loginview')
		username=request.POST.get('username')
		password=request.POST.get('password')
		token=self.create_token()
		request.session['token']=token
		print('user:',username,'passwd:',password,'session:',request.session)
		return render_to_response('login_form.thml',token,context_instance=RequestContext(request))

	def get(self,request,*args,**kwargs):
		print('in loginview get')
		token=self.create_token()
		request.session['token']=token
		print('session:',dir(request.session.values))
	def create_token(self):
		return ''.join(random.sample('ZXVBNMASDFGHJKLQWERTYUIO0123456789zxcvbnmasdfghjklqwertyuiop',12)).replace(' ','')
