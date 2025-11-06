import streamlit as st

st.title("Lista Zakupów")

if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = {}

def add_item():
    item = st.session_state.new_item.strip().lower()  # Convert to lowercase for consistency
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
    item = st.session_state.item_to_remove
    item = item.split(" (")[0].lower()  # Extract "mleko" from "Mleko (Ilość: 3)"

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
        format_func=lambda x: x  # Display the full string (e.g., "Mleko (Ilość: 3)")
    )
    st.button("Usuń produkt", on_click=remove_item)
else:
    st.warning("Nie ma produktów do usunięcia.")
