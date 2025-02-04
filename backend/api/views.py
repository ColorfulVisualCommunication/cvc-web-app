from django.http import JsonResponse

# Create your views here.
# Define a function-based view called home that takes a request object as an argument


def home(request):
    return JsonResponse({'message':'Welcome to the CVC API! @successfully connected!'}) # Return a JSON response with a welcome message