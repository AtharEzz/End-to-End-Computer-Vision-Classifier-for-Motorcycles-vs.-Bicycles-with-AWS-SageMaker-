 # Motorcycles vs Bicycles SageMaker Image Classification Project

## Academic Context & Credentials
Project Capstone: This production pipeline was developed as the comprehensive final capstone project for the AWS Machine Learning Fundamentals Nanodegree (Udacity). It demonstrates mastery in deploying scalable, cloud-native machine learning workflows, serverless orchestration, and automated production monitoring using AWS core ML services.

## Business Case: Optimizing Fleet Operations for "Scones Unlimited"
**The Problem**
In high-volume food logistics, operational efficiency depends heavily on routing the right vehicle to the right order. For Scones Unlimited, a premium delivery-focused logistics company, delivery dispatch must be optimized based on transit types:

Bicycles must be assigned to short-distance, dense urban orders to bypass traffic.

Motorcycles must be assigned to long-distance orders to maintain food freshness over mileage.

Manually identifying vehicle types at the loading bays creates massive operational bottlenecks, delays delivery times, and increases human labor costs.

**The Solution**
As a Machine Learning Engineer, I designed and shipped a scalable, safe, and automated image classification pipeline that identifies whether an incoming delivery driver has a bicycle or a motorcycle. By integrating this intelligence into the company's operating environment, Scones Unlimited can automatically route drivers to the correct loading bays and dynamically assign orders on-demand.

To ensure this enterprise application is production-ready, the architecture includes automated scaling to meet peak morning delivery demands and explicit MLOps safeguards to detect data drift or degraded model performance over time.

## End-to-End Implementation Steps
To achieve this, the project was executed across six core engineering stages:

[1. Data Staging] ➔ [2. Model Training & Deployment] ➔ [3. Serverless Lambda & Step Functions]
                                                                        │
[6. Resource Cleanup & Optimization] ⮘ [5. Advanced Drift Monitoring] ⮘ [4. Testing & Evaluation]

1 Data Staging: Extracted target vehicle classes from the raw CIFAR-100 dataset, processed images into optimized formats, and staged them in structured Amazon S3 buckets.

2 Model Training and Deployment: Leveraged AWS SageMaker to train a highly accurate image classifier using transfer learning on GPU compute, deploying it to an auto-scaling, production-grade endpoint with data capture enabled.

3 Lambdas and Step Function Workflow: Composed a serverless event-driven microservices application using AWS Lambda to handle data serialization, model inference invocations, and confidence-based filtering. Structured the entire logic path via AWS Step Functions.

4 Testing and Evaluation: Conducted live inference tests against validation data, monitored prediction confidence spreads, and verified the pipeline's operational threshold constraints.

5 Advanced MLOps Monitoring: Established automated data capture and generation of statistical baselines to continuously watch for real-world data drift or performance degradation.

6 Cloud Resource Cleanup: Successfully audited and tore down ephemeral infrastructure to demonstrate cost-optimization and budget discipline in cloud environments.

