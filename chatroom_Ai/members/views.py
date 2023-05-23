from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member, ChatMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import openai

openai.api_key = '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'

def members(request):
  if request.method == 'POST':
    message = request.POST.get('message')

    ChatMessage.objects.create(message=message)

def signup(request):
  return render(request, 'signup.html')

def signin(request):
  return render(request, 'signin.html')


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())