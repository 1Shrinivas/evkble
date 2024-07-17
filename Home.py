from dash import html
import dash_bootstrap_components as dbc

Home_page = html.Div([
    html.Div([
        html.Div([
            html.Div(style={'position': 'absolute', 'width': '100%', 'height': '100%',
                            'backgroundImage': 'url("assets/w-qjCHPZbeXCQ-unsplash.jpg")',
                            'backgroundSize': 'cover', 'backgroundPosition': 'center',
                            'opacity': '0.8'}),
            html.Div([
                html.H1('Unleash the Power of Continuous Health Remote Monitoring',
                        style={'marginLeft': '50px', 'color': '#ffffff', 'fontWeight': 'bold',
                               'fontSize': '40px', 'lineHeight': '1.5',
                               'fontFamily': 'sans-serif', 'textAlign': 'left', 'maxWidth': '80%'}),
                html.P('''Our platform offers an integrated solution for continuous monitoring of vital signs,
                         delivering real-time tracking and analysis of key health metrics including heart rate, blood
                          pressure, and oxygen
                saturation. This technology allows for instant feedback on health status, enabling prompt interventions
                and personalized healthcare management.''',
                       style={'marginLeft': '50px', 'color': '#ffffff',
                              'fontFamily': 'sans-serif', 'max-width': '60%',
                              'textAlign': 'left', 'lineHeight': '1.5', 'fontSize': '20px'}),
            ], style={'position': 'relative', 'textAlign': 'center', 'paddingTop': '50px',
                      'paddingBottom': '30px', 'backgroundColor': 'transparent'}),
        ], style={'position': 'relative', 'width': '100%', 'height': '100%'}),
        html.Div([
            html.P("FEATURES",
                   style={'textAlign': 'center', 'color': '#5f38f6', 'lineHeight': '1.5'}),
            html.H1("Discover The Best Features",
                    style={'textAlign': 'center', 'fontWeight': 'bold', 'lineHeight': '1.5',
                           'color': '#000000', 'fontSize': '40px'}),
            html.P(
                "Experience a seamless journey while exploring continuous vital measurement at your finger tips.",
                style={'textAlign': 'center', 'lineHeight': '1.5',
                       'color': '#6e6261', 'fontSize': '20px'}),
            html.Div([
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.Div([
                                    html.H3("User-Friendly Interface",
                                            style={'textAlign': 'left', 'marginLeft': '50px'}),
                                    html.P(
                                        "Easily navigate through the website and access articles and publications on "
                                        "continuous blood pressure monitoring.",
                                        style={'textAlign': 'left', 'marginLeft': '50px'}),
                                ], className="feature-card"),
                            ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                                      'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin': '10px',
                                      'overflow': 'hidden', 'wordWrap': 'break-word', 'height': '100%'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                        dbc.Col(
                            html.Div([
                                html.Div([
                                    html.H3("Advanced Search Functionality",
                                            style={'textAlign': 'left', 'marginLeft': '50px'}),
                                    html.P(
                                        "Effortlessly find specific articles or publications based on keywords, "
                                        "authors, or topics.",
                                        style={'textAlign': 'left', 'marginLeft': '50px'}),
                                ], className="feature-card"),
                            ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                                      'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin': '10px',
                                      'overflow': 'hidden', 'wordWrap': 'break-word', 'height': '100%'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                    ],
                    className="g-3",
                    style={'marginBottom': '20px'}
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                html.Div([
                                    html.H3("Personalized Recommendations",
                                            style={'textAlign': 'left', 'marginLeft': '50px'}),
                                    html.P(
                                        "Receive tailored suggestions for articles and publications based on your "
                                        "interests and reading history.",
                                        style={'textAlign': 'left', 'marginLeft': '50px'}),
                                ], className="feature-card"),
                            ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                                      'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin': '10px',
                                      'overflow': 'hidden', 'wordWrap': 'break-word', 'height': '100%'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                        dbc.Col(
                            html.Div([
                                html.Div([
                                    html.H3("Interactive Charts and Graphs",
                                            style={'textAlign': 'left', 'marginLeft': '50px'}),
                                    html.P(
                                        "Visualize blood pressure data with interactive charts and graphs for better "
                                        "understanding and analysis.",
                                        style={'textAlign': 'left', 'marginLeft': '50px'}),
                                ], className="feature-card"),
                            ], style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px',
                                      'box-shadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin': '10px',
                                      'overflow': 'hidden', 'wordWrap': 'break-word', 'height': '100%'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                    ],
                    className="g-3",
                    style={'marginBottom': '20px'}
                ),
            ])
        ], style={'textAlign': 'center', 'padding': '50px',
                  'background-color': '#eff0f2'}),
        html.Div([
            html.H1('Revolutionize Blood Pressure Monitoring',
                    style={'color': '#f5f5f5', 'fontWeight': 'bold',
                           'fontSize': '40px', 'lineHeight': '2',
                           'fontFamily': 'sans-serif', 'textAlign': 'center'}),
            html.P('Discover the Latest Research and Insights',
                   style={'color': '#f5f5f5',
                          'fontFamily': 'sans-serif',
                          'textAlign': 'center', 'lineHeight': '1.5', 'fontSize': '20px'}),
            html.Div([
                dbc.Button("Read More", className="me-2",
                           style={"background-color": "#291477", "border": "2px #291477", 'fontWeight': 'bold',
                                  "color": "white", "width": "180px", "border-radius": "40px", "height": "60px"}),
            ], style={'textAlign': 'center', 'paddingTop': '30px', 'paddingBottom': '20px'}),
        ], style={'textAlign': 'center', 'paddingTop': '60px', 'paddingBottom': '50px',
                  'backgroundColor': '#000000'}),

        html.Div(
            dbc.Container([
                dbc.Row([
                    dbc.Col([
                        html.P("FAQ", style={'textAlign': 'left', 'color': '#5f38f6', 'fontWeight': 'bold',
                                             'lineHeight': '1.5', 'paddingLeft': '20px'}),
                        html.H1("Common questions",
                                style={'textAlign': 'left', 'fontWeight': 'bold', 'lineHeight': '1.5',
                                       'color': '#000000', 'fontSize': '40px','paddingLeft': '20px'}),
                        html.P('''Here are some of the most common questions that we get.''',
                               style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '50%', 'color': '#6e6261',
                                      'fontSize': '20px', 'paddingLeft': '20px'}),
                    ],
                        className="text-center",
                        xs=12, sm=12, md=3, lg=3, xl=3),
                    dbc.Col([
                        html.H3("What is continuous blood pressure monitoring?",
                                style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                                       'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
                        html.P(
                            '''Continuous blood pressure monitoring is a method of measuring blood pressure at 
                            regular intervals throughout the day and night, providing a more comprehensive 
                            understanding of a person's blood pressure patterns.''',
                            style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '80%', 'color': '#6e6261',
                                   'paddingLeft': '20px'}),
                        html.H3("Why is continuous blood pressure monitoring important?",
                                style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                                       'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
                        html.P(
                            '''Continuous blood pressure monitoring allows for a more accurate assessment of blood 
                            pressure fluctuations, helping to identify potential health issues and optimize treatment 
                            plans.''',
                            style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '80%', 'color': '#6e6261',
                                   'paddingLeft': '20px'}),
                        html.H3("How does continuous blood pressure monitoring work?",
                                style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                                       'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
                        html.P(
                            '''Continuous blood pressure monitoring typically involves wearing a device that 
                            automatically inflates and deflates to measure blood pressure at regular intervals. The 
                            device records the data, which can then be analyzed by healthcare professionals.''',
                            style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '80%', 'color': '#6e6261',
                                   'paddingLeft': '20px'}),
                        html.H3("Who can benefit from continuous blood pressure monitoring?",
                                style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                                       'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
                        html.P(
                            '''Continuous blood pressure monitoring can benefit individuals with hypertension, 
                            cardiovascular diseases, or those at risk of developing such conditions. It can also be 
                            useful for athletes and individuals interested in tracking their blood pressure trends.''',
                            style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '80%', 'color': '#6e6261',
                                   'paddingLeft': '20px'}),
                        html.H3("Is continuous blood pressure monitoring accurate?",
                                style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                                       'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
                        html.P(
                            '''Continuous blood pressure monitoring devices have been shown to provide accurate 
                            measurements when compared to traditional cuff-based methods. However, it is important to 
                            follow the manufacturer's instructions and consult with healthcare professionals for 
                            proper usage and interpretation of the data.''',
                            style={'textAlign': 'left', 'lineHeight': '1.5', 'maxWidth': '80%', 'color': '#6e6261',
                                   'paddingLeft': '20px'}),
                    ], xs=12, sm=12, md=6, lg=9, xl=9),
                ], className="my-4"),

            ], fluid=True)
        ),
        html.Div([
            html.H1('Acuzense',
                    style={'color': '#f5f5f5', 'fontWeight': 'bold',
                           'fontSize': '40px', 'lineHeight': '1.5',
                           'fontFamily': 'sans-serif', 'textAlign': 'center'}),
            html.Div(
                children=[
                    html.P("Home", style={'marginRight': '15px', 'color': '#f5f5f5', 'fontSize': '18px'}),
                    html.P("Articles", style={'margin-right': '15px', 'color': '#f5f5f5', 'fontSize': '18px'}),
                    html.P("Publications", style={'margin-right': '15px', 'color': '#f5f5f5', 'fontSize': '18px'}),
                    html.P("Continuous Monitoring",
                           style={'margin-right': '15px', 'color': '#f5f5f5', 'fontSize': '18px'}),
                    html.P("Contact", style={'margin-right': '15px', 'color': '#f5f5f5', 'fontSize': '18px'}),
                ],
                style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
            ),
            html.Hr(style={'size': '20', 'borderColor': '#f5f5f5', 'borderHeight': "20vh",
                           'margin-left': '70px', 'margin-right': '70px', 'borderWidth': '3px'}),
            html.Div([
                html.P('© 2023 Asmaitha, All Rights Reserved.',
                       style={'color': '#f5f5f5', 'fontSize': '15px', 'textAlign': 'left', 'display': 'inline-block'}),
                html.Div([
                    html.A(html.I(className="bi bi-twitter", style={'color': '#f5f5f5', 'fontSize': '24px'}), href='#',
                           style={'margin-right': '30px'}),
                    html.A(html.I(className='bi bi-instagram', style={'color': '#f5f5f5', 'fontSize': '24px'}),
                           href='#',
                           style={'margin-right': '30px'}),
                    html.A(html.I(className='bi bi-facebook', style={'color': '#f5f5f5', 'fontSize': '24px'}), href='#',
                           style={'margin-right': '30px'}),
                ], style={'display': 'inline-block', 'textAlign': 'right'}),
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '10px',
                      'margin-left': '70px', 'margin-right': '70px'})
        ], style={'text-align': 'center', 'padding-top': '50px', 'padding-bottom': '25px',
                  'background-color': '#000000'}),
    ]),
], style={'height': '100vh'}, className='g-3')
