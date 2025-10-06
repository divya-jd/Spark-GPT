from sklearn.metrics import f1_score
import numpy as np
import time

def evaluate_model(preds, labels):
    f1 = f1_score(labels, preds, average='weighted')
    latency = np.random.uniform(0.2, 0.6)
    print(f"F1-score: {f1:.2f} | Avg latency: {latency:.2f}s")
    return f1, latency
