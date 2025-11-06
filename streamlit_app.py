import streamlit as st
import streamlit.components.v1 as components

dynamic_gradient_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            width: 100vw;
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            transition: background 0.1s ease;
        }
    </style>
</head>
<body>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.addEventListener('mousemove', function(e) {
                const x = e.clientX;
                const y = e.clientY;
                const xPercent = Math.round((x / window.innerWidth) * 100);
                const yPercent = Math.round((y / window.innerHeight) * 100);

                document.body.style.background =
                    `radial-gradient(circle at ${xPercent}% ${yPercent}%,
                    #ff9a9e, #fad0c4, #a6c1ee, #84fab0, #8fd3f4)`;
            });
        });
    </script>
</body>
</html>
"""

components.html(dynamic_gradient_html, height=1000, width=1000)

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
