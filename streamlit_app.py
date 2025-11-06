import streamlit as st
import locale

languages = {
    "polish": {
        "title": "Lista Zakupów",
        "add_product": "Dodaj nowy produkt:",
        "remove_product": "Usuń produkt",
        "clear_list": "Wyczyść listę",
        "empty_list": "Lista zakupów jest pusta.",
        "select_language": "Wybierz język",
        "dark_mode": "Włącz tryb ciemny",
        "font_size": "Rozmiar czcionki",
        "high_contrast": "Włącz tryb wysokiego kontrastu",
        "accessibility_statement": "Oświadczenie dotyczące dostępności",
    },
    "english": {
        "title": "Shopping List",
        "add_product": "Add a new product:",
        "remove_product": "Remove product",
        "clear_list": "Clear list",
        "empty_list": "The shopping list is empty.",
        "select_language": "Select language",
        "dark_mode": "Enable dark mode",
        "font_size": "Font size",
        "high_contrast": "Enable high contrast mode",
        "accessibility_statement": "Accessibility Statement",
    },
}

if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = {}

with st.sidebar:
    st.header(languages["english"]["select_language"])  # Default header in English

    # Language selection with error handling
    selected_language = st.selectbox(
        languages["english"]["select_language"],
        options=list(languages.keys()),
        index=0,  # Default to the first language
    )
    current_language = languages.get(selected_language, languages["polish"])  # Fallback to Polish

    dark_mode = st.checkbox(current_language["dark_mode"])

    high_contrast = st.checkbox(current_language["high_contrast"])

    font_size = st.slider(current_language["font_size"], 10, 24, 16)

if dark_mode:
    st.markdown(
        """
        <style>
            body, .stApp, .stTextInput, .stButton, .stSelectbox, .stWrite, .stExpander, .stHeader {
                background-color: #1E1E1E;
                color: white;
            }
            .stTextInput input, .stSelectbox select, .stButton button {
                background-color: #333333;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if high_contrast:
    st.markdown(
        """
        <style>
            body, .stApp, .stTextInput, .stButton, .stSelectbox, .stWrite, .stExpander, .stHeader {
                background-color: black;
                color: white;
            }
            .stTextInput input, .stSelectbox select, .stButton button {
                background-color: white;
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <style>
        body, .stTextInput, .stButton, .stSelectbox, .stWrite, .stExpander, .stHeader {{
            font-size: {font_size}px !important;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(current_language["title"])

new_item = st.text_input(current_language["add_product"], key="new_item")

def add_item():
    item = new_item.strip().lower()
    if item:
        if item in st.session_state.shopping_list:
            st.session_state.shopping_list[item] += 1
            st.success(f"{current_language['add_product']} {item} (Ilość: {st.session_state.shopping_list[item]})")
        else:
            st.session_state.shopping_list[item] = 1
            st.success(f"{current_language['add_product']} {item} (Ilość: 1)")
    else:
        st.warning(current_language["empty_list"])

st.button(current_language["add_product"], on_click=add_item)

st.write(current_language["title"] + ":")
if not st.session_state.shopping_list:
    st.info(current_language["empty_list"])
else:
    for item, quantity in st.session_state.shopping_list.items():
        st.write(f"- {item} ({current_language['quantity']}: {quantity})")

if st.session_state.shopping_list:
    options = [f"{item} ({current_language['quantity']}: {quantity})" for item, quantity in st.session_state.shopping_list.items()]
    item_to_remove = st.selectbox(current_language["remove_product"], options=options, key="item_to_remove")

    def remove_item():
        item = item_to_remove.split(" (")[0].lower()
        if item in st.session_state.shopping_list:
            if st.session_state.shopping_list[item] > 1:
                st.session_state.shopping_list[item] -= 1
                st.warning(f"{current_language['remove_product']} {item} ({current_language['quantity']}: {st.session_state.shopping_list[item]})")
            else:
                del st.session_state.shopping_list[item]
                st.warning(f"{current_language['remove_product']} {item}")

    st.button(current_language["remove_product"], on_click=remove_item)
else:
    st.warning(current_language["empty_list"])

with st.expander(current_language["accessibility_statement"]):
    st.write(
        f"""
        {current_language['accessibility_statement']}:
        - {current_language['dark_mode']}
        - {current_language['high_contrast']}
        - {current_language['font_size']}
        """
    )
