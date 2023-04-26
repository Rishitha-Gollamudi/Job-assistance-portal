# SI507-housing-assistance-portal

#Python Packages to be installed separately
Flask
Requests

#Instructions for running the code

App.py should be executed to launch the website. Before running the code, login to the Glassdoor account as it is required to scrape data from Glassdoor. The credentials are provided in the final project report. Store the API keys for Job salary data API and JSearch in the ‘.env’ file. The procedure is mentioned in the final project report.

#Instructions on how to interact with the system

Enter the job role and location in the home page. All the job listings will be displayed in a tabular format. Data can be sorted by any of the job attributes such as job posting date etc. and can download the data in different formats. Clicking on Popular questions & Salary statistics redirects the user to popular interview questions and salary statistics for that role and location.

#Data Structure

I used a tree data structure to save all the processed data. Job data related to all searches are stored as children to the root node. Each search data will have the company names from job listings and interview questions and salary statistics as child nodes. Every company node will have job attributes like job role, job description etc. as the child nodes. Below figure shows the tree structure. Tree.json contains the cached data in a tree format. Json_saving_reading.py can be used to save a tree in json format and convert a json tree file to a tree object.

![Image of Yaktocat](https://github.com/Rishitha-Gollamudi/Job-assistance-portal/blob/main/extra_files/SI_tree%20(2).jpeg)
