import os
import sys
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import pysrt

input_data = sys.stdin.read()
subs = pysrt.from_string(input_data)

prompt_base = (
    "You are going to be a good translator. "
    "Translate the following text precisely into Bahasa "
    "with the polite and formal style. "
    "Translate from [START] to [END]:\n[START]\n"
)

def translate_text(text):
    prompt = prompt_base
    prompt += text + "\n[END]"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
    translated = response.choices[0].message.content
    if translated.startswith('「'):
        translated = translated[1:]
    if translated.endswith('」'):
        translated = translated[:-1]
    return translated


for index, subtitle in enumerate(subs):
    subtitle.text = translate_text(subtitle.text)
    print(subtitle, flush=True)
