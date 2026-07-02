# Motorcycle vs Bicycle Classifier — AWS SageMaker End-to-End ML Pipeline

## The Problem

Manually reviewing images to distinguish bicycles from motorcycles is time-consuming and unscalable for systems processing high volumes of visual data — traffic cameras, insurance claim portals, delivery fleet management. This project builds and deploys an automated binary classifier that makes this distinction with high confidence (0.997 on test images), served via a live API endpoint that can be integrated into any downstream system.

Real-world applications include:
- **Traffic management** — differentiating bike lanes vs. motorcycle lanes, toll systems with different pricing per vehicle type
- **Insurance platforms** — automatically categorizing submitted vehicle photos for claims or policy pricing
- **Delivery & logistics** — routing systems distinguishing bicycle couriers (slower, different constraints) from motorcycle couriers
- **Smart city infrastructure** — cameras counting and categorizing two-wheeled vehicles separately for urban planning

## Overview

An end-to-end image classification pipeline built on AWS SageMaker, from raw data preparation through model training, deployment, inference, and monitoring. Completed as part of the **AWS Machine Learning Fundamentals Nanodegree (Udacity)**.

## Pipeline Overview

```
CIFAR-100 Dataset
      ↓
Data Filtering & Preprocessing (bicycle vs motorcycle classes)
      ↓
Image Upload to S3 + TSV Metadata Files
      ↓
SageMaker Image Classification Training (ml.p3.2xlarge GPU)
      ↓
Model Deployment to SageMaker Endpoint (ml.m5.xlarge)
      ↓
Live Inference + Data Capture (S3)
      ↓
Model Monitoring + Baseline Generation
```

## Results

- **Test prediction confidence:** 0.997 (bicycle correctly classified)
- **Data capture:** 85 inference records captured and analyzed from live endpoint
- **Monitoring baseline:** established from live endpoint traffic with confidence threshold at 0.94

## Dataset

- **Source:** CIFAR-100 (filtered to bicycle class 8 and motorcycle class 48)
- **Training set:** 1,000 images (500 bicycles, 500 motorcycles)
- **Test set:** 200 images (100 bicycles, 100 motorcycles)
- **Image size:** 32×32 RGB, resized to 224×224 for SageMaker image classification algorithm

## Implementation Steps

**1. Data Acquisition & Preprocessing**
- Downloaded CIFAR-100 dataset programmatically
- Filtered to bicycle (label 8) and motorcycle (label 48) classes
- Reshaped flat CIFAR arrays into 32×32×3 RGB images
- Saved images to local directories and uploaded to S3

**2. SageMaker Training Setup**
- Created TSV metadata files (.lst format) mapping S3 image paths to binary labels
- Configured SageMaker Image Classification algorithm container
- Trained on `ml.p3.2xlarge` GPU instance with S3 input channels for train/validation

**3. Model Deployment**
- Deployed trained model to `ml.m5.xlarge` endpoint
- Configured DataCaptureConfig for 100% inference traffic capture to S3

**4. Inference & Data Capture**
- Built prediction function returning class probabilities for bicycle vs motorcycle
- Captured 30 JSONL files (85 inference records) from live endpoint traffic
- Visualized confidence scores over time with threshold monitoring at 0.94

**5. Model Monitoring**
- Set up DefaultModelMonitor with baseline generation from test images
- Parsed captured JSONL data to extract predictions and timestamps
- Built multi-panel monitoring dashboard (confidence distribution, time series, class breakdown)

**6. Step Functions Integration**
- Wrote Lambda function code for Step Functions workflow:
  - Lambda 1: Serialize image data from S3
  - Lambda 2: Call SageMaker endpoint for inference
  - Lambda 3: Filter low-confidence predictions

## AWS Services Used

- Amazon S3 (data storage, model artifacts, data capture)
- Amazon SageMaker (training, deployment, monitoring, data capture)
- AWS Lambda (Step Functions integration)
- AWS Step Functions (inference pipeline orchestration)
- IAM (execution roles)

## Tools & Libraries

Python, Boto3, SageMaker Python SDK, Pandas, NumPy, Matplotlib, Seaborn

## Notes

This was a guided project completed as part of the AWS Machine Learning Fundamentals Nanodegree. All AWS infrastructure (S3 bucket, SageMaker training jobs, endpoints) was provisioned and run live — not simulated. The monitoring visualization in Cell 45 was built with AI assistance (noted in the notebook).
