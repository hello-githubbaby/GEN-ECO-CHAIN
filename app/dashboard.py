import streamlit as st
from src.modules.returns_prediction import predict_return_likelihood
from src.modules.fraud_agent import detect_fraud
from src.modules.sustainability_score import sustainability_score
from src.modules.personalization_agent import personalize_customer
from src.modules.anomaly_detector import detect_anomaly
from src.modules.route_optimizer import optimize_route

st.title("GEN-ECO-CHAIN — Reverse Logistics AI Engine")

st.subheader("Enter Order Details")
product = st.text_input("Product")
category = st.text_input("Category")
price = st.number_input("Price", min_value=0.0)
past_returns = st.number_input("Past Returns", min_value=0)
reason = st.text_input("Return Reason")

if st.button("Run Analysis"):
    order = {
        "product": product,
        "category": category,
        "price": price,
        "past_returns": past_returns,
        "return_reason": reason,
    }

    st.write("### Return Likelihood")
    st.json(predict_return_likelihood(order))

    st.write("### Fraud Check")
    st.json(detect_fraud(order))

    st.write("### Sustainability")
    st.json(sustainability_score(order))

    st.write("### Personalization")
    st.json(personalize_customer(order))

    st.write("### Anomaly Detection")
    st.json(detect_anomaly(order))

locations = st.text_area("Enter locations (comma separated)")
if st.button("Optimize Route"):
    locs = [x.strip() for x in locations.split(",")]
    st.json(optimize_route(locs))
