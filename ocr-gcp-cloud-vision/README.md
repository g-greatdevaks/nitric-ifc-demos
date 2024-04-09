## Author
Anmol Krishan Sachdeva (greatdevaks)

## About the Module
Module for implementing simple Nitric-based APIs for a mock OCR use-case which uses the GCP Cloud Vision API.

## About OCR
OCR (Optical Character Recognition) enables a user to detect and extract text from images and documents.

## User Journeys (exposed API operations)
1. A user should be able to create their user profile.
2. A user should be able to retrieve details of their user profile.
3. A user should be able to upload an image (single, for demo purposes). The image upload API should only work for users who have their user profiles created.
4. A user should be able to retrieve the text corresponding to the uploaded image; OCR is applied on the image to retrieve text from the image.

## Where to Run
This Nitric-powered Python application can be run on any supported provider (AWS, GCP, Azure, etc.). However, since the application makes use of the GCP Cloud Vision API, having access to the same is necessary. If extending from this codebase, the GCP Cloud Vision API could be replaced by the OCR API of choice.

## Disclaimer
This codebase is not production-ready and is meant for demonstration purposes only. The codebase doesn't necessarily cover API design and security best practices.