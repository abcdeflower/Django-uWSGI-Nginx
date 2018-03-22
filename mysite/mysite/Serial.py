from django.db import models
from django.db.models import manager
from django.db.models.query import QuerySet
from django.db.models.fields.files import ImageFieldFile,FileField

class Serializer(object):
	include_attr=[]
	exclude_attr=[]
	objects=[]
	origin_data=None
	output_type='raw'
	datetime_format='timestamp'
	foreign=False
	many=False
	
	def __init__(self,data,datetime_format='timestamp',output_type='raw',include_attr=None,exclude_attr=Node,
			foreign=False,many=False,*args,**kwargs):
		if include_attr:
			self.include_attr=include_attr
		if exclude_attr:
			self.exclude_attr=exclude_attr
		self.origin_data=data
		self.output_type=output_type
		self.foreign=foreign
		self.many=many
		self.datetime_format=datetime_format
		self._dict_check=kwargs.get('dict_check',False)
	def chech_attr(self,attr):
		if self.exclude_attr and attr in self.exclude_attr:
			return False
		if self.include_attr and attr in self.include_attr:
			return False
		return True

	def data_inspect(self,data):
		if isinstance(data,(QuerySet)):
			convert_data=[]
			for obj in data:
				convert_data.append(self.data_inspect(obj))
			return convert_data
		elif isinstance(data,models.Model):
			obj_dict={}
			concrete_model=data._meta.concrete_model
			for field in concrete_model._meta.local_fields:
				if self.chech_attr(field.name) and self.foreign:
					obj_dict[field.name]=self.data_inspect(getattr(data,field.name))
			for field in concrete_model._meta.many_to_many:
				if self.chech_attr(field.name) and self.many:
					obj_dict[field.name]=self.data_inspect(getattr(data,field.name))
			for k,v in data.__dict__.iteritems():
				if not unicode(k).startswith('_') and k not in obj_dict.keys() and self.chech_attr(k):
					obj_dict[k]=self.data_inspect(v)
			return obj_dict
		elif isinstance(data,manager.Manager):
			
