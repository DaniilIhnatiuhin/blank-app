import streamlit as st

st.set_page_config(page_title="Lista zakupów", page_icon="🛒")

if "shopping_list" not in st.session_state:
    st.session_state["shopping_list"] = ["Chleb", "Mleko", "Jajka"]

st.title("Lista zakupów 🛒")

with st.form("add_form"):
    new_item = st.text_input("Nazwa produktu", key="new_item_input")
    submitted = st.form_submit_button("Dodaj")
    if submitted:
        item = new_item.strip()
        if item:
            st.session_state["shopping_list"].append(item)
            st.session_state["new_item_input"] = ""  # bezpieczne: wykonujemy to po submit
            st.success(f"Dodano: {item}")
        else:
            st.warning("Wpisz nazwę produktu przed dodaniem.")

st.markdown("---")

if st.button("Wyczyść listę"):
    st.session_state["shopping_list"] = []
    st.info("Lista została wyczyszczona.")

st.header("Twoja lista")
if st.session_state["shopping_list"]:
    for idx, it in enumerate(st.session_state["shopping_list"], start=1):
        cols = st.columns([0.85, 0.15])
        cols[0].write(f"{idx}. {it}")
        if cols[1].button("Usuń", key=f"del_{idx}"):
            st.session_state["shopping_list"].pop(idx - 1)
            st.experimental_rerun()
else:
    st.info("Lista jest pusta. Dodaj pierwszy produkt powyżej.")
