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

## Project Outcomes & Strategic Conclusion

**1. Final Project Deliverables**

The project successfully met and exceeded all operational design parameters set by the AWS Nanodegree curriculum:

The Model: Shipped a fine-tuned binary image classifier achieving a 94.3% validation accuracy at Epoch 14, requiring less than 4 minutes ($235 \text{ seconds}$) of active GPU training time.

The Workflow: Built a fully operational, event-driven serverless state machine that handles live image streams with a strict 93% automated confidence gate.

The MLOps Safeguard: Enabled 100% active data capture with an hourly monitoring loop to protect the live production system from silent performance decay.


**2. Business Impact for Scones Unlimited**

By moving from manual vehicle routing to this automated computer vision pipeline, the system delivers clear organizational value:

Eliminated Loading Bay Bottlenecks: Incoming delivery drivers are classified instantly upon arrival, automating dispatch routing to the correct loading zone without human intervention.

Optimized Fleet Efficiency: Bicycles are reliably restricted to localized, short-distance runs where they beat traffic, while motorcycles are prioritized for long-distance runs—directly reducing delivery times and protecting food freshness.

Risk Mitigation: By enforcing the 93% confidence threshold, the business avoids catastrophic misrouting. If a driver's vehicle image is obscured, foggy, or hard to read, the system safely routes the ticket to a human manager rather than making an automated, incorrect guess.

**3. Engineering Reflections & Expectations** 

Did it meet expectations? Yes. The rapid convergence rate (jumping from 61.9% to 92.2% validation accuracy within the first 4 epochs) proved that Transfer Learning was the correct architecture choice. Attempting to train a deep convolutional network from scratch on only 1,000 small images would have led to heavy overfitting.

Key Technical Learning: Orchestrating the application via AWS Step Functions highlighted the immense value of decoupling code. Isolating data serialization, inference generation, and filtering into distinct Lambda functions means individual microservices can be updated, scaled, or debugged independently without impacting the core machine learning model.
