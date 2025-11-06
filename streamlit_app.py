import streamlit as st

st.title("Lista Zakupów")

if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

def add_item():
    item = st.session_state.new_item.strip()
    if item and item not in st.session_state.shopping_list:
        st.session_state.shopping_list.append(item)
        st.session_state.new_item = ""
        st.success(f"Dodano produkt: {item}")
    elif item in st.session_state.shopping_list:
        st.warning(f"Produkt '{item}' już istnieje na liście.")

def remove_item():
    item = st.session_state.item_to_remove
    if item in st.session_state.shopping_list:
        st.session_state.shopping_list.remove(item)
        st.warning(f"Usunięto produkt: {item}")

st.text_input("Dodaj nowy produkt:", key="new_item", on_change=add_item)

st.write("Twoja lista zakupów:")
if not st.session_state.shopping_list:
    st.info("Lista zakupów jest pusta.")
else:
    for item in st.session_state.shopping_list:
        st.write(f"- {item}")

if st.session_state.shopping_list:
    st.selectbox(
        "Wybierz produkt do usunięcia:",
        st.session_state.shopping_list,
        key="item_to_remove"
    )
    st.button("Usuń produkt", on_click=remove_item)
else:
    st.warning("Nie ma produktów do usunięcia.")
