import openai
from colorama import Fore, Style

key = ""
openai.api_key = key

# TODO: ADD CUSTOM GPT PROMPTS
summary_prompt="This is a raw transcript of words. Write down the key topics discussed in this transcript, as well as the major points made."

def process_file(audio_file, audio_prompt):

    transcript = call_whisper_api(audio_file, audio_prompt)
    summary = call_completion_api(transcript, summary_prompt)

    return summary

def call_whisper_api(audio_file, prompt):

    print(Style.BRIGHT + Fore.BLUE + "Calling Whisper API..." + Style.RESET_ALL)
    try:
        response = openai.Audio.transcribe(model="whisper-1", file=audio_file, language="en", prompt=prompt)
        print(Style.BRIGHT + Fore.GREEN + "Whisper API call successful!" + Style.RESET_ALL)
        return response['text']
    except openai.error.APIError as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API returned an API Error: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.APIConnectionError as e:
        print(Style.BRIGHT + Fore.RED + f"Failed to connect to OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.RateLimitError as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API request exceeded rate limit: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.Timeout as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API request timed out: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.InvalidRequestError as e:
        print(Style.BRIGHT + Fore.RED + f"Invalid request to OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.AuthenticationError as e:
        print(Style.BRIGHT + Fore.RED + f"Authentication error with OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.ServiceUnavailableError as e:
        print(Style.BRIGHT + Fore.RED + f"Service unavailable on OpenAI API: {e}" + Style.RESET_ALL)
        exit()


def call_completion_api(transcript, sum_prompt):

    print(Style.BRIGHT + Fore.BLUE + "Calling GPT API..." + Style.RESET_ALL)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": sum_prompt},
                {"role": "user", "content": transcript},
            ]
        )
        content = response['choices'][0]['message']['content']
        print(Style.BRIGHT + Fore.GREEN + "GPT API call successful!" + Style.RESET_ALL)
        return content
    except openai.error.APIError as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API returned an API Error: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.APIConnectionError as e:
        print(Style.BRIGHT + Fore.RED + f"Failed to connect to OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.RateLimitError as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API request exceeded rate limit: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.Timeout as e:
        print(Style.BRIGHT + Fore.RED + f"OpenAI API request timed out: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.InvalidRequestError as e:
        print(Style.BRIGHT + Fore.RED + f"Invalid request to OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.AuthenticationError as e:
        print(Style.BRIGHT + Fore.RED + f"Authentication error with OpenAI API: {e}" + Style.RESET_ALL)
        exit()
    except openai.error.ServiceUnavailableError as e:
        print(Style.BRIGHT + Fore.RED + f"Service unavailable on OpenAI API: {e}" + Style.RESET_ALL)
        exit()

