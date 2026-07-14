import streamlit as st

# Original SnapClass palette — used for both light and dark theme.
_PRIMARY = "#5865F2"
_HOME_BG = "#5865f2"
_LAVENDER = "#E0E3FF"
_ACCENT = "#EB459E"
_WHITE = "white"
_BLACK = "black"
_TEXT_DARK = "#1e293b"


def _theme_lock_css():
    """Strategy A + B + C: force the original palette in light and dark mode."""
    return f"""
        /* Strategy A: prefer light color-scheme at the document level */
        html, body, .stApp {{
            color-scheme: light only !important;
        }}

        /* Strategy B: remap Streamlit dark-theme variables to the original palette */
        .stApp[data-theme="dark"] {{
            --primary-color: {_PRIMARY};
            --background-color: {_LAVENDER};
            --secondary-background-color: {_WHITE};
            --text-color: {_TEXT_DARK};
        }}

        .stApp[data-theme="dark"],
        .stApp[data-theme="dark"] .main,
        .stApp[data-theme="dark"] [data-testid="stAppViewContainer"],
        .stApp[data-theme="dark"] [data-testid="stMainBlockContainer"] {{
            color: {_TEXT_DARK} !important;
        }}

        .stApp[data-theme="dark"] [data-testid="stWidgetLabel"] p,
        .stApp[data-theme="dark"] [data-testid="stCaption"],
        .stApp[data-theme="dark"] [data-testid="stCaption"] p {{
            color: {_BLACK} !important;
        }}

        .stApp[data-theme="dark"] input,
        .stApp[data-theme="dark"] textarea,
        .stApp[data-theme="dark"] [data-baseweb="select"] > div {{
            background-color: {_WHITE} !important;
            color: {_TEXT_DARK} !important;
            border-color: {_BLACK} !important;
        }}

        .stApp[data-theme="dark"] .stButton > button {{
            background-color: {_PRIMARY} !important;
            color: {_WHITE} !important;
        }}

        .stApp[data-theme="dark"] .stButton > button[kind="secondary"] {{
            background-color: {_ACCENT} !important;
            color: {_WHITE} !important;
        }}

        .stApp[data-theme="dark"] .stButton > button[kind="tertiary"] {{
            background-color: {_BLACK} !important;
            color: {_WHITE} !important;
        }}

        .stApp[data-theme="dark"] [data-testid="stDialog"] {{
            background-color: {_WHITE} !important;
            color: {_TEXT_DARK} !important;
        }}
    """


def style_background_home():

    st.markdown(
        f"""
        <style>
            {_theme_lock_css()}

            .stApp,
            .stApp[data-theme="dark"],
            .stApp[data-theme="light"] {{
                background: {_HOME_BG} !important;
            }}

            .stApp div[data-testid="stColumn"],
            .stApp[data-theme="dark"] div[data-testid="stColumn"],
            .stApp[data-theme="light"] div[data-testid="stColumn"] {{
                background-color: {_LAVENDER} !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():

    st.markdown(
        f"""
        <style>
            {_theme_lock_css()}

            .stApp,
            .stApp[data-theme="dark"],
            .stApp[data-theme="light"] {{
                background: {_LAVENDER} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            {_theme_lock_css()}

            #Margin, header {{
                visibility: hidden;
            }}

            .block-container {{
                padding-top: 1.5rem !important;
            }}

            h1 {{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }}

            h2 {{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: {_BLACK} !important;
            }}

            h3, h4, p {{
                font-family: 'Outfit', sans-serif !important;
                color: {_TEXT_DARK} !important;
            }}

            /* Strategy C: strengthened selectors for native widgets */
            button,
            .stButton > button {{
                border-radius: 1.5rem !important;
                background-color: {_PRIMARY} !important;
                color: {_WHITE} !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out;
            }}

            button[kind="secondary"],
            .stButton > button[kind="secondary"] {{
                border-radius: 1.5rem !important;
                background-color: {_ACCENT} !important;
                color: {_WHITE} !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out;
            }}

            button[kind="tertiary"],
            .stButton > button[kind="tertiary"] {{
                border-radius: 1.5rem !important;
                background-color: {_BLACK} !important;
                color: {_WHITE} !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out;
            }}

            button:hover,
            .stButton > button:hover {{
                transform: scale(1.05);
            }}

            [data-testid="stWidgetLabel"] p,
            [data-testid="stCaption"],
            [data-testid="stCaption"] p {{
                color: {_BLACK} !important;
            }}

            input,
            textarea,
            [data-baseweb="select"] > div {{
                background-color: {_WHITE} !important;
                color: {_TEXT_DARK} !important;
                border-color: {_BLACK} !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
