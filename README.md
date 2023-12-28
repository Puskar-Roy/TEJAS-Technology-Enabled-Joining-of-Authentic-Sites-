## TEJAS (Technology-Enabled Joining of Authentic Sites) 

## Project Workflow
The project will follow the same approach as used in all ML project. We'll go through different stages of data collection,feature extraction,training and finally deployment of trained model.

- Data Collection
- Feature Extraction
- Model training & evaluation
- Deployment


## Run (locally)
1. Import this repository using git command
```
git clone https://github.com/deepeshdm/Phishing-Attack-Domain-Detection.git
```
2. Install all the required dependencies inside a virtual environment
```
pip install -r requirements.txt
```
3. After this just import the get_prediction() from API.py and pass the required arguments to make the prediction.Below is an example,copy the below code snippet and pass the required variable values
```python
from API import get_prediction

# path to trained model
model_path = r"/models/Malicious_URL_Prediction.h5"

# input url
url = "www.google.com"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)
```




