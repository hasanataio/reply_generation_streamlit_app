import streamlit as st
import requests

# Streamlit app
st.title("Review Reply Generator")

# API URL
api_url = 'http://44.231.228.32:8023/generate_personalized_response'  # Change this to your FastAPI endpoint

# Input fields for user to enter data
st.subheader("Enter the Details Below:")

auth_token = st.text_input("Authorization Token", type="password")  # Token input, hidden for security
review = st.text_area("Review", "")
ratings = st.number_input("Ratings", min_value=0, max_value=5, value=0)
length = st.selectbox("Length", ["short", "long"])
food_items = st.text_input("Food Items", "")
customer_name = st.text_input("Customer Name", "")
additional_context = st.text_area("Additional Context", "")

# Button to submit data
if st.button("Generate Content"):
    # Preparing the data to send
    data = {
        "review": review,
        "ratings": str(ratings),
        "length": length,
        "food_items": food_items,
        "customer_name": customer_name,
        "additional_context": additional_context,
          "previous_replies": []
    }

    # Setting up the headers with the authorization token
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    # Making the POST request to the API
    try:
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            content_generated = response.json()
            st.subheader("Generated Content:")
            st.write("**Response**", content_generated.get("response",""))
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
