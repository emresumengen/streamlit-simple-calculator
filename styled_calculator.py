import streamlit as st

# Function to perform the calculation
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

# Layout
st.markdown("""
<style>
    .calculator {
        background-color: #f1f1f1;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        display: grid;
        grid-template-columns: repeat(4, 1fr);
    }
    .button {
        background-color: #4CAF50;
        border: none;
        color: white;
        font-size: 24px;
        padding: 20px;
        border-radius: 5px;
        margin: 5px;
        cursor: pointer;
    }
    .button:hover {
        background-color: #45a049;
    }
    .display {
        grid-column: span 4;
        background-color: white;
        border-radius: 5px;
        padding: 20px;
        font-size: 30px;
        text-align: right;
        border: 1px solid #ccc;
    }
</style>
""", unsafe_allow_html=True)

# Title of the App
st.title("Simple Calculator")

# Input field for the expression
expression = st.text_input("Input", value="0", key="input", max_chars=15)

# Calculator layout with buttons
with st.container():
    st.markdown('<div class="calculator">', unsafe_allow_html=True)
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    for button in buttons:
        if st.button(button, key=button):
            # Add functionality for button presses
            if button == 'C':
                expression = "0"
            elif button == '=':
                expression = str(calculate(expression))
            else:
                if expression == "0":
                    expression = button
                else:
                    expression += button

            # Update the input field
            st.session_state.input = expression

    st.markdown('</div>', unsafe_allow_html=True)

# Display Result
st.markdown('<div class="display">{}</div>'.format(st.session_state.input), unsafe_allow_html=True)
