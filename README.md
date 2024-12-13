# upliance_data_analyst_sara
Description of Assignment:
- The objective of this assignment is to analyze datasets related to user behavior,
cooking preferences, and order trends.
- You will work with three datasets: UserDetails, CookingSessions, and
OrderDetails.
- The task involves cleaning and merging the data, analyzing the relationship between
cooking sessions and user orders, identifying popular dishes, and exploring
demographic factors that influence user behavior.
- Additionally, you will create visualizations to showcase key insights and write a report
summarizing your findings and business recommendations.


This project is a comprehensive Python-based pipeline to clean, analyze, and visualize data for a cooking and ordering platform. The code integrates user details, cooking sessions, and order details to uncover insights into user behavior, session participation, and popular dishes.

## Features

1. *Data Cleaning*:
   - Handles missing values by imputation or removal.
   - Removes duplicates and standardizes column names.
   - Ensures consistent data types, such as date and numeric formats.
  
2. *Data Merging*:
   - Combines datasets based on common keys (user_id and session_id).
   - Produces a unified dataset for in-depth analysis.

3. *Analysis*:
   - Calculates user participation rates in cooking sessions.
   - Identifies repeat orders and popular dishes.
   - Explores demographic influences on user behavior.

4. *Visualization*:
   - Bar charts for total orders by age group.
   - Heatmaps for dish preferences by age group.
   - Bar charts for session participation by location.
## Installation Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>

2. Install the required dependencies:

   ```bash
   pip install pandas matplotlib seaborn openpyxl
 Ensure the input file Assignment.xlsx is available in the root directory.

3. Usage
Run the script:
   ```bash
   python main.py


Outputs include:


Cleaned datasets (cleaned_user_details.csv, cleaned_cooking_sessions.csv, cleaned_order_details.csv).
Merged dataset (merged_dataset.csv).
Analysis results (participation_rate.csv, repeat_orders.csv, daily_sessions.csv).
Visualizations (total_orders_by_age_group.png, dishes_by_age_group_heatmap.png, sessions_by_location.png).


File Descriptions

Input Files:

UserDetails.csv: Contains user demographics and total orders.

CookingSessions.csv: Details of cooking sessions including timestamps.

OrderDetails.csv: Information on user orders and ratings.


Output Files:

Cleaned and merged datasets for further analysis.

CSV files summarizing participation rates, popular dishes, and demographics.

PNG files for visual representations.


## Contributing
Contributions are welcome! 
