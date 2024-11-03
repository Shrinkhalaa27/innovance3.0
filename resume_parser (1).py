# -*- coding: utf-8 -*-
"""Resume Parser.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bSNGcD-7nkO0ax4vAtm1AUKooVTCSjiP
"""

!pip install PyPDF2

import pdfplumber
import re
import pandas as pd

def parse_resume_from_pdf(pdf_path):
    # Initialize a dictionary to hold parsed data
    parsed_data = {
        "experience": [],
        "education": [],
        "skills": [],
        "certifications": []
    }

    # Define keyword sets for each category
    experience_keywords = {"managed", "developed", "led", "designed", "coordinated", "implemented", "analyzed", "created", "directed", "executed", "supervised", "assisted",
    "experience",
    "managed",
    "developed",
    "led",
    "coordinated",
    "implemented",
    "designed",
    "engineered",
    "architected",
    "orchestrated",
    "conducted",
    "analyzed",
    "optimized",
    "created",
    "directed",
    "executed",
    "supervised",
    "assisted",
    "achieved",
    "established",
    "collaborated",
    "communicated",
    "trained",
    "mentored","evaluated","strategized","formulated","improved","built",
    "produced","facilitated","supported","innovated","drove"}
    skills_keywords = {
    "Algorithm Design", "Computational Complexity", "Dynamic Programming",
    "Greedy Algorithms", "Divide and Conquer", "Backtracking", "Graph Theory",
    "Data Structures", "Binary Trees", "Hash Tables", "Linked Lists",
    "Stacks", "Queues", "Red-Black Trees", "Trie Data Structure",
    "Distributed Systems", "Event-Driven Architecture", "Pub/Sub Systems",
    "Microfrontends", "Progressive Web Apps (PWA)", "Single Page Applications (SPA)",
    "Web Accessibility (WCAG)", "Cross-Browser Compatibility", "Web Security",
    "OAuth2", "JWT (JSON Web Token)", "CORS", "Content Delivery Network (CDN)",
    "Load Balancer", "Reverse Proxy", "SSL/TLS", "SQL Indexing", "Query Optimization",
    "ACID Properties", "CAP Theorem", "Database Sharding", "Data Replication",
    "Web Scraping", "Selenium", "Beautiful Soup", "Scrapy", "Automated Testing",
    "Behavior-Driven Development (BDD)", "Test-Driven Development (TDD)",
    "Continuous Testing", "Chaos Engineering", "Infrastructure as Code (IaC)",
    "Containerization", "Cloud-Native Applications", "Serverless Functions",
    "Message Queues", "RabbitMQ", "Apache ActiveMQ", "ZeroMQ", "Message Brokers",
    "Circuit Breaker Pattern", "Service Mesh", "Istio", "Linkerd",
    "Application Monitoring", "Prometheus", "Grafana", "ELK Stack",
    "Machine Learning Pipelines", "MLflow", "Kubeflow", "Airflow",
    "Data Version Control (DVC)", "Synthetic Data", "Model Drift Detection",
    "Data Distribution Shift", "Bayesian Networks", "Gaussian Mixture Models",
    "Reinforcement Learning Environments", "OpenAI Gym", "Markov Decision Processes",
    "Policy Gradient Methods", "Q-Learning", "Monte Carlo Methods",
    "Statistical Inference", "Maximum Likelihood Estimation (MLE)",
    "Bayesian Inference", "Bootstrapping", "Resampling Techniques",
    "Empirical Bayes", "Hierarchical Clustering", "Agglomerative Clustering",
    "Dendrograms", "Silhouette Analysis", "Scree Plot", "Elbow Method",
    "Hadoop Ecosystem", "HDFS", "YARN", "Pig", "Hive", "Flume",
    "Oozie", "ZooKeeper", "Ambari", "Databricks", "PrestoDB",
    "Feature Stores", "Feature Engineering Tools", "Feature Drift",
    "Hyperparameter Optimization", "Grid Search", "Random Search", "Bayesian Optimization",
    "SHAP Values", "LIME (Local Interpretable Model-Agnostic Explanations)",
    "Model Explainability", "Trustworthy AI", "Data Quality Assessment",
    "Data Provenance", "Anomaly Detection", "Time Series Forecasting",
    "Seasonal Decomposition", "ARIMA Models", "LSTM Networks for Time Series",
    "Attention Mechanisms", "Transformers", "BERT", "GPT Models",
    "Text Preprocessing", "Tokenization", "Stemming", "Lemmatization",
    "Word Embeddings", "GloVe", "Word2Vec", "FastText", "TF-IDF",
    "Document Classification", "Sentiment Analysis", "Topic Modeling",
    "Latent Dirichlet Allocation (LDA)", "Text Summarization", "Named Entity Recognition (NER)","python", "java", "sql", "data analysis", "machine learning", "communication", "project management", "team leadership"}

    education_keywords = {
    "bachelor",
    "master",
    "phd",
    "degree",
    "university",
    "college",
    "diploma",
    "certification",
    "associate",
    "graduate",
    "undergraduate",
    "postgraduate",
    "transcript",
    "GPA",
    "coursework",
    "curriculum",
    "major",
    "minor",
    "field of study",
    "specialization",
    "honors",
    "honors degree",
    "thesis",
    "dissertation",
    "faculty",
    "academic",
    "study abroad",
    "online course",
    "continuing education",
    "alumni",
    "enrollment",
    "admissions",
    "tuition",
    "scholarship",
    "fellowship",
    "training",
    "workshop",
    "seminar",
    "lecture",
    "module",
    "credits",
    "program",
    "school",
    "certificate",
    "recognition",
    "achievement",
    "accreditation",
    "institution",
    "academic record",
    "skills development",
    "apprenticeship"
}

    certifications_keywords = {"certified", "certification", "license", "credential"}

    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Extract text from each page
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                print(f"Extracted Text from Page:\n{text}\n")  # Debugging: Print extracted text

                # Split the text into lines for further processing
                lines = text.split('\n')

                # Define regex patterns to identify sections
                experience_pattern = re.compile(r'(Experience|Work History)', re.IGNORECASE)
                education_pattern = re.compile(r'(Education|Academic)', re.IGNORECASE)
                skills_pattern = re.compile(r'(Skills|Technical Skills)', re.IGNORECASE)
                certifications_pattern = re.compile(r'(Certifications|Licenses)', re.IGNORECASE)

                current_section = None

                for line in lines:
                    # Check for section headers
                    if experience_pattern.search(line):
                        current_section = 'experience'
                    elif education_pattern.search(line):
                        current_section = 'education'
                    elif skills_pattern.search(line):
                        current_section = 'skills'
                    elif certifications_pattern.search(line):
                        current_section = 'certifications'
                    elif current_section:
                        # Extract relevant keywords based on the current section
                        if current_section == 'experience':
                            extracted_keywords = [word for word in experience_keywords if word in line.lower()]
                            if extracted_keywords:
                                parsed_data[current_section].extend(extracted_keywords)
                        elif current_section == 'education':
                            extracted_keywords = [word for word in education_keywords if word in line.lower()]
                            if extracted_keywords:
                                parsed_data[current_section].extend(extracted_keywords)
                        elif current_section == 'skills':
                            extracted_keywords = [word for word in skills_keywords if word in line.lower()]
                            if extracted_keywords:
                                parsed_data[current_section].extend(extracted_keywords)
                        elif current_section == 'certifications':
                            extracted_keywords = [word for word in certifications_keywords if word in line.lower()]
                            if extracted_keywords:
                                parsed_data[current_section].extend(extracted_keywords)

    # Clean up the lists by removing duplicates and empty entries
    for key in parsed_data:
        parsed_data[key] = list(set(parsed_data[key]))  # Remove duplicates
        parsed_data[key] = [entry for entry in parsed_data[key] if entry]  # Remove empty entries

    # Debugging: Print parsed data
    print("Parsed Data:")
    for section, entries in parsed_data.items():
        print(f"{section}: {entries}")

    return parsed_data

# Example usage
pdf_path =   #->>>>>>>>>>>>>>> #Resume path <<<<<<<<<<<<<-        # Specify the path to your PDF resume
parsed_resume = parse_resume_from_pdf(pdf_path)

# Convert parsed data to a DataFrame for better visualization
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in parsed_resume.items()]))
print(df)