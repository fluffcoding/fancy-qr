import os
import streamlit as st
import replicate

from PIL import Image

# https://replicate.com/dannypostma/cog-visual-qr/api#input-qr_code_content (Inputs here)


# os.environ['REPLICATE_API_TOKEN'] = 'r8_Hzixefvl3Q2m4Q10XWqRevgSKcVrqSD1PdjmP'
os.environ['REPLICATE_API_TOKEN'] = 'r8_NEGDOdeM8jkd3xjnCE5SuwnSRpJraW24CE5nZ'


# output = replicate.run(
#     "dannypostma/cog-visual-qr:7653601d0571fa6342ba4fa93a0962adebd1169e9e2329eefeb5729cac645d42",
#     input={"qr_code_content": "https://www.headshotpro.com"}
# )
# print(output)

# st.write('Lets make a QR app')
# st.image(output)

header = st.container()
body = st.container()

image = Image.open("output.png")


# st.sidebar.image(image, width=100)
with st.sidebar:
    st.subheader("Settings")
    # st.write("Create beautiful QR codes for your business using AI. Help your QR codes stand out!")

    st.text_input('Your landing page (URL)', placeholder='https://www.google.com/')

    st.write('qr.prompt')

    st.text_input('Prompt for AI', value='Gorgeous romantic sunset, cliffside onlooking the beautiful city of new york, warm colors, in the style of hiroshi nagai, very detailed, 8 0 s')

    st.text_input('negative_prompt', value='ugly, disfigured, low quality, blurry, nsfw')

    guidance_scale = 20
    conditioning_scale = 2
    strength = 0.8
    seed= 1594771627
    num_inference_steps = 40

    

    # st.write('guidance_scale')

    # st.write('conditioning scale')

    # st.write('strength')
    
    # st.write('seed')

    # st.write('num_inference_steps')

    # st.write('init_image')


with header:
    logo, rest, unused = st.columns(3)
    logo.image(image, width=100)
    rest.title("Design QR")
    unused.write("Create beautiful QR codes for your business using AI. Help your QR codes stand out!")

with body:
    col1, col2 = st.columns(2)
    
    
    # col1.subheader("Design your QR code")




    col2.write("Let's display the resultant image here")

