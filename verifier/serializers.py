from rest_framework import serializers
from verifier.models import Signature

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'  

import cv2
from django.shortcuts import render
from verifier.forms import SignatureVerificationForm
from skimage.metrics import structural_similarity as ssim

def upload_and_verify(request):
    if request.method == 'POST':
        form = SignatureVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            # Get uploaded images from form
            image1 = form.cleaned_data['image1']
            image2 = form.cleaned_data['image2']
            
            # Process uploaded images
            # Assuming images are stored in the media directory
            img1_path = image1.path
            img2_path = image2.path
            
            # Read images using OpenCV
            img1 = cv2.imread(img1_path)
            img2 = cv2.imread(img2_path)
            
            # Compute similarity metric (e.g., SSIM)
            # Example: ssim = compute_ssim(img1, img2)
            # You need to implement compute_ssim function using OpenCV or other libraries
            
            # Display result based on similarity metric
            # For simplicity, we'll just render a template with the similarity metric
            return render(request, 'verification_success.html', {'ssim': ssim})
    else:
        form = SignatureVerificationForm()
    return render(request, 'upload.html', {'form': form})
