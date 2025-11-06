import streamlit as st

st.set_page_config(page_title="Lista zakupów", page_icon="🛒")

if "items" not in st.session_state:
    st.session_state.items = ["Chleb", "Mleko", "Jajka"]

st.title("Lista zakupów 🛒")

st.header("Dodaj produkt")
new_item = st.text_input("Nazwa produktu", key="new_item_input")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Dodaj"):
        item = new_item.strip()
        if item:
            st.session_state.items.append(item)
            st.session_state.new_item_input = ""  # wyczyść pole
            st.success(f'Dodano: {item}')
        else:
            st.warning("Wpisz nazwę produktu przed dodaniem.")

with col2:
    if st.button("Wyczyść listę"):
        st.session_state.items = []
        st.info("Lista została wyczyszczona.")

st.markdown("---")

st.header("Twoja lista")
if st.session_state.items:
    to_remove = st.multiselect("Zaznacz produkty do usunięcia", options=st.session_state.items)
    if st.button("Usuń zaznaczone"):
        if to_remove:
            st.session_state.items = [it for it in st.session_state.items if it not in to_remove]
            st.success(f'Usunięto: {", ".join(to_remove)}')
        else:
            st.warning("Żaden produkt nie został zaznaczony.")
    st.write("Aktualna lista:")
    for i, it in enumerate(st.session_state.items, start=1):
        st.write(f"{i}. {it}")
else:
    st.info("Lista jest pusta. Dodaj pierwszy produkt powyżej.")
