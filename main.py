from startup import startup
import asyncio

def run_metagpt(request):
    # Parse the input from the cloud function event data (assuming it's a JSON payload)
    request_json = request.get_json()
    if request_json and 'idea' in request_json:
        idea = request_json['idea']
    else:
        return "Error: 'idea' parameter missing in the request."

    # Call the GPT-4 API to generate content
    asyncio.run(startup(idea))

    # Save the generated content to a Cloud Storage bucket (you can do this within the startup function)

    # Return a success response
    return "Content generation completed successfully."