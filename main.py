import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = "--verbose" in sys.argv

    if len(sys.argv) < 2:
        print("Missing prompt")
        sys.exit(1)
    user_prompt = sys.argv[1]

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):

    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    for i in range(0, 20):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages, config=config,
        )

        if verbose:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")

        if not response.function_calls:
            print(f"Final answer: {response.text}")
            break

        for candidate in response.candidates:
            messages.append(candidate.content)

        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
            ):
                raise Exception("empty function call result")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])
        
        if function_responses:
            messages.append(types.Content(role="model", parts=function_responses))

main()