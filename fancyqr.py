import os
import streamlit as st
import replicate

# https://replicate.com/dannypostma/cog-visual-qr/api#input-qr_code_content (Inputs here)


os.environ['REPLICATE_API_TOKEN'] = 'r8_Hzixefvl3Q2m4Q10XWqRevgSKcVrqSD1PdjmP'

output = replicate.run(
    "dannypostma/cog-visual-qr:7653601d0571fa6342ba4fa93a0962adebd1169e9e2329eefeb5729cac645d42",
    input={"qr_code_content": "https://www.headshotpro.com"}
)
# print(output)

# st.write('Lets make a QR app')
# st.image(output)

header = st.container()
body = st.container()

with header:
    st.title("Fancy QR Codes")
    st.write("Create a Fancy QR Code for your business. Help your QR codes stand out!")

with body:
    col1, col2 = st.columns(2)
    col1.write("Let's display the input options here")
    col2.write("Let's display the resultant image here")

