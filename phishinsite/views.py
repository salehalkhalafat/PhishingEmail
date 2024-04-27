from django.shortcuts import render
from .listen import massagelisten
from django.http import JsonResponse
from data.models import EMAILS

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def HomePage(request):
    emails = EMAILS.objects.filter(isfishing=False)
    context = {'emails': emails}
    return render(request, 'mail.html', context)


def phishingPage(request):
    emails = EMAILS.objects.filter(isfishing=True)
    context = {'emails': emails}
    return render(request, 'phishingbox.html', context)


def seperate(request):
    data = massagelisten()
    response_data = {
        "status": bool(len(data) > 0),
        "data": data,
    }
    return JsonResponse(response_data)


@api_view(['POST'])
def add_email(request):
    email = request.data.get('email')
    subject = request.data.get('subject')
    body = request.data.get('body')
    if email and subject and body:
        EMAILS.objects.create(email=email, subject=subject, body=body)
        return Response({'status': 'success', 'message': 'Email details added successfully'},
                        status=status.HTTP_201_CREATED)
    else:
        return Response({'status': 'error', 'message': 'All fields (email, subject, body) are required'},
                        status=status.HTTP_400_BAD_REQUEST)
