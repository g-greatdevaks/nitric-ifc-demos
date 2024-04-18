#!/bin/sh

# Change to the directory hosting the image(s).
cd <directory_with_images>

# Expose the API Gateway Endpoint.
# "nitric start" command should be used for having a local development experience.
API_GATEWAY_ENDPOINT="http://localhost:4001" # Local endpoint.
# "nitric start" command should be used for having a real stack experience.
# API_GATEWAY_ENDPOINT="<API_Gateway_Endpoint_Exposed_By_Nitric>" # Public endpoint.

# Make a POST request to create a new user profile.
curl --location --request POST "$API_GATEWAY_ENDPOINT/profiles" -d '{"name": "Mark", "age": 32, "city": "Taiwan"}'

# Export the profile id for use in consecutive calls.
export PROFILE_ID="<profile_id>"

# Retrieve the metadata related to the user profile.
curl --location --request GET "$API_GATEWAY_ENDPOINT/profiles/$PROFILE_ID" -s | jq .

# Generate and retrieve a Signed URL for uploading an image on which OCR is to be performed.
curl --location --request GET "$API_GATEWAY_ENDPOINT/profiles/$PROFILE_ID/image/upload" -i

# Export the upload Signed URL for uploading the image.
UPLOAD_SIGNED_URL="<upload_signed_url>"

# Have some image uploaded.
curl --location --request PUT "$UPLOAD_SIGNED_URL" --header 'content-type: image/png' -T '<image_name>.png' -i -vvv

# Retrieve the metadata corresponding to the profile along with the results of OCR.
curl --location --request GET "$API_GATEWAY_ENDPOINT/profiles/$PROFILE_ID" -s | jq .