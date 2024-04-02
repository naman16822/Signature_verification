from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from verifier.models import Signature
from verifier.serializers import SignatureSerializer

@api_view(['POST'])
def verify_signature(request):
    print('Hello')
    serializer = SignatureSerializer(data=request.data)
    if serializer.is_valid():
        signature = serializer.save()
        signature.verified = True
        signature.verified_by = "Admin" 
        signature.save()
        return Response(request, 'verification_success.html', {'serializer': serializer})
    else:
        return Response(request,'verification_failure.html', {'errors': serializer.errors})
def verify_signature(request):
    context = {
        'request': request
    }
    return render(request, 'verify_signature.html', context)

def upload_view(request):
    if request.method == 'POST':
        for file_field_name, file_obj in request.FILES.items():
            pass
        return render(request, 'upload_success.html')
    else:
        return render(request, 'upload.html')
    


