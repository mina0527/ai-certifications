# 🔍 Generative AI-Powered Fraud Detection System

**Course:** Generative AI-Powered Fraud Detection System — Coursera  
**Status:** ✅ Completed

---

## 📌 Project Overview

This project builds an end-to-end fraud detection framework using Generative AI. The system generates synthetic financial transaction data, trains a machine learning model on that data, and detects fraudulent transactions — demonstrating how AI can be applied to one of the most critical challenges in financial operations and supply chain management.

---

## 🚀 What This Project Does

1. **Synthetic Data Generation** — Uses Generative AI principles (Probabilistic Modeling) to simulate realistic financial transaction datasets. This ensures the data contains "hidden" fraudulent patterns—like structuring and velocity spikes—that a standard random number generator would miss.
2. **Framework Design** — Builds a structured pipeline from data ingestion to model evaluation
3. **Model Logic & Classification** — Implements a heuristic-based classification model (Rule-Based ML) to identify fraudulent patterns. The model was optimized by testing different transaction thresholds to balance precision and recall.
4. **Fraud Detection** — Applies the trained model to flag suspicious transactions with measurable accuracy

---

## 💡 Why This Matters for Supply Chain & Procurement

Fraud detection is a critical concern in global supply chain operations, including:
- **Invoice fraud** and duplicate billing
- **Vendor manipulation** and kickback schemes
- **Payment diversion** in international procurement
- **Counterfeit goods** detection

The techniques used in this project are directly applicable to building smarter, AI-powered procurement and financial controls.

---

## 🛠️ Tools & Technologies

- **Language:** Python
- **AI/ML Libraries:** *(add your specific libraries, e.g., scikit-learn, TensorFlow, SDV, etc.)*
- **Data:** Synthetically generated transaction dataset
- **Environment:** Jupyter Notebook

---

## 📂 Repository Structure

```
fraud-detection-genai/
│
├── README.md                          ← Overview, setup, and findings
├── data/                              ← RAW DATA (Input files)
│   └── syntheticdata1.csv
│   └── synthetictransaction1.csv   
├── src/                               ← SCRIPTS (The "Engine")
│       ├── Syntheticdatacreation.py    ← Synthetic Data Generation logic
│       ├── TransactionFlagList.py      ← Initial threshold-based logic
│       ├── AnomallyDetection.py   ← Real-time monitoring simulation
│       ├── Flaggingtransactionssyntheticdata.py   ← Feature engineering (Frequency/Geo)
│       ├── parametersanomalliesdectec.py   ← Advanced Feature Engineering (Amount, Frequency, & Geography)
│       └── Evaluate_model.py            ← Performance metrics (Precision/Recall)
└── results/                           ← OUTPUTS (The Reports)
        ├── flagged_transactions_report.csv  ← Audit trail (Full data + flags)
        └── flagged_report_only.csv          ← Compliance Report (Alerts only)
```

---

## 📊 Results

| Metric | Score | Interpretation |
|---|---|---|
| Accuracy | *96.00%* | High, but misleading due to class imbalance|
|---------|
| True Positives  (Caught Fraud): | 4 | |
| False Positives (False Alarms): | 0 | Excellent for customer experience (no false alarm) |
| False Negatives (Missed Fraud): | 40 | HIgh Risk: Criminals are operatin successfully below $1k |
| True Negatives  (Correct Legit): | 956 | |
|---|
| Precision | *100%* | Every alert we generated was a real fraud |
| Recall | *9.09%* | Critical weakness: We missed 90% of the fraudulent activity |


---

### Key Findings
- The number and parameters of the synthetic data could be modify depending of the needs.
ex. the amount threshold could be modify for ML learning purposes.
- Using AI to analyze the data could provide a better overview of average transactions amounts, min, max, and other different patterns that we would like to highlight.
- You can set up an automated anomaly detection system using AI and providing the requirements for the industry needs.
- The model successfully detected fraudulent transactions with 96% accuracy
- If False Negatives (FN) is high: Your $1,000 threshold is too high. You are missing "cheap" fraud.
    - Solution: Lower the threshold to $500.
- If False Positives (FP) is high: Your $1,000 threshold is too low for your specific users. You are flagging too many normal big purchases.
    - Solution: Add more rules (like checking if the location is "Unknown").
- Accuracy vs. Recall: In fraud detection, Accuracy is often misleading. If 99% of transactions are legit, a model that says "nothing is fraud" is 99% accurate but 0% useful. Focus on Recall—that tells you if you're actually stopping the bad guys.

**NOTE**

- **Model Optimization:** During testing, I compared a $1,000 threshold against a $500 threshold.
    - At $1,000: Precision was 100% (zero false alarms), but Recall was only 9.09% (missed most fraud).
    - At $500: Recall significantly improved, catching smaller "smurfing" transactions, though it increased the number of False Positives. This highlights the critical "Fraud Analyst Trade-off."

### Model Evaluation

1. Testing Approach and Metrics

To evaluate the current script, we used a Synthetic Data Testing approach. Since we are using a rule-based system (threshold-based), the testing focused on segmentation accuracy.

- **Approach:** 
We ran the script against a dataset of diverse transaction amounts, locations, and frequencies to see how the "Fixed Threshold" rule performed against different transaction personas (e.g., a high-net-worth spender vs. a micro-transaction criminal).
- **Key Metrics Used:**
Detection Rate (Recall): The percentage of high-value transactions we successfully flagged. (Current: 100% for transactions >$1,000).
- **False Positive Rate (FPR):**
The percentage of legitimate high-value transactions (like rent or luxury purchases) that were incorrectly flagged.
- **Processing Latency:**
Time taken to process the CSV. Using Pandas vectorized operations resulted in near-instant execution, which is highly efficient for datasets up to several million rows.

2. Adjustments Made for Accuracy and Efficiency

Several iterations were made to the workflow to move it from a "prototype" to a "functional tool":

- **Automation of Output:**
Initially, the system only printed results to the terminal. We adjusted the script to generate a dedicated Report CSV (flagged_report_only.csv). This improves efficiency by allowing compliance officers to open the results directly in Excel without running the code themselves.
- **Path Robustness:** 
We adjusted the file-loading logic to use Raw String Paths (r'...') and absolute addressing. This fixed a critical efficiency bottleneck where the script would fail depending on which folder the terminal was opened in.
- **Data Labeling:** 
We added a Review_Reason column. This adds "Explainability" to the model, ensuring that the human reviewer knows exactly why a transaction was flagged, reducing the time spent on manual investigation.

3. Steps Taken to Reduce False Positives and False Negatives

The current $1,000 threshold is a "vulnerability" for both types of errors. We have planned the following technical adjustments to address them:

**To Reduce False Positives (Honest customers getting flagged):**
    - Current Issue: A user paying a $1,200 mortgage or buying a $1,100 laptop at a trusted store is flagged.
    - Adjustment: Implement Whitelisting/Profiling. By calculating the user's historical average spend, we can adjust the threshold.
        - *Logic:* Only flag if Amount > (User_Avg * 3). This ignores a $1,200 purchase for someone who usually spends $1,000, but flags a $1,200 purchase for someone who usually spends $20.

**To Reduce False Negatives (Criminals slipping through):**
    - Current Issue: "Structuring" or "Smurfing." A criminal makes five separate transactions of $950 to stay under our $1,000     radar.
    - Adjustment: Implement Velocity and Cumulative Checks.
        - *Logic:* Add a rolling 24-hour sum. If User_Sum_24h > 2000, flag the account even if every individual transaction was small.
    - Adjustment: Geographic "Impossible Travel" logic. If a transaction occurs in New York and another in London 2 hours later, the system should flag it regardless of the amount.

---

### ⚖️ Ethical & Governance Considerations
To ensure this system aligns with financial regulations (like AML and GDPR) and ethical AI standards, the following was considered:

- **Data Privacy:** By using Synthetic Data instead of real customer records, we eliminate the risk of exposing Personally Identifiable Information (PII) during the development phase.
- **Algorithmic Bias:** While this model uses a fixed threshold, a real-world version must be audited to ensure it doesn't unfairly flag specific geographic regions or lower-income brackets more often than others. It is important to set up and calibrate the parameters to reduce bias.
- **Human-in-the-Loop:** This system is designed as a **Decision Support Tool**, not a final decision-maker. All transactions flagged in flagged_report_only.csv must be reviewed by a human compliance officer before any accounts are blocked or vendors are blacklisted.


## Final Summary
The current workflow is highly efficient for meeting basic regulatory requirements (Large Transaction Reporting), but it is a low-precision model. It prioritizes catching every large transaction (High Recall) at the cost of flagging many legitimate ones (High False Positives). The next phase of development will focus on contextual features to narrow the focus to truly suspicious behavior. 

---


## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/ai-certifications.git

# Navigate to the project folder
cd ai-certifications/fraud-detection-genai

# Install dependencies (pandas, scikit-learn)
pip install -r requirements.txt

# --- STEP-BY-STEP EXECUTION ---

# 1. Generate the synthetic data
python src/Syntheticdatacreation.py

# 2. Run the flagging engine to identify fraud
python src/Flaggingtransactionssyntheticdata.py

# 3. View the performance metrics
python src/EvaluateModel.py
```

---

## 🏫 Course Credit

This project was completed as the final capstone for the **Generative AI-Powered Fraud Detection System** course on [Coursera](https://www.coursera.org).

---

*Part of my [AI Certifications](../README.md) repository.*
