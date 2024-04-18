## Project Description

An example for implementing simple Nitric-based APIs for a mock OCR use-case which uses the Google Cloud Vision API.

## About OCR

OCR (Optical Character Recognition) enables a user to detect and extract text from images and documents.

## User Journeys (exposed API operations)

1. A user should be able to create their user profile.
2. A user should be able to retrieve details of their user profile. No security patterns like Authorization, Authentication, Identification, etc. have been enforced as the shown APIs are for demonstration purposes only. A sample (written in JavaScript) for security could be found at: [Secure APIs with Auth0](https://nitric.io/docs/guides/getting-started/nodejs/secure-api-auth0)
3. A user should be able to upload an image (single, for demo purposes). The image upload API should only work for users who have their user profiles created.
   Note: No Authorization, Authentication, Identification, etc. patterns have been applied and the request is validated just based on the correct UUID (for user profile).
4. A user should be able to retrieve the text corresponding to the uploaded image; OCR is applied on the image to retrieve text from the image. The detected text is uploaded to the user's profile metadata and the same should be retrievable from the API that returns a user's profile information based on the UUID supplied.

## Where to Run

This Nitric-powered Python application can be run on any supported provider (AWS, GCP, Azure, etc.). However, since the application makes use of the Google Cloud Vision API, having access to the same is necessary (and a pre-requisite for this demo). If extending from this codebase, the Google Cloud Vision API could be replaced by the OCR API of choice.

## Usage / Demo

### Step 1: Install Nitric

- Follow the steps outlined in the official Nitric [installation guide](https://nitric.io/docs/installation).
- Make sure that Docker is installed and functional on the host from where the Nitric stack is going to be brought up.
- Also make sure to have `PULUMI_ACCESS_TOKEN` exposed (`pulumi login` can be used [pulumi login](https://www.pulumi.com/docs/cli/commands/pulumi_login/).
  - Details around Pulumi can be even found in one of the (my) talks delivered [Achieving Ultimate Infrastructure Automation Using Pulumi and Python](https://github.com/g-greatdevaks/automation-days-asia-2023-pulumi).

### Step 2: Clone this repository and get into the directory

```
git clone https://github.com/g-greatdevaks/nitric-ifc-demos.git
cd nitric-ifc-demos
```

### Step 3: Move to the Application Codebase and configure the stack file

```
cd ocr-gcp-cloud-vision
vim nitric.gcp-mock.yaml # This could be for the supported cloud provider of choice.
```

### Step 4: Run the Nitric project locally

```bash
pipenv install --dev
nitric start
```

### Step 5: Try out OCR Application's APIs locally

Refer [commands.sh](ocr-gcp-cloud-vision/commands.sh) file for step-by-step execution sequence.

### Step 6: Run the Nitric project on GCP

```bash
nitric stack update -s gcp-mock
```

### Step 7: Try out the publicly deployed OCR Application's APIs

Refer [commands.sh](ocr-gcp-cloud-vision/commands.sh) file for step-by-step execution sequence.

## Disclaimer

This codebase is not production-ready and is meant for demonstration purposes only. The codebase doesn't necessarily cover API design and security best practices.
