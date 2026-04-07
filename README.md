# ☁️ Predictive Cloud Resource Forecaster

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

## What is this project?
Cloud servers (like AWS or Azure) cost a lot of money if you leave them running at maximum power when nobody is using them. But if you scale them down and a sudden wave of users logs in, your application crashes. Usually, servers just react to traffic *after* it happens. 

I wanted to see if I could build a predictive model that forecasts server CPU demand *before* the traffic hits, so the system can scale up proactively.

## Why this matters (The Goal)
1. **Saving Money:** If the model knows the server will be quiet at 3:00 AM, the company can confidently scale down resources and cut costs.
2. **Preventing Crashes:** If it knows a spike is coming at noon, it can boot up extra compute power in advance so users don't experience lag.
3. **Automation:** It removes the need for an engineer to manually watch server dashboards all day.

## How I built it 
###### (and flaws along the way)
I quickly learned that predicting data is harder than it looks. I went through a few different approaches:

* **Attempt 1: Hardcoding the Rules**
  * *What I tried:* I just wrote basic logic like "If it's past 12:00 PM, increase CPU by 50%."
  * *Why it failed:* It was too rigid. It didn't account for weekends or random organic traffic, so it was frequently wrong.
* **Attempt 2: Linear Regression**
  * *What I tried:* I used basic statistical regression to try and draw a trend line through the data. 
  * *Why it failed:* Server traffic isn't a straight line; it moves in waves. The linear model totally missed the mid-day spikes.
* **Attempt 3: Random Forest (The Winner)**
  * *What I tried:* I used `Scikit-Learn` to implement a Random Forest Regressor. 
  * *The Result:* This worked incredibly well. The model actually learned the difference between a busy Tuesday afternoon and a quiet Sunday night, tracking the data almost perfectly without human intervention.


![Prediction Graph](<pred_graph.jpeg>)

## What I want to improve next
I'm proud of how the model performs on normal weekly cycles, but there are a few things I would want to fix as I keep learning:

1. **It doesn't know about Holidays:** Right now, the AI only looks at the `Hour` and `Day_of_Week`. If a massive, unpredictable event happens (like Black Friday), the model will fail. I want to add a boolean `is_holiday` feature to the dataset next.
2. **Real-Time Data:** Currently, I train the model on a static CSV file that I generated using Pandas/NumPy. In the real world, I'd want to connect this to a live streaming pipeline to ingest real server logs.
3. **Actually Deploying It:** Right now, my code outputs a Matplotlib graph to prove the math works, but it doesn't actually talk to a cloud server yet. Eventually, I'd like to wrap this in an API (like FastAPI) so a real server load-balancer could ask my AI for instructions.

## How to Run Locally

**1. Clone the repository and install the libraries:**
``` bash
git clone https://github.com/kaur-nel/cloud-resource-forecaster.git
cd cloud-resource-forecaster
pip install pandas numpy scikit-learn matplotlib
``` 

**2. Generate the simulated server data:**
```bash
python generate_data.py
```
*(This creates a `server_logs.csv` file with 720 hours of simulated traffic).*

**3. Train the AI and see the results:**
```bash
python train_model.py
```
*(A visual graph will pop up comparing the Actual Server Load against the AI's Prediction).*