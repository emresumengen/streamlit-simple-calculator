import streamlit as st
import math

def main():
    # Set page title
    st.title("Web Calculator")
    
    # Initialize session state to store calculation history
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    if 'current_number' not in st.session_state:
        st.session_state.current_number = ''

    # Display calculation history
    st.subheader("Calculation History:")
    for item in st.session_state.history:
        st.text(item)
    
    # Calculator display
    display = st.text_input("Calculator Display", value=st.session_state.current_number, key="display", label_visibility="collapsed")

    # Create button layout
    col1, col2, col3, col4 = st.columns(4)
    
    # Row 1
    with col1:
        if st.button("7"):
            st.session_state.current_number += "7"
            st.rerun()
    with col2:
        if st.button("8"):
            st.session_state.current_number += "8"
            st.rerun()
    with col3:
        if st.button("9"):
            st.session_state.current_number += "9"
            st.rerun()
    with col4:
        if st.button("÷"):
            st.session_state.current_number += "/"
            st.rerun()

    # Row 2
    with col1:
        if st.button("4"):
            st.session_state.current_number += "4"
            st.rerun()
    with col2:
        if st.button("5"):
            st.session_state.current_number += "5"
            st.rerun()
    with col3:
        if st.button("6"):
            st.session_state.current_number += "6"
            st.rerun()
    with col4:
        if st.button("×"):
            st.session_state.current_number += "*"
            st.rerun()

    # Row 3
    with col1:
        if st.button("1"):
            st.session_state.current_number += "1"
            st.rerun()
    with col2:
        if st.button("2"):
            st.session_state.current_number += "2"
            st.rerun()
    with col3:
        if st.button("3"):
            st.session_state.current_number += "3"
            st.rerun()
    with col4:
        if st.button("-"):
            st.session_state.current_number += "-"
            st.rerun()

    # Row 4
    with col1:
        if st.button("0"):
            st.session_state.current_number += "0"
            st.rerun()
    with col2:
        if st.button("C"):
            st.session_state.current_number = ""
            st.rerun()
    with col3:
        if st.button("√"):
            try:
                result = math.sqrt(float(st.session_state.current_number))
                st.session_state.history.append(f"√{st.session_state.current_number} = {result}")
                st.session_state.current_number = str(result)
                st.rerun()
            except:
                st.error("Invalid input for square root")
    with col4:
        if st.button("+"):
            st.session_state.current_number += "+"
            st.rerun()

    # Equal button
    if st.button("="):
        try:
            result = eval(st.session_state.current_number)
            st.session_state.history.append(f"{st.session_state.current_number} = {result}")
            st.session_state.current_number = str(result)
            st.rerun()
        except:
            st.error("Invalid expression")

if __name__ == "__main__":
    main()
