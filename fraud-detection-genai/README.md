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
3. **Model Logic & Classification** — Implements a Random Forest Classifier (Supervised Machine Learning) to identify fraudulent patterns. Unlike static threshold rules, this model was trained on synthetic data to learn the complex statistical relationships between transaction amounts, frequency, and locations.
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
- **AI/ML Libraries:** pandas, scikit-learn
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
├── src/                               ← SCRIPTS (The "Engine")
│       ├── Syntheticdatacreation.py    ← Synthetic Data Generation logic
│       ├── Flaggingtransactionssyntheticdata.py   ← Feature engineering (Frequency/Geo)
│       └── Evaluate_model.py            ← Performance metrics (Precision/Recall)
└── results/                           ← OUTPUTS (The Reports)
        └── ml_flagged_report.csv            ← Compliance Report (Alerts only)
```

---

## 📊 Results

| Metric | OLD RULE (\$1K) | NEW ML MODEL |
|---|---|---|
| Accuracy | *96.00%* | *99.60%* |
| Precision | *100.00%* | *97.62%* |
| Recall | *9.09%* | *93.18%* |

--- ML MODEL CONFUSION MATRIX (COUNTS) ---
- True Positives  (Fraud Caught): 41
- True Negatives  (Correct Legit): 955
- False Positives (False Alarms):  1
- False Negatives (Missed Fraud):  3

---

### Key Findings
- Dataset Flexibility: The synthetic data parameters (volume, threshold, and fraud distribution) can be easily modified to simulate different industry-specific needs, such as procurement fraud or high-frequency retail transactions.
- The "Threshold" Limitation (Lessons Learned):
    - Initial benchmarking showed that a $1,000 static threshold was too rigid, resulting in a high number of False Negatives (missed fraud) and a low Recall of 9.09%.
    - While lowering the manual threshold to $500 improved detection, it significantly increased False Positives, creating an inefficient manual review process (the "Fraud Analyst Trade-off").
- The Machine Learning Solution: To overcome these limitations, the system was optimized by transitioning to a Random Forest Classifier. This allowed the model to analyze the statistical distribution of the data rather than relying on a fixed number, successfully identifying "structured fraud" at various price points.
- Final Performance: The optimized ML model achieved 99.60% Accuracy and 93.18% Recall, effectively identifying the fraudulent patterns that human-defined rules missed.
- The Importance of Recall: In fraud detection, Accuracy is often misleading. If 99% of transactions are legitimate, a model that simply guesses "Normal" every time would be 99% accurate but 0% useful. By focusing on Recall, we ensured the system is actually stopping criminal activity, which is the primary objective of a compliance workflow.

---

### Model Evaluation

1. Testing Approach and Metrics

To evaluate the system, we transitioned from a simple rule-based approach to a Supervised Machine Learning approach using a Random Forest Classifier.

    - Testing Methodology: We utilized an 80/20 train-test split on the synthetic dataset. This ensures that the model is evaluated on data it has never seen before, providing a true measure of its predictive power.
    - Key Metrics Used:
        - Recall (Sensitivity): The percentage of total fraudulent transactions correctly caught by the ML model. (Significantly improved from 9.09% to [Your Number]%).
        - Precision: The accuracy of the alerts generated, ensuring that flagged transactions are truly suspicious and reducing unnecessary manual investigations.
        - F1-Score: The harmonic mean of Precision and Recall, used to prove the model's overall robustness across imbalanced datasets.
2. Adjustments Made for Accuracy and Efficiency (Optimization)

The most significant adjustment was the move from Static Heuristic Rules to Algorithmic Classification:

    - From Static to Dynamic: The initial "Fixed Threshold" ($1,000) was replaced with the Random Forest model. This adjustment resolved the "False Negative" crisis where smaller, "structured" fraudulent transactions were being missed.
    - Feature Engineering: We optimized the model by focusing on Amount and Location patterns. This allowed the AI to "learn" that fraud often occurs in specific geographic clusters or unusual amount distributions that do not follow a simple linear rule.
    - Workflow Automation: The ML model automatically processes incoming CSV data and generates a prioritized ml_flagged_results.csv report, maintaining near-instant processing latency.

3. Steps Taken to Reduce False Positives and False Negatives

The transition to Machine Learning directly addressed the vulnerabilities of the previous rule-based system:

    - Reducing False Negatives (Missed Fraud): By training on the Is_Fraud ground-truth labels, the Random Forest model learned to flag suspicious transactions at various price points (e.g., $850 or $920). This effectively neutralized "Smurfing" tactics designed to bypass the $1,000 limit.
    - Reducing False Positives (False Alarms): The model performs Multi-Parameter Analysis. Instead of flagging every large purchase, it evaluates the relationship between Amount and Location. High-value transactions in "Trusted Locations" are cleared, while similar amounts in "Unknown" locations are flagged.

4. Baseline Comparison & Optimization Results

During the optimization phase, we compared three different detection strategies:

    - Rule-Based ($1,000): 100% Precision, but only 9.09% Recall (Highly ineffective).
    - Rule-Based ($500): Improved Recall, but created an unacceptable volume of False Positives (Inefficient).
    - Random Forest ML Model: Achieved the optimal balance with 99.60% Accuracy and 93.18% Recall, proving that Machine Learning is the superior solution for complex fraud detection.

---

### ⚖️ Ethical & Governance Considerations
To ensure this system aligns with financial regulations (like AML and GDPR) and ethical AI standards, the following was considered:

- **Data Privacy:** By using Synthetic Data instead of real customer records, we eliminate the risk of exposing Personally Identifiable Information (PII) during the development phase.
- **Algorithmic Bias:** Because Machine Learning models learn from data, they can unintentionally inherit biases. A real-world version must be audited to ensure it does not unfairly flag specific geographic regions or transaction types. Continuous calibration of the Random Forest parameters is required to ensure fair and equitable treatment of all users.
- **Human-in-the-Loop:** This system is designed as a **Decision Support Tool**, not an autonomous decision-maker. All transactions flagged in ml_flagged_results.csv are routed for human verification. This ensures that no vendor is blacklisted or account blocked without a manual audit by a compliance officer.


## Final Summary
The transition from a heuristic rule-based system to a Generative AI-informed Machine Learning framework has successfully modernized the fraud detection workflow. By replacing static thresholds with a Random Forest Classifier, the system moved from a "blind" 9.09% recall rate to a high-performance 93.18% recall, while maintaining exceptional precision.

The current workflow is now highly efficient for both meeting basic regulatory requirements (Large Transaction Reporting) and detecting sophisticated, "structured" fraud patterns. This project demonstrates that while Generative AI is invaluable for creating robust testing environments, Machine Learning is the superior choice for real-time classification and risk mitigation in financial operations and supply chain management. 

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
python src/Evaluate_model.py
```

---

## 🏫 Course Credit

This project was completed as the final capstone for the **Generative AI-Powered Fraud Detection System** course on [Coursera](https://www.coursera.org).

---

*Part of my [AI Certifications](../README.md) repository.*
