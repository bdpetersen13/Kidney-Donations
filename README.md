
# United States Kidney Donations and Transplants Data Analysis and Visualization

## Overview


This repository contains the source code and data for a web application that analyzes and visualizes kidney transplants and donation data in the United States. The application is built using an SQL database for data storage, Python for backend logic, and the Dash web framework for the front end.

https://github.com/bdpetersen13/Kidney-Donations/assets/89234922/d1f7fdd9-4589-4a87-b455-884f082e901a

## Project Structure

* database_scripts/: Contains SQL scripts for database creation and data insertion.

* backend/: Includes Python scripts for backend logic and data processing.

* frontend/: Houses Dash web application files for interactive data visualization.
## Data

### Data Sources
The project uses the following datasets where the data was gathered from the Organ Procurement & Transplantation Network and the United Network for Organ Sharing:

* kidney_transplant_by_state.csv: Kidney transplant data by state and year.

* repeat_kidney_transplant.csv: Repeat kidney transplant data by state, diabetes type, and year.

* kidney_transplant_by_donor_age.csv: Kidney transplant data by donor age, state, and year.

* kidney_transplant_by_recipient_age.csv: Kidney transplant data by recipient age, state, and year.

* kidney_donor_relationship.csv: Kidney donor relationship data by state, diabetes type, and year.

* kidney_transplant_diabetes_status.csv: Kidney transplant diabetes status data by state, diabetes type, and year.

* living_or_deceased_states.csv: Data on living and deceased donors by state and year.

* organ_waitlist.csv: Organ waitlist data by state and time on the waitlist.

### Data Details

The data provides detailed information on kidney transplants, including state-wise breakdowns, donor demographics, recipient age, diabetes status, and more.


## Getting Started

1. ``` git clone https://github.com/bdpetersen13/kidney-transplant-analysis.git ```

2. Execute the SQL scripts in database_scripts/ to set up the database and populate it with the provided data.

3. Install the required Python packages, run the backend server, frontend setup

4. Access the web application 

## Interactive Webpage

The web application includes:

* A color-coded map of the United States based on the selected metric.

* Charts displaying trends over time for key metrics.

* Dynamic information updates when clicking on a specific state on the map.
## Future Enhancements

* Incorporate additional data sources for a more comprehensive analysis.

* Implement user authentication for data security.

* Enhance data visualization and interactivity features.

As a side note, depending on the size of your window, some information and widgets may appear off the screen.

## Roadmap

* Code Organization: Currently, all the main functionality of the application is inside one file, creating a long and complex codebase. The first step in improving the application will be to break down the codebase into smaller modules and functions to improve readability and maintainability.

* Error  Handling: Adding error handling will make the application more robust and better at troubleshooting issues that might occur during database queries.

* Inline CSS Styling: Some aspects of the code have inline CSS styling, and this should be moved to the styles.css file.

* Global Variables: Update the codebase and modify the global variables to use session or cache to store and manage shared data. Global variables can often lead to unexpected behavior.

* Security: When the application is ready for deployment, ensure it follows best security practices, such as setting up HTTPS, securing database connections, etc.

* Debug mode: Modify debug mode in production application as it could expose sensitive information and security vulnerabilities.

## Contributing

Contributions are always welcome!

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions, please open an issue.

