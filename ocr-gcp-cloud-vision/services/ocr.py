"""
Author: Anmol Krishan Sachdeva (greatdevaks)

About the Module:
Module for implementing simple Nitric-based APIs for
a mock OCR use-case which uses the GCP Cloud Vision API.

About OCR:
OCR (Optical Character Recognition) enables a user
to detect and extract text from images and documents.

User Journeys (exposed API operations):
1. A user should be able to create their user profile.
2. A user should be able to retrieve details of their user profile.
3. A user should be able to upload an image (single, for demo purposes).
The image upload API should only work for users who have their
user profiles created.
4. A user should be able to retrieve the text corresponding to the
uploaded image; OCR is applied on the image to retrieve text from the image.

Where to Run:
This Nitric-powered Python application can be run on any supported
provider (AWS, GCP, Azure, etc.). However, since the application makes
use of the GCP Cloud Vision API, having access to the same is necessary.
If extending from this codebase, the GCP Cloud Vision API could be replaced
by the OCR API of choice.

Disclaimer:
This codebase is not production-ready and is meant
for demonstration purposes only. The codebase doesn't necessarily
cover API design and security best practices.
"""

from uuid import uuid4

from nitric.application import Nitric
from nitric.context import HttpContext
from nitric.resources import api, kv

# Create a Nitric-powered API for the mock OCR use-case.
ocr_api = api("ocr-api")

# Create a Nitric-powered Key-Value Store for storing users'
# profiles and related metadata.
# Also, define the IAM permission categories for the permissions
# which the Python application should be having to the Key-Value
# Store; 'get' and 'set' permissions have been given for the
# 'user_profiles' Key-Value Store.
user_profiles = kv("user_profiles").allow("get", "set")


@ocr_api.post("/profiles")
async def create_user_profile(ctx: HttpContext) -> None:
    """
    A POST API to create a user's profile and store
    it in a Key-Value store.

    Args:
        ctx (HttpContext): HTTP Request and Response context for the API.
    """
    # Generate a unique profile id for the user.
    user_profile_id = str(uuid4())

    # Initialize a set of JSON keys which should be present in the
    # HTTP Request Payload.
    required_json_payload_keys = {"name", "age", "city"}

    # If HTTP Request JSON Payload is not empty, proceed with user profile
    # creation.
    if ctx.req.json is not None:
        # Check the difference between the desired HTTP Request JSON Payload
        # keys and the ones sent over the actual HTTP Request.
        missing_json_payload_keys = required_json_payload_keys - set(ctx.req.json)

        # If any required keys are missing in the HTTP Request JSON Payload,
        # return an HTTP 400 Bad Request response.
        if missing_json_payload_keys:
            ctx.res.status = 400
            ctx.res.body = {
                "msg": f"Bad Request. Missing required keys: {missing_json_payload_keys}."
            }
            return
    else:
        # Return an HTTP 400 Bad Request response.
        ctx.res.status = 400
        ctx.res.body = {
            "msg": f"Bad Request. Missing required keys: {required_json_payload_keys}."
        }
        return

    # Store the user profile details in the Key-Value Store.
    try:
        await user_profiles.set(
            user_profile_id,
            {
                "name": ctx.req.json["name"],
                "age": ctx.req.json["age"],
                "city": ctx.req.json["city"],
            },
        )

        # Return an HTTP 200 OK message telling that the creation of the user profile
        # happened successfully.
        ctx.res.body = {
            "msg": f"Profile with id '{user_profile_id}' created successfully."
        }
        return
    except Exception:
        # Return an HTTP 500 Internal Server Error response.
        ctx.res.status = 500
        ctx.res.body = {
            "msg": "An Internal Server Error happened. User profile creation failed."
        }
        return


@ocr_api.get("/profiles/:id")
async def get_user_profile(ctx: HttpContext) -> None:
    """
    A GET API to retrieve a user's profile details.

    Args:
        ctx (HttpContext): HTTP Request and Response context for the API.
    """
    # Get the profile id of the user from the HTTP Request.
    user_profile_id = ctx.req.params["id"]

    # Retrieve the details for the user's profile.
    try:
        profile_details = await user_profiles.get(user_profile_id)
        ctx.res.body = f"{profile_details}"
    except Exception:
        # Return an HTTP 500 Internal Server Error response.
        ctx.res.status = 500
        ctx.res.body = {
            "msg": "An Internal Server Error happened. User profile couldn't be fetched or doesn't exist."
        }
        return


Nitric.run()
