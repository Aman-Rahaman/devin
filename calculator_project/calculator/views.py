from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calculate(request):
    data = json.loads(request.body)
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return JsonResponse({'error': 'Division by zero'}, status=400)
        result = num1 / num2

    return JsonResponse({'result': result})
    
