    User Behavior & Conversion Analysis

    Overview
This project focuses on the analysis of user behavior within an e-commerce environment. By processing raw event logs, the tool uncovers how users interact with a platform, where they drop off in the sales process, and how different devices influence purchasing decisions.

The project is designed to demonstrate the transition from raw digital footprints (logs) to actionable business insights regarding user retention and conversion.

    ech Stack
    Python - core processing and analytical logic
    Pandas - data manipulation and calculation of business metrics (CR, Retention)
    Matplotlib / Seaborn – static data visualization for reporting
    Random / Datetime - synthetic data generation and time-series handling

    Key Analytical Features
    Conversion Funnel Logic
Calculates the transition rate from basic page views to successful purchases, identifying the overall efficiency of the sales process.
    Device-Based Segmentation
Analyzes performance differences between Mobile and Desktop users to determine which platform yields higher engagement and conversion.
    Retention Tracking
Identifies returning users by analyzing unique login patterns over multiple days, providing a snapshot of platform loyalty.
    Automated Data Synthesis
Includes a custom-built generator that creates realistic e-commerce datasets, simulating real-world server logs.

    Analytical Purpose
The analysis is built to support business questions such as:
    What is the global Conversion Rate (CR) of the store?
    Which device type (Mobile or Desktop) should be prioritized for marketing spend?
    Is the platform successful at bringing users back (Retention)?
    Where is the biggest drop-off in the user journey?

    How to Run
1. Generate the dataset first:
    ```bash
    python data_generator.py

Run the analysis to see results and charts:
python analysis.py

Files in Project
data_generator.py - Script to create the synthetic user_events.csv file.

analysis.py - Main analytical script that processes data and generates charts.

user_events.csv - The generated dataset (created after running the generator).

user_behavior_chart.png - A visual dashboard featuring a detailed bar chart that compares traffic across different devices, including exact data labels and optimized scaling for better readability.