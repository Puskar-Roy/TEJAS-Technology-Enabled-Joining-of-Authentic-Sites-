from API import get_prediction

model_path = r"D:/Documents/ML/Tejas/Phishing-Attack-Domain-Detection/models/Malicious_URL_Prediction.h5"

url = "www.tesla.com/"

prediction = get_prediction(url,model_path)
print(prediction)

