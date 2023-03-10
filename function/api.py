import os
import openai

import sys
import valiable

openai.organization = valiable.YOUR_ORG_ID
openai.api_key = valiable.OPENAI_API_KEY

# Get response from GPT
def get_response(messenge):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=messenge,
    temperature=0,
    max_tokens=600,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  print(response)
  return response["choices"][0]["text"]
