#  Network Intrusion Detection System (NIDS) for IoT Gateway

##  Project Overview
This project implements a **Network Intrusion Detection System (NIDS)** designed for an IoT gateway operating under resource constraints.

The system analyzes network traffic in real-time, extracts features from packet flows, and detects attack patterns using **Dynamic Time Warping (DTW)**.

It is designed to be:
- Lightweight  
- Real-time  
- Robust to network jitter and timing variations  

---

##  Objectives

- Monitor network traffic using flow-based analysis  
- Extract statistical and behavioral features  
- Detect known attack patterns (Port Scan, DoS, Malware)  
- Optimize performance for embedded environments  

---

##  Key Features

- ✅ Flow identification using 5-tuple  
- ✅ Sliding window segmentation (with overlap)  
- ✅ Feature extraction (mean, variance, inter-arrival time, flags)  
- ✅ DTW-based pattern matching  
- ✅ Sakoe-Chiba band optimization  
- ✅ Early abandonment for performance  
- ✅ Real-time classification output  
- ✅ Flow table with memory-aware aging  
- ✅ Evaluation using confusion matrix and accuracy  

---

##  System Architecture
Packet Data (CSV)
↓
Flow Identification (5-tuple)
↓
Sliding Window (per flow)
↓
Feature Extraction
↓
DTW Matching
↓
Classification Output

---

##  Technologies Used

- **Language:** Python  
- **Libraries:** None (DTW implemented from scratch)  
- **Data Format:** CSV (simulated network traffic)  
- **Environment:** VS Code  

---

##  Project Structure
NIDS_project4/
│
├── src/
│ ├── main.py
│ ├── dtw.py
│ ├── matcher.py
│ ├── feature_extractor.py
│ ├── sliding_window.py
│ ├── packet.py
│ ├── evaluation.py
│
├── data/
│ └── traffic.csv
│
├── templates/
│ └── templates.json
│
├── tests/
│ └── tests_dtw.py
│
└── README.md

---

##  How to Run

###  Run Main Detection System

> python src/main.py

### Run Evaluation

>python src/evaluation.py

### Evaluation Results ##
Confusion Matrix:
{'normal': {'normal': 1},
 'port_scan': {'port_scan': 1},
 'dos': {'dos': 1}}
Accuracy:
1.0 (synthetic dataset)

Note: Accuracy is high due to controlled synthetic data. Real-world performance may vary.

## DTW Algorithm

Dynamic Time Warping (DTW) is used to compare time-series patterns.

Complexity:
O(n × m)
Optimizations:
Sakoe-Chiba Band → reduces search space
Early Abandonment → stops unnecessary computation
### Trade-offs
Factor	            Trade-off
Window Size	        Latency vs Accuracy
Template Length	    Speed vs Precision
Flow Count	        Memory vs Coverage

### Limitations
Uses synthetic dataset
Simplified attack templates
DTW computational overhead

## Future Improvements
Integration with real datasets (CIC-IDS, KDD)
Machine learning-based detection
Adaptive template generation
Hardware optimization for embedded systems

## Authors
ACHIENG JACINTA OKETCH
KIYAI SOPHIE OKOLONG
KYAMANYWA CLOPHUS
KYAGONDEZE FLORAH
KIIZA PETER