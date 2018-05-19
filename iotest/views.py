# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse,HttpResponse
import json

def keyboard(request):

	return JsonResponse({
                'type' : 'buttons',
		'buttons' : ['카메라','온도','습도']
})


