import streamlit as st

def calculate_comm_score(responses):
    """
    Calculate the total score for the Current Opioid Misuse Measure (COMM).
    
    Args:
        responses (list): A list of integer responses to the 17 COMM items.
        
    Returns:
        int: The total score for the COMM.
    """
    return sum(responses)

def interpret_comm_score(score):
    """
    Interpret the total score for the Current Opioid Misuse Measure (COMM).
    
    Args:
        score (int): The total score for the COMM.
        
    Returns:
        str: The interpretation of the COMM score.
    """
    if score < 9:
        return "Low likelihood of opioid misuse."
    elif score >= 9 and score < 20:
        return "Moderate likelihood of opioid misuse."
    else:
        return "High likelihood of opioid misuse."


st.title("Current Opioid Misuse Measure (COMM) Calculator")

# Description of the app
st.write("""
The Current Opioid Misuse Measure (COMM) is a self-report screening tool used to
identify patients who may be misusing prescription opioids. It consists of 17 items,
each scored on a scale of 0 (never) to 4 (very often). This app allows you to input
your responses to the 17 COMM items and receive a calculated total score along with an
interpretation.
""")

# Input fields for the 17 COMM items
responses = []
for i in range(1, 18):
    response = st.slider(f"Item {i} (0: Never, 4: Very Often)", min_value=0, max_value=4, value=0, step=1)
    responses.append(response)

# Calculate the total score and display the interpretation
if st.button("Calculate COMM Score"):
    total_score = calculate_comm_score(responses)
    interpretation = interpret_comm_score(total_score)
    st.write(f"Total COMM Score: {total_score}")
    st.write(interpretation)
