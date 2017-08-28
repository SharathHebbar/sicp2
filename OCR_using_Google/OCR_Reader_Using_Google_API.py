from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()

import argparse
import io

from google.cloud import vision
from google.cloud.vision import types


def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print(texts[0].description)
    from gtts import gTTS
    import os
    tts = gTTS(text=texts[0].description, lang='en')
    tts.save("plzwork.mp3")
    os.system("mpg321 plzwork.mp3")

#import sys
#filepath = sys.argv[-1]

detect_text("/home/pi/Desktop/ocr/OCR_using_Google/work.png")
