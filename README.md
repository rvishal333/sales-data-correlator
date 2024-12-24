Streamlit Application for Statistical Analysis of Revenue by Location

Overview

This project provides a streamlined way to analyze the statistical significance between location and revenue for a supermarket chain. It consists of two Python scripts:

generate_data.py: Creates a CSV file containing sample data.

main_app.py: Runs the Streamlit application that processes the generated CSV and performs statistical analysis.

Getting Started

Prerequisites

Make sure you have the following installed on your system:

Python 3.7 or later

Required Python libraries (install via requirements.txt):

pip install -r requirements.txt

Required Libraries

The application depends on the following Python packages:

streamlit

pandas

scipy

numpy

How to Use the Application

Step 1: Generate the CSV File

Run the generate_data.py script to generate a sample CSV file containing data for analysis. This file will include variables such as location and revenue.

Command:

python generate_data.py

Output:

A CSV file named supermarket_data.csv will be created in the project directory.

Step 2: Run the Streamlit Application

Use the main_app.py script to start the Streamlit application. This program will load the generated CSV file and perform statistical analysis to identify the significance of the location variable in relation to revenue.

Command:

streamlit run main_app.py

Features:

Upload the generated supermarket_data.csv file.

Visualize data distributions for location and revenue.

Perform statistical tests to evaluate the significance of the relationship.

Display results in an interactive and user-friendly interface.

File Descriptions

generate_data.py

This script generates a synthetic dataset with the following columns:

Location: Represents different store locations.

Revenue: Simulated revenue figures for each location.

main_app.py

This script launches the Streamlit application, providing an interface to analyze the data for statistical significance. It uses:

T-tests, ANOVA, or other relevant statistical methods.

Interactive visualizations to better understand the relationship between variables.

Example Workflow

Run generate_data.py to create supermarket_data.csv.

Start the application with streamlit run main_app.py.

Upload the generated CSV file to the app.

View results and visualizations in the browser.

Contributions

Feel free to contribute to this project by submitting pull requests or reporting issues.

License

This project is licensed under the MIT License. See the LICENSE file for details.
