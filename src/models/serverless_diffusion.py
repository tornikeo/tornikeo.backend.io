import banana_dev as banana
import base64
from io import BytesIO
from PIL import Image
import os
import gradio as gr
# from ratelimit import limits

# FIFTEEN_MINUTES = 900
# @limits(calls=15, period=FIFTEEN_MINUTES)
def run(prompt: str, 
        height=512,
        width=512,
        seed=3242,
        num_inference_steps=50,
        guidance_scale=9,
        ) -> Image.Image:
    # Just grab all args, works for now    
    model_inputs = dict(locals())

    api_key = os.getenv("BANANA_API_KEY")
    model_key = os.getenv("BANANA_SD_MODEL_KEY")
    assert api_key is not None, "API key is missing from environment. Aborting image generation. Contact the developer."

    # Run the model
    try:
        out = banana.run(api_key, model_key, model_inputs)
    except Exception as e:
        raise Exception(f'Backend GPU server call failed. Contact the developer. Error details: {e}')

    # Extract the image and save to output.jpg
    image_byte_string = out["modelOutputs"][0]["image_base64"]
    image_encoded = image_byte_string.encode('utf-8')
    image = Image.open(BytesIO(base64.b64decode(image_encoded)))
    return image

def gradio_app():
    io = gr.Interface(
        fn=run,
        inputs=[
            gr.components.Textbox("interior design, open plan, kitchen and living room, modular furniture with cotton textiles, wooden floor, high ceiling, large steel windows viewing a city.", 
                label="Please draw the following..."),
            gr.components.Slider(256, 512, 512, step=4, label='Image height'),
            gr.components.Slider(256, 512, 512, step=4, label='Image Width'),
            gr.components.Slider(0, 100, 13, label='Random initial seed'),
            gr.components.Slider(15, 50, 50, step=1, label='(Advanced) Number of diffusion steps (higher = more details)'),
            gr.components.Slider(1, 10, 9, step=1, label='(Advanced) Scale of diffusion steps (higher = more randomness)'),
        ], 
        outputs=[
            gr.components.Image(type='pil')
        ],
        # examples=[
        #     ["Big red apple on a branch of a tree.", 50, 0],
        #     ["A pair of modern NIKE shoes, with iridescent color.", 50, 0],
        # ],
        # cache_examples=True,
    )
    io.show_error = True
    return gr.routes.App.create_app(io)
    
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
