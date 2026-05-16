import streamlit as st

st.set_page_config(page_title="IP Validator", page_icon ="🌐")

st.title("IP Address Validator")
st.write("Check whether an IPv4 address is valid or invalid.")

def validate_ip(ip):
    parts = ip.split('.')

    if len(parts) !=4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        num = int(part)

        if num < 0 or num > 255:
            return False
        
    return True

ip = st.text_input("Enter IP Address")

if st.button("Validate IP"):

    if validate_ip(ip):
        st.success("Valid IP Address")
    else:
        st.error("Invalid IP Address")

st.markdown("___")
st.caption("Cyber Project")