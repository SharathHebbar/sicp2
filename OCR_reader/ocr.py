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
    tts.save("YourFileName.mp3")
    
    
    

# Change the image directory to your's
detect_text("/Users/movingkyu/Desktop/work.png")

# To play your audio file that you saved
# Go to the terminal and type following command:

### os.system("mpg321 YourFileName.mp3") ###
