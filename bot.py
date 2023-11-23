import openai
import os


openai.api_key = "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"

model_engine = "text-cordelia-001"

model_engine = "text-davinci-002"

prompt = "Привіт, як твої справи?"
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)
message = completions.choices[0].text
print(message)