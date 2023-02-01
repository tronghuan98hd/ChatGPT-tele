import os
import openai
OPENAI_API_KEY = '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'
YOUR_ORG_ID = 'org-oC1BMaxw1MIvkjxTFmJ1pten'
openai.organization = YOUR_ORG_ID
openai.api_key = OPENAI_API_KEY


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

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="1 cộng 1 bằng mấy",
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

#print(get_response("1 cộng 1 bằng mấy"))

