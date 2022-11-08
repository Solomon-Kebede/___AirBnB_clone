#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
	def __init__(self):
		"""Instantiate a new object with a
		unique id and the time of creation or
		update"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()


	def __str__(self):
		"""String method for object"""
		return '[{}] ({}) {}'.format(
			self.__class__.__name__,
			self.id,
			self.__dict__)


	def save(self):
		"""Update the public instance attrribute
		updated_at with current datetime"""
		self.updated_at = datetime.now()


	def to_dict(self):
		"""Returns a dictionary containing all
		keys/values of __dict__ of the instance"""
		new_dict = {}
		for key, value in self.__dict__.items():
			new_dict[key] = value
		new_dict['__class__'] = self.__class__.__name__
		new_dict['created_at'] = self.created_at.strftime(
			'%Y-%m-%dT%H:%M:%S.%f')
		new_dict['updated_at'] = self.updated_at.strftime(
			'%Y-%m-%dT%H:%M:%S.%f')
		return new_dict