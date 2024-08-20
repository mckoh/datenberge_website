"""
Dynamic Content
Author: Michael Kohlegger
Date: 2024-08-19
"""

import streamlit as st
from time import sleep
import numpy as np


TITLE = "Michael Kohlegger"
ICON = "🚀"
LOGO_PATH = "static/logo.png"
ICON_PATH = "static/icon.png"


st.set_page_config(
    page_title=TITLE,
    page_icon=ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# st.logo(LOGO_PATH, icon_image=ICON_PATH)

# #####################################################################


iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)
progress_bar = st.sidebar.progress(0)
frame_text = st.sidebar.empty()

col1, col2, col3 = st.columns(3)

with col1:
    image = st.empty()

with col2:
    st.title("Michael Kohlegger")
    st.markdown(
        """
        Professor, data scientist and developer affiliated with ...

        * Management Center Innsbruck
        * University of Applied Sciences Kufstein
        * University of Innsbruck

        [Book a 30 Minutes virtual meeting with me.](https://calendly.com/michael-kohlegger/30min)
        """
    )

m, n, s = 960, 640, 400
x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

while True:
    for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):

        progress_bar.progress(frame_num)
        frame_text.text(f"Frame {frame_num}/99")

        c = separation * np.exp(1j * a)
        Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
        C = np.full((n, m), c)
        M = np.full((n, m), True, dtype=bool)
        N = np.zeros((n, m))

        for i in range(iterations):
            Z[M] = Z[M] * Z[M] + C[M]
            M[np.abs(Z) > 2] = False
            N[M] = i

        image.image(1.0 - (N / N.max()), use_column_width=True)
