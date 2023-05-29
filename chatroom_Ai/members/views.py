import os
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import ChatMessage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('api_key')

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        # Store the user message
        ChatMessage.objects.create(message=message)

        # Generate a response using ChatGPT
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=message,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
        )

        response_text = response.choices[0].text.strip()

        # Store the ChatGPT response
        ChatMessage.objects.create(message=response_text)

        return JsonResponse({'response': response_text})

    return render(request, 'index.html')


def signup(request):
  return render(request, 'signup.html')

def signin(request):
  return render(request, 'signin.html')

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())