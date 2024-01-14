import os
from openai import OpenAI
import sys

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
video_id = sys.argv[1]
audio_file_path = os.path.join(os.getcwd(), 'tmp', video_id + '.m4a')

audio_file = open(audio_file_path, 'rb')
transcript = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1",
    response_format="srt",
    prompt="I am a programmer. My name is Husni. This is a vlog about my app development"
)
print(transcript)
