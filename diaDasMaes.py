import streamlit as st

st.set_page_config(page_title="dia das maes", page_icon="💞")

st.title("feliz dia das maes💖")
nome= st.text_input("digite o nome da sua mae: ")

if st.button("mostrar mensagem"):
    if nome:
        st.success(f"{nome}, voce e uma amae incrivel te amo💗")
        st.balloons()
    else:
        st.warning("digite o nome da sua mae para ver a mensagem")
st.image("https://s.calendarr.com/upload/90/a4/dia-das-maes-f.png", use_container_width= True)