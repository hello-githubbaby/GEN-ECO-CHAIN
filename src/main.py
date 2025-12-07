from src.modules.returns_prediction import predict_return_likelihood
from src.modules.fraud_agent import detect_fraud
from src.modules.sustainability_score import sustainability_score
from src.modules.personalization_agent import personalize_customer
from src.modules.anomaly_detector import detect_anomaly
from src.modules.route_optimizer import optimize_route

sample_order = {
    "customer_id": "C123",
    "product": "Wireless Earbuds",
    "price": 69.99,
    "category": "Electronics",
    "past_returns": 2,
    "delivery_delay_hours": 12,
    "location": "Hyderabad",
    "return_reason": "Not working",
}

sample_locations = ["Hyderabad", "Secunderabad", "Ameerpet", "Gachibowli"]

def run_pipeline(order):
    print("\n=== Return Likelihood ===")
    print(predict_return_likelihood(order))

    print("\n=== Fraud Analysis ===")
    print(detect_fraud(order))

    print("\n=== Sustainability Score ===")
    print(sustainability_score(order))

    print("\n=== Customer Cluster ===")
    print(personalize_customer(order))

    print("\n=== Anomaly Detection ===")
    print(detect_anomaly(order))

    print("\n=== Route Optimization ===")
    print(optimize_route(sample_locations))

if __name__ == "__main__":
    run_pipeline(sample_order)
