# Import necessary libraries
import dash
from dash import dcc, html, State, Input, Output
from sqlalchemy import create_engine
import pandas as pd
import plotly.graph_objs as go
from states_abbreviations import state_abbreviations

# Connect to MySQL database using SQLAlchemy
db_url = "mysql+mysqlconnector://root:""@""/Kidney_Donations"
engine = create_engine(db_url)

# Load data from the database - Kidney Transplants
transplant_query = "SELECT States, `2022` AS Transplants_2022 FROM Kidney_Transplants ORDER BY Transplants_2022 DESC;"
transplant_df = pd.read_sql_query(transplant_query, engine)
transplant_df['States'] = transplant_df['States'].map(state_abbreviations)

# Load data from the database - Kidney Waitlist
waitlist_query = "SELECT State, `2022` AS Waitlisted FROM Kidney_Waitlist_Addition;"
waitlist_df = pd.read_sql_query(waitlist_query, engine)
waitlist_df['State'] = waitlist_df['State'].map(state_abbreviations)

# Calculate total number of people waitlisted
total_waitlisted = waitlist_df['Waitlisted'].sum()

# Calculate total number of kidney transplants in 2022
total_transplants_2022 = transplant_df['Transplants_2022'].sum()

# Load data from the database - Kidney Donor Living
donor_living_query = "SELECT States, `2022` FROM Kidney_Donor_Living;"
donor_living_df = pd.read_sql_query(donor_living_query, engine)
donor_living_df['States'] = donor_living_df['States'].map(state_abbreviations)

# Load data from the database - Kidney Donor Deceased
donor_deceased_query = "SELECT States, `2022` FROM Kidney_Donor_Deceased;"
donor_deceased_df = pd.read_sql_query(donor_deceased_query, engine)
donor_deceased_df['States'] = donor_deceased_df['States'].map(state_abbreviations)

# Calculate total number of living donors and deceased donors in the US for 2022
initial_total_living_donors_us = pd.read_sql_query("SELECT SUM(`2022`) AS Total_Living_Donors FROM Kidney_Donor_Living", engine)['Total_Living_Donors'].values[0]
initial_total_deceased_donors_us = pd.read_sql_query("SELECT SUM(`2022`) AS Total_Deceased_Donors FROM Kidney_Donor_Deceased", engine)['Total_Deceased_Donors'].values[0]

# Calculate initial percentage of living donors for the entire US in 2022
initial_alive_donors_percentage = 'N/A'
if initial_total_living_donors_us + initial_total_deceased_donors_us != 0:
    initial_alive_donors_percentage = f'{(initial_total_living_donors_us / (initial_total_living_donors_us + initial_total_deceased_donors_us)) * 100:.2f}% (USA)'

# Initialize global variables for dynamic updates
total_living_donors_us = initial_total_living_donors_us
total_deceased_donors_us = initial_total_deceased_donors_us

# Load data from the database - Kidney Donor Gender
donor_gender_query = "SELECT Gender, `2022` AS Donors_2022 FROM Kidney_Donor_Gender;"
donor_gender_df = pd.read_sql_query(donor_gender_query, engine)

# Calculate initial gender distribution for the pie chart
initial_gender_distribution = donor_gender_df.set_index('Gender')['Donors_2022']

# Load data from the database - Kidney Recipient Age
recipient_age_query = "SELECT * FROM Kidney_Recipient_Age;"
recipient_age_df = pd.read_sql_query(recipient_age_query, engine)

# Load data from the database - Kidney Donor Age
donor_age_query = "SELECT * FROM Kidney_Donor_Age;"
donor_age_df = pd.read_sql_query(donor_age_query, engine)

# Load data from the database - Organ Waitlist
organ_waitlist_query = "SELECT State, Kidney, Liver, Pancreas, Heart, Lung, Intestine, Abdominal_Wall, VCA_Head_and_Neck, VCA_Upper_Limb, VCA_Uterus FROM Organ_Waitlist;"
organ_waitlist_df = pd.read_sql_query(organ_waitlist_query, engine)
organ_waitlist_df['State'] = organ_waitlist_df['State'].map(state_abbreviations)
# Exclude the 'State' column from the sum
numeric_columns = organ_waitlist_df.drop(columns='State')
# Sum across the numeric columns
sum_values = numeric_columns.sum()

state_store = State('kidney-transplants-map', 'selected_state')

# Create a Dash web application
app = dash.Dash(__name__)

# Define the layout of the web application
app.layout = html.Div([
    html.Div([
        # Title and Year Dropdown
        html.H1("Kidney Transplants in the United States", style={'width': '70%', 'display': 'inline-block'}),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': str(year)} for year in range(1988, 2024)],
            value='2022',
            style={'width': '30%', 'margin-left': 'auto', 'margin-right': '10px', 'display': 'inline-block'}
        ),
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'}),
    
    html.Div([
        # Text BOX
        html.Div([
            html.H4("Every passing moment marks a race against time as someone joins the transplant waitlist.", style={'background-color': '#3C3B3E', 'padding': '10px', 'text-align': 'left', 'margin-bottom': '0px', 'border-radius': '10px'}),
            html.H4("In the span of just 10 minutes, a new name surfaces on the national transplant waitlist.", style={'background-color': '#3C3B3E', 'padding': '10px', 'text-align': 'left', 'margin-top': '-10px', 'border-bottom-left-radius': '10px', 'border-bottom-right-radius': '10px'}),
            html.H4("Consider this: a single organ donation has the incredible potential to impact not one, but eight lives.", style={'background-color': '#3C3B3E', 'padding': '10px', 'text-align': 'left', 'margin-top': '-42px', 'border-bottom-left-radius': '10px', 'border-bottom-right-radius': '10px'}),
        ], style={'width': '50%'}),
        # Clock Div
        html.Div([
            html.Img(src="assets/clock.gif", alt="clock-img", className='clock-img', style={'width': '170px', 'height': '170px', 'margin-left': '190px'}),
        ], className='col-lg-4', style={'display': 'flex', 'align-items': 'center', 'justify-content': 'flex-end'}),
    ], className='row', style={'display': 'flex', 'background-color': '#3C3B3E' , 'margin-top': '20px', 'margin-bottom': '20px', 'height': '300px', 'border-radius': '10px'}),
        
    html.Div([
        # Total Transplants Box
        html.Div([
            html.H3(id='total-transplants', children=f'{total_transplants_2022}', style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-bottom': '0px', 'border-radius': '10px'}),
            html.P('Kidneys Transplanted', style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-top': '-10px', 'border-bottom-left-radius': '10px', 'border-bottom-right-radius': '10px'}),
        ], style={'margin-left': '10%', 'width': '20%'}),
        # Waitlisted Box
        html.Div([
            html.H3(id='total-waitlisted', children=f'{total_waitlisted}', style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-bottom': '0px', 'border-radius': '10px'}),
            html.P('People Added to Waitlist', style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-top': '-10px', 'border-bottom-left-radius': '10px', 'border-bottom-right-radius': '10px'}),
        ], style={'margin-left': '5%', 'width': '20%'}),
        # Alive Donors Percentage Box
        html.Div([
            html.H3(id='alive-donors-percentage', children=initial_alive_donors_percentage, style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-bottom': '0px', 'border-radius': '10px'}),
            html.P('From Living Donors', style={'background-color': 'lightgray', 'padding': '10px', 'text-align': 'center', 'margin-top': '-10px', 'border-bottom-left-radius': '10px', 'border-bottom-right-radius': '10px'}),
        ], style={'margin-left': '5%', 'width': '20%'}),

    dcc.Graph(
        id='donor-gender-pie-chart',
        figure={
            'data': [
                dict(
                    type='pie',
                    labels=['female', 'male'],  # Empty labels to remove legend
                    values=initial_gender_distribution.values,
                    hoverinfo='label+percent',
                    textinfo='value',
                    hole=0.4,
                    marker=dict(colors=['#FF9999', '#66B2FF'], showlegend=False),
                ),
            ],
            'layout': dict(
                title='Living Donor Gender Distribution',
                margin=dict(l=0, r=0, t=50, b=10),
                showlegend=False,
                width=500,
                height=200,
            ),
        },
    ),
    ], style={'display': 'flex', 'justify-content': 'flex-end'}),
    
    dcc.Graph(
        id='kidney-transplants-map',
        figure={
            'data': [
                dict(
                    type='choropleth',
                    colorscale='Blues',
                    reversescale=True,
                    locations=transplant_df['States'],
                    locationmode="USA-states",
                    z=transplant_df['Transplants_2022'],
                    colorbar={'title': 'Number of Transplants', 'zmin': transplant_df['Transplants_2022'].min(), 'zmax': transplant_df['Transplants_2022'].max()},
                ),
            ],
            'layout': dict(
                title='Kidney Transplants by State',
                geo=dict(
                    scope='usa',
                    projection=dict(type='albers usa'),
                    showlakes=True,
                    lakecolor='rgb(255, 255, 255)',
                ),
                margin=dict(l=10, r=10, t=50, b=10),
            ),
        },
    ),

    html.Div([
        # Create side-by-side bar chart for recipient's age vs living donor's age to the layout
        dcc.Graph(
            id='age-comparison-chart',
            figure={
                'data': [
                    {'x': recipient_age_df['Age_Group'], 'y': recipient_age_df['2022'], 'type': 'bar', 'name': 'Recipient', 'marker': {'color': 'rgb(148, 103, 189)'}},
                    {'x': donor_age_df['Age_Group'], 'y': donor_age_df['2022'], 'type': 'bar', 'name': 'Donor', 'marker': {'color': 'rgb(70, 130, 180)'}}
                ],
                'layout': {
                    'title': f'Recipient\'s Age vs Donor\'s Age (2022)',
                    'barmode': 'group',
                    'xaxis': {'title': 'Age Group'},
                    'yaxis': {'title': 'Number of Transplants'},
                }
            },
            style={'width': '48%', 'display': 'inline-block'}  # Adjusted width and added display property
        ),
        # Create organ waitlist bar chart
        dcc.Graph(
            id='organ-waitlist-bar-chart',
            figure={
                'data': [
                    {
                        'x': numeric_columns.columns,
                        'y': numeric_columns.sum(axis=0),
                        'type': 'bar',
                        'marker': {'color': 'lightblue'},
                        'text': numeric_columns.sum(axis=0),
                        'textposition': 'auto',
                    }
                ],
                'layout': {
                    'title': 'Organ Waitlist Across the United States',
                    'xaxis': {'title': 'Organs'},
                    'yaxis': {'title': 'Number of People Waiting for Transplants'},
                    'margin': {'l': 50, 'r': 10, 't': 50, 'b': 50},
                }
            },
            style={'width': '48%', 'display': 'inline-block', 'margin-left': '2%'}  # Adjusted width and added display and margin properties
        ),
    ], style={'display': 'flex'}),
    # Did you Know? Carousel
    html.Div([
        html.Div([
            html.H2("Did You Know?", style={'text-align': 'left', 'margin-right': '10px', 'margin-top': '20px', 'margin-left': '18px'}),
            html.H4(id='did-you-know-text', style={'padding': '10px', 'text-align': 'center', 'border-radius': '10px'}),
        ], style={'height': '400px', 'background-color': '#3C3B3E', 'border-radius': '10px'}),
        dcc.Interval(
            id='carousel-interval',
            interval=7000,  # Update every 5 seconds (adjust as needed)
            n_intervals=0,
        ),
    ], style={'margin-top': '20px'}),
    html.Div([
    # Text on the left side of the button
    html.Div([
        html.H5("20 people die each day waiting for an organ transplant. You can make a difference", style={'text-align': 'left', 'margin-right': '10px', 'margin-top': '10px', 'margin-left': '50px', 'margin-bottom': '10px'}),
        html.H5("Waiting for an organ transplant", style={'text-align': 'left', 'margin-right': '10px', 'margin-left': '50px', 'margin-top': '10px', 'margin-bottom': '10px'}),
        html.H5("You can make a difference", style={'text-align': 'left', 'margin-right': '10px', 'margin-left': '50px', 'margin-top': '10px', 'margin-bottom': '10px'}),
    ], style={'width': '50%', 'display': 'inline-block', 'margin-top': '20px'}),
    
    # Circular button and location on the right side
    html.Div([
        html.A(html.Button('Register Today', id='register-button', n_clicks=0, style={'border-radius': '50%', 'background-color': 'lightblue', 'color': 'black', 'width': '100px', 'height': '100px'}),
               href='https://www.organdonor.gov/sign-up', target='_blank'),
        dcc.Location(id='register-location', refresh=False),
    ], style={'width': '50%', 'display': 'inline-block', 'text-align': 'right', 'margin-top': '25px'}),
], style={'display': 'flex', 'justify-content': 'space-between', 'margin-top': '30px', 'margin-right': '400px'}),

    # Section with three elements at the bottom
    html.Div([
        # Element 1
        html.Div([
            html.Img(src="assets/heart.png", alt='heart-icon', style={'width': '40px', 'height': '40px'}),
            html.P("As of 2022, 170 million people in the US are registered donors", style={'color': 'white'}),
        ], style={'width': '33%', 'text-align': 'center', 'margin-top': '80px', 'margin-bottom': '40px', 'display': 'inline-block'}),

        # Element 2
        html.Div([
            html.Img(src="assets/kidney.png", alt='kidney-icon', style={'width': '40px', 'height': '40px'}),
            html.P("86% of patients waiting are in need of a Kidney", style={'color': 'white'}),
        ], style={'width': '33%', 'text-align': 'center', 'margin-top': '80px', 'margin-bottom': '40px', 'display': 'inline-block'}),

        # Element 3
        html.Div([
            html.Img(src="assets/handshake.png", alt='handshake-icon', style={'width': '40px', 'height': '40px'}),
            html.P("26% of donations are from a living donor", style={'color': 'white'}),
        ], style={'width': '33%', 'text-align': 'center', 'margin-top': '80px', 'margin-bottom': '40px', 'display': 'inline-block'}),
    ], style={'background-color': '#297fb8', 'display': 'flex', 'justify-content': 'space-between', 'border-radius': '10px', 'height': '200px', 'margin-top': '40px', 'margin-bottom': '20px'})
])

# Callback to update the kidney transplants map based on the selected year
@app.callback(
    Output('kidney-transplants-map', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_transplants_map(selected_year):
    # Load data for the selected year
    transplant_query = f"SELECT States, `{selected_year}` AS Transplants FROM Kidney_Transplants;"
    transplant_df = pd.read_sql_query(transplant_query, engine)
    transplant_df['States'] = transplant_df['States'].map(state_abbreviations)

    # Update the figure for the choropleth map
    figure = {
        'data': [
            dict(
                type='choropleth',
                colorscale='Blues',
                reversescale=True,
                locations=transplant_df['States'],
                locationmode="USA-states",
                z=transplant_df['Transplants'],
                colorbar={'title': 'Number of Transplants', 'zmin': transplant_df['Transplants'].min(), 'zmax': transplant_df['Transplants'].max()},
            ),
        ],
        'layout': dict(
            title=f'Kidney Transplants by State ({selected_year})',
            geo=dict(
                scope='usa',
                projection=dict(type='albers usa'),
                showlakes=True,
                lakecolor='rgb(255, 255, 255)',
            ),
            margin=dict(l=10, r=10, t=50, b=10),
        ),
    }

    return figure

# Callback to update total transplants and total waitlisted based on clicked state
@app.callback(
    [Output('total-transplants', 'children'),
     Output('total-waitlisted', 'children')],
    [Input('kidney-transplants-map', 'clickData'),
     Input('year-dropdown', 'value')]
)
def update_totals(click_data, selected_year):
    # Load data for the selected year
    transplant_query = f"SELECT States, `{selected_year}` AS Transplants FROM Kidney_Transplants;"
    transplant_df = pd.read_sql_query(transplant_query, engine)
    transplant_df['States'] = transplant_df['States'].map(state_abbreviations)

    waitlist_query = f"SELECT State, `{selected_year}` AS Waitlisted FROM Kidney_Waitlist_Addition;"
    waitlist_df = pd.read_sql_query(waitlist_query, engine)
    waitlist_df['State'] = waitlist_df['State'].map(state_abbreviations)

    # Initialize state-specific variables
    selected_state = "USA"
    state_transplants = transplant_df[f'Transplants'].sum()
    state_waitlisted = waitlist_df[f'Waitlisted'].sum()

    if click_data is not None:
        selected_state = click_data['points'][0]['location']

        # Retrieve state-specific values
        if selected_state in transplant_df['States'].values:
            state_transplants = transplant_df[transplant_df['States'] == selected_state][f'Transplants'].values[0]

        if selected_state in waitlist_df['State'].values:
            state_waitlisted = waitlist_df[waitlist_df['State'] == selected_state][f'Waitlisted'].values[0]

    return f'{state_transplants} ({selected_state})', f'{state_waitlisted} ({selected_state})'

# Callback to update alive donors percentage based on clicked state and selected year
@app.callback(
    Output('alive-donors-percentage', 'children'),
    [Input('kidney-transplants-map', 'clickData'),
     Input('year-dropdown', 'value')]
)
def update_alive_donors_percentage(click_data, selected_year):
    # Load data for the selected year if it's not None
    if selected_year is not None:
        donor_living_query = f"SELECT States, `{selected_year}` FROM Kidney_Donor_Living;"
        donor_deceased_query = f"SELECT States, `{selected_year}` FROM Kidney_Donor_Deceased;"
        transplant_query = f"SELECT States, `{selected_year}` AS Transplants FROM Kidney_Transplants;"

        donor_living_df = pd.read_sql_query(donor_living_query, engine)
        donor_deceased_df = pd.read_sql_query(donor_deceased_query, engine)
        transplant_df = pd.read_sql_query(transplant_query, engine)

        donor_living_df['States'] = donor_living_df['States'].map(state_abbreviations)
        donor_deceased_df['States'] = donor_deceased_df['States'].map(state_abbreviations)

        total_living_donors_us = donor_living_df[f'{selected_year}'].sum()
        total_deceased_donors_us = donor_deceased_df[f'{selected_year}'].sum()

        # Initialize alive_donors_percentage and state-specific variables
        alive_donors_percentage_usa = 'N/A'
        alive_donors_percentage_state = 'N/A'
        state_living_donors_us = 0
        state_deceased_donors_us = 0

        if total_living_donors_us + total_deceased_donors_us != 0:
            alive_donors_percentage_usa = f'{(total_living_donors_us / (total_living_donors_us + total_deceased_donors_us)) * 100:.2f}% (USA)'

        # Initialize selected_state_full with a default value
        selected_state_full = 'USA'

        if click_data is not None and 'points' in click_data:
            selected_state_abbrev = click_data['points'][0]['location']

            # Convert abbreviation to full name using states_abbreviations.py
            selected_state_full = state_abbreviations.get(selected_state_abbrev, selected_state_abbrev)

            if selected_state_full in donor_living_df['States'].values:
                state_living_donors_us = donor_living_df.loc[donor_living_df['States'] == selected_state_full, f'{selected_year}'].values[0]
            else:
                print(f"State Living Donors {selected_state_full} not found in donor_living_df")
            if selected_state_full in donor_deceased_df['States'].values:
                state_deceased_donors_us = donor_deceased_df.loc[donor_deceased_df['States'] == selected_state_full, f'{selected_year}'].values[0]
            else:
                print(f"State Deceased Donors {selected_state_full} not found in donor_deceased_df")

            # Calculate alive donors percentage for the selected state
            total_donors_state = state_living_donors_us + state_deceased_donors_us

            if total_donors_state != 0:
                alive_donors_percentage_state = f'{(state_living_donors_us / total_donors_state) * 100:.2f}% ({selected_state_full})'

        return alive_donors_percentage_state if alive_donors_percentage_state != 'N/A' else alive_donors_percentage_usa

    else:
        return 'N/A'

# Callback to update the pie chart based on the selected year
@app.callback(
    Output('donor-gender-pie-chart', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_gender_pie_chart(selected_year):
    # Load data for the selected year
    donor_gender_query = f"SELECT Gender, `{selected_year}` AS Donors FROM Kidney_Donor_Gender;"
    donor_gender_df = pd.read_sql_query(donor_gender_query, engine)

    # Calculate gender distribution for the pie chart
    gender_distribution = donor_gender_df.set_index('Gender')['Donors']

    # Update the figure for the pie chart
    figure = {
        'data': [
            dict(
                type='pie',
                labels=['female', 'male'],  # Empty labels to remove legend
                values=gender_distribution.values,
                hoverinfo='label+percent',
                textinfo='value',
                hole=0.4,
                marker=dict(colors=['#FF9999', '#66B2FF'], showlegend=False),
            ),
        ],
        'layout': dict(
            title='Living Donor Gender Distribution',
            margin=dict(l=0, r=0, t=50, b=10),
            showlegend=False,
            width=500,
            height=200
        ),
    }

    return figure

# Callback to update the age comparison chart based on the selected year
@app.callback(
    Output('age-comparison-chart', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_age_comparison_chart(selected_year):
    # Load data for the selected year
    recipient_age_query = f"SELECT * FROM Kidney_Recipient_Age;"
    donor_age_query = f"SELECT * FROM Kidney_Donor_Age;"

    recipient_age_df = pd.read_sql_query(recipient_age_query, engine)
    donor_age_df = pd.read_sql_query(donor_age_query, engine)

    # Create a new figure for the side-by-side bar chart
    figure = {
        'data': [
            {'x': recipient_age_df['Age_Group'], 'y': recipient_age_df[selected_year], 'type': 'bar', 'name': 'Recipient', 'marker': {'color': 'rgb(148, 103, 189)'}},
            {'x': donor_age_df['Age_Group'], 'y': donor_age_df[selected_year], 'type': 'bar', 'name': 'Donor', 'marker': {'color': 'rgb(70, 130, 180)'}}
        ],
        'layout': {
            'title': f'Recipient\'s Age vs Donor\'s Age ({selected_year})',
            'barmode': 'group',
            'xaxis': {'title': 'Age Group'},
            'yaxis': {'title': 'Number of Transplants'},
        }
    }

    return figure

# Callback to update the organ waitlist bar chart based on the selected state
@app.callback(
    Output('organ-waitlist-bar-chart', 'figure'),
    [Input('kidney-transplants-map', 'clickData')]
)
def update_organ_waitlist_chart(click_data):
    # Load data for the selected state
    if click_data is not None and 'points' in click_data:
        selected_state_abbrev = click_data['points'][0]['location']

        # Convert abbreviation to full name using states_abbreviations.py
        selected_state_full = state_abbreviations.get(selected_state_abbrev, selected_state_abbrev)

        # Filter organ waitlist data for the selected state
        state_organ_waitlist = organ_waitlist_df[organ_waitlist_df['State'] == selected_state_full]

        # Create a new figure for the organ waitlist bar chart
        figure = {
            'data': [
                {
                    'x': state_organ_waitlist.columns[1:],  # Exclude 'State' column
                    'y': state_organ_waitlist.iloc[0, 1:],
                    'type': 'bar',
                    'marker': {'color': 'lightblue'},
                    'text': state_organ_waitlist.iloc[0, 1:],
                    'textposition': 'auto',
                }
            ],
            'layout': {
                'title': f'Organ Waitlist in {selected_state_full}',
                'xaxis': {'title': 'Organs'},
                'yaxis': {'title': 'Number of People Waiting for Transplants'},
                'margin': {'l': 50, 'r': 10, 't': 50, 'b': 50},
            }
        }

        return figure
    else:
        # If no state is selected, show the overall organ waitlist
        overall_organ_waitlist = {
            'x': numeric_columns.columns,
            'y': numeric_columns.sum(axis=0),
            'type': 'bar',
            'marker': {'color': 'lightblue'},
            'text': numeric_columns.sum(axis=0),
            'textposition': 'auto',
        }

        figure = {
            'data': [overall_organ_waitlist],
            'layout': {
                'title': 'Organ Waitlist Across the United States',
                'xaxis': {'title': 'Organs'},
                'yaxis': {'title': 'Number of People Waiting for Transplants'},
                'margin': {'l': 50, 'r': 10, 't': 50, 'b': 50},
            }
        }

        return figure

@app.callback(
    Output('did-you-know-text', 'children'),
    [Input('carousel-interval', 'n_intervals')]
)
def update_did_you_know_text(n_intervals):
    # Define a list of texts to rotate through
    did_you_know_texts = [
        "Living donors can make a significant impact, with one donor potentially saving up to eight lives through solid organ donation and improving the lives of up to 75 people through tissue donation",
        "Organ donation, both from deceased and living donors, is a safe and well-regulated process",
        "The suitability of tissue donors and organs is determined on a case-by-case basis. Organs and tissues can be donated by individuals of any age, including newborns, children, and adults",
        "Less than 1% of donors end up meeting the specific medical criteria to donate their organs and tissue",
        "Donating organs is completely free, and the donor's family will not be charged for any medical expenses associated with the donation process"
    ]

    # Rotate through the texts
    current_text = did_you_know_texts[n_intervals % len(did_you_know_texts)]

    # Return the current text
    return html.H4(current_text, style={'padding': '10px', 'text-align': 'left', 'border-radius': '10px'})

# Callback to update the location based on button click
@app.callback(
    Output('register-location', 'pathname'),
    [Input('register-button', 'n_clicks')]
)
def update_registration_location(n_clicks):
    # Change the location dynamically if needed
    return '/sign-up' if n_clicks else '/'

# Run the Dash web application
if __name__ == '__main__':
    app.run_server(debug=True)