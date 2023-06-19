import os
import streamlit as st
import replicate

from PIL import Image

# https://replicate.com/dannypostma/cog-visual-qr/api#input-qr_code_content (Inputs here)


# os.environ['REPLICATE_API_TOKEN'] = 'r8_Hzixefvl3Q2m4Q10XWqRevgSKcVrqSD1PdjmP'
os.environ['REPLICATE_API_TOKEN'] = 'r8_NEGDOdeM8jkd3xjnCE5SuwnSRpJraW24CE5nZ'




header = st.container()
body = st.container()

image = Image.open("output.png")


# st.sidebar.image(image, width=100)
with st.sidebar:
    st.subheader("Settings")
    # st.write("Create beautiful QR codes for your business using AI. Help your QR codes stand out!")

    url = st.text_input('Your landing page (URL)', placeholder='https://www.google.com/')

    prompt = st.text_input('Prompt for AI', value='Gorgeous romantic sunset, cliffside onlooking the beautiful city of new york, warm colors, in the style of hiroshi nagai, very detailed, 8 0 s')

    neg_prompt = st.text_input('negative_prompt', value='ugly, disfigured, low quality, blurry, nsfw')

    

    create_button = st.button("Create")


with header:
    logo, rest, unused = st.columns(3)
    logo.image(image, width=100)
    rest.title("Design QR")
    unused.write("Create beautiful QR codes for your business using AI. Help your QR codes stand out!")

with body:
    col1, col2 = st.columns(2)
    
    
    # col1.subheader("Design your QR code")

    if create_button:
        inputData = {
                "qr_code_content": url,
                "prompt": prompt,
                "negative_prompt": neg_prompt,
                "guidance_scale": 20,
                "conditioning_scale": 2,
                "strength": 0.8,
                "seed": 1594771627,
                "num_inference_steps": 40
                }
        col1.subheader("Your selected configuration")
        col1.write(f'URL: {inputData["qr_code_content"]}')
        col1.write(f'Prompt: {inputData["prompt"]}')
        col1.write(f'Negative Promp: {inputData["negative_prompt"]}')
        col1.write(f'Guidance Scale: {inputData["guidance_scale"]}')
        col1.write(f'Conditioning Scale: {inputData["conditioning_scale"]}')
        col1.write(f'Strength: {inputData["strength"]}')
        col1.write(f'Seed: {inputData["seed"]}')
        col1.write(f'Inference Steps: {inputData["num_inference_steps"]}')
        col2.subheader("Your Result")
        output = replicate.run(
            "dannypostma/cog-visual-qr:7653601d0571fa6342ba4fa93a0962adebd1169e9e2329eefeb5729cac645d42",
            input=inputData
        )

        col2.image(output)

        # col2.download_button("Download", output)
        link = f'[Download image]({output})'
        col2.markdown(link, unsafe_allow_html=True)


    col2.write("Your results will appear here")
