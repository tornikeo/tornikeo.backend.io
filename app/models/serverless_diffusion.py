from symbol import arglist
from pandas import notna
import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image
import os

def run(prompt: str, 
        num_inference_steps = 50,
        guidance_scale=9,
        height=512,
        width=512,
        seed=3242) -> Image:
    # Just grab all args, works for now    
    model_inputs = dict(locals())

    api_key = os.getenv("BANANA_API_KEY")
    model_key = os.getenv("BANANA_SD_MODEL_KEY")
    assert api_key is not None, "API key is missing from environment. Aborting."

    # Run the model
    out = banana.run(api_key, model_key, model_inputs)

    # Extract the image and save to output.jpg
    image_byte_string = out["modelOutputs"][0]["image_base64"]
    image_encoded = image_byte_string.encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(image_encoded)))
    return image

if __name__ == "__main__":
    model_inputs = {
        "prompt": "table full of muffins",
        "num_inference_steps":50,
        "guidance_scale":9,
        "height":512,
        "width":512,
        "seed":3242
    }

    api_key = os.getenv("BANANA_API_KEY")
    model_key = os.getenv("BANANA_SD_MODEL_KEY")
    assert api_key is not None, "API key is missing from environment. Aborting."

    # Run the model
    out = banana.run(api_key, model_key, model_inputs)

    # Extract the image and save to output.jpg
    image_byte_string = out["modelOutputs"][0]["image_base64"]
    image_encoded = image_byte_string.encode('utf-8')
    image_bytes = BytesIO(base64.b64decode(image_encoded))
    image = Image.open(image_bytes)
    image.save("output.jpg")
