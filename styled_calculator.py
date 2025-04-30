import streamlit as st

# Initialize session states
if 'current_number' not in st.session_state:
    st.session_state.current_number = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Custom CSS for calculator styling and layout
st.markdown("""
<style>
    .main-container {
        display: flex;
        flex-direction: row;
        padding: 20px;
        gap: 20px;
    }
    
    .calculator {
        width: 400px;
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    
    .history {
        width: 300px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
        max-height: 600px;
        overflow-y: auto;
    }
    
    .history-item {
        cursor: pointer;
        padding: 5px;
        margin: 2px 0;
        border-radius: 3px;
    }
    
    .history-item:hover {
        background-color: #e9ecef;
    }
    
    .stButton > button {
        width: 100%;
        height: 50px;
        margin: 0px;
        padding: 0px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 5px;
    }
    
    div[data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
    }
    
    div[data-testid="stHorizontalBlock"] {
        gap: 5px !important;
        padding: 5px !important;
        margin: 0px !important;
    }
    
    div.row-widget.stTextInput > div {
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 5px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Create main container with flex layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Calculator container (left side)
st.markdown('<div class="calculator">', unsafe_allow_html=True)

# Calculator display
display = st.text_input("Calculator Display", value=st.session_state.current_number, 
                       key="display", label_visibility="collapsed")

# Row 1
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C"):
        st.session_state.current_number = ""
        st.rerun()
with col2:
    if st.button("("):
        st.session_state.current_number += "("
        st.rerun()
with col3:
    if st.button(")"):
        st.session_state.current_number += ")"
        st.rerun()
with col4:
    if st.button("➗"):
        st.session_state.current_number += "/"
        st.rerun()

# Row 2
col1, col2, col3, col4 = st.columns(4)
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
    if st.button("✖️"):
        st.session_state.current_number += "*"
        st.rerun()

# Row 3
col1, col2, col3, col4 = st.columns(4)
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
    if st.button("➖"):
        st.session_state.current_number += "-"
        st.rerun()

# Row 4
col1, col2, col3, col4 = st.columns(4)
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
    if st.button("➕"):
        st.session_state.current_number += "+"
        st.rerun()

# Row 5
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("0"):
        st.session_state.current_number += "0"
        st.rerun()
with col2:
    if st.button("."):
        st.session_state.current_number += "."
        st.rerun()
with col3:
    if st.button("⌫"):
        st.session_state.current_number = st.session_state.current_number[:-1]
        st.rerun()
with col4:
    if st.button("="):
        try:
            expression = st.session_state.current_number
            result = str(eval(expression))
            # Add to history
            st.session_state.history.append(f"{expression} = {result}")
            st.session_state.current_number = result
        except:
            st.session_state.current_number = "Error"
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# History section (right side)
st.markdown('<div class="history">', unsafe_allow_html=True)
st.markdown("### History")

# Make history items clickable
for idx, item in enumerate(st.session_state.history):
    if st.button(item, key=f"history_{idx}"):
        # Extract the result part (after the '=')
        result = item.split('=')[1].strip()
        st.session_state.current_number = result
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
