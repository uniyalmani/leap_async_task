from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .tasks import fetch_fact
from .models import CatFact


@api_view(['GET'])
def health_check(request):

    return Response(data={"message": "application is running"} , status=status.HTTP_200_OK)


@api_view(['GET'])
def fetch_fact_view(request):
    try:
        message = fetch_fact.send()
        return Response(data={'success': True})
    except Exception as e:
        return Response({'success': False, 'error': str(e)})
    
    
@api_view(['GET'])
def get_fact(request):
    try:
        fact = CatFact.objects.order_by('-fetched_at').first()
        if fact:
            return Response({'fact': fact.text, "user_id": fact.user_id, "fetched_at": fact.fetched_at})
        else:
            return Response({'error': 'no_task_has_been_queued_yet'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)