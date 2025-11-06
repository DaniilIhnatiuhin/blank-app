import streamlit as st
import time

gradients = [
    "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)",
    "linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%)",
    "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
    "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
    "linear-gradient(135deg, #a8ff78 0%, #78ffd6 100%)"
]

change_frequency = 3  

gradient_js = f"""
<script>
let gradients = {gradients};
let currentIndex = 0;

function changeGradient() {{
    currentIndex = (currentIndex + 1) % gradients.length;
    document.querySelector('.stApp').style.background = gradients[currentIndex];
}}

setInterval(changeGradient, {change_frequency * 1000});
</script>
"""

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {gradients[0]};
        background-attachment: fixed;
        transition: background 1s ease;
    }}
    </style>
    {gradient_js}
    """,
    unsafe_allow_html=True
)

st.title("Lista Zakupów")

if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = {}

def add_item():
    item = st.session_state.new_item.strip().lower()
    if item:
        if item in st.session_state.shopping_list:
            st.session_state.shopping_list[item] += 1
            st.success(f"Zaktualizowano ilość produktu: {item} (Ilość: {st.session_state.shopping_list[item]})")
        else:
            st.session_state.shopping_list[item] = 1
            st.success(f"Dodano produkt: {item} (Ilość: 1)")
        st.session_state.new_item = ""
    else:
        st.warning("Wprowadź nazwę produktu.")

def remove_item():
    selected_option = st.session_state.item_to_remove
    item = selected_option.split(" (")[0].lower()

    if item in st.session_state.shopping_list:
        if st.session_state.shopping_list[item] > 1:
            st.session_state.shopping_list[item] -= 1
            st.warning(f"Zmniejszono ilość produktu: {item} (Ilość: {st.session_state.shopping_list[item]})")
        else:
            del st.session_state.shopping_list[item]
            st.warning(f"Usunięto produkt: {item}")

st.text_input("Dodaj nowy produkt:", key="new_item", on_change=add_item)

st.write("Twoja lista zakupów:")
if not st.session_state.shopping_list:
    st.info("Lista zakupów jest pusta.")
else:
    for item, quantity in st.session_state.shopping_list.items():
        st.write(f"- {item} (Ilość: {quantity})")

if st.session_state.shopping_list:
    options = [f"{item} (Ilość: {quantity})" for item, quantity in st.session_state.shopping_list.items()]
    st.selectbox(
        "Wybierz produkt do usunięcia:",
        options=options,
        key="item_to_remove",
        format_func=lambda x: x
    )
    st.button("Usuń produkt", on_click=remove_item)
else:
    st.warning("Nie ma produktów do usunięcia.")
