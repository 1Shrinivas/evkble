from dash import html, dcc
import dash_bootstrap_components as dbc

dashboard_page = html.Div([
    dbc.Container([
        html.Div([
            dcc.Store(id='stored-dataframe'),
            dbc.Row([
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.I(className="bi bi-people-fill",
                                                       style={"fontSize": "2rem", "color": "#000"}),
                                                html.P("Subscribers", className="card-text",
                                                       style={"color": "#000"}),
                                                html.P(id="Subscribers-id", className="card-text",
                                                       style={"color": "#000", 'fontWeight': 'bold'}),
                                            ],
                                            style={"textAlign": "center", 'overflow': 'hidden',
                                                   'wordWrap': 'break-word', 'height': '100%'}
                                        )
                                    ]
                                )
                            ],
                            className="mb-4",
                            style={"maxWidth": "540px", "border": "1px solid #c93a6e", "borderRadius": "10px",
                                   'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'},
                            color="ffffff",
                            outline=True
                        )
                    ],
                    xs=12, sm=12, md=6, lg=2, xl=2
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.I(className="bi bi-watch",
                                                       style={"fontSize": "2rem", "color": "#000"}),
                                                html.P("Measurements", className="card-text",
                                                       style={"color": "#000"}),
                                                html.P(id="Measurements-id", className="card-text",
                                                       style={"color": "#000", 'fontWeight': 'bold'}),
                                            ],
                                            style={"textAlign": "center", 'overflow': 'hidden',
                                                   'wordWrap': 'break-word', 'height': '100%'}
                                        )
                                    ]
                                )
                            ],
                            className="mb-4",
                            style={"maxWidth": "540px", "border": "1px solid #c93a6e", "borderRadius": "10px",
                                   'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'},
                            color="ffffff",
                            outline=True
                        )
                    ],
                    xs=12, sm=12, md=6, lg=2, xl=2
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.I(className="bi bi-gender-male",
                                                       style={"fontSize": "2rem", "color": "#000"}),
                                                html.P("Males", className="card-text",
                                                       style={"color": "#000"}),
                                                html.P(id="Males-id", className="card-text",
                                                       style={"color": "#000", 'fontWeight': 'bold'}),
                                            ],
                                            style={"textAlign": "center", 'overflow': 'hidden',
                                                   'wordWrap': 'break-word', 'height': '100%'}
                                        )
                                    ]
                                )
                            ],
                            className="mb-4",
                            style={"maxWidth": "540px", "border": "1px solid #c93a6e", "borderRadius": "10px",
                                   'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'},
                            color="ffffff",
                            outline=True
                        )
                    ],
                    xs=12, sm=12, md=6, lg=2, xl=2
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.I(className="bi bi-gender-female",
                                                       style={"fontSize": "2rem", "color": "#000"}),
                                                html.P("Females", className="card-text",
                                                       style={"color": "#000"}),
                                                html.P(id="Females-id", className="card-text",
                                                       style={"color": "000", 'fontWeight': 'bold'}),
                                            ],
                                            style={"textAlign": "center", 'overflow': 'hidden',
                                                   'wordWrap': 'break-word', 'height': '100%'}
                                        )
                                    ]
                                )
                            ],
                            className="mb-4",
                            style={"maxWidth": "540px", "border": "1px solid #c93a6e", "borderRadius": "10px",
                                   'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'},
                            color="ffffff",
                            outline=True
                        )
                    ],
                    xs=12, sm=12, md=6, lg=2, xl=2
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.I(className="bi bi-gender-trans",
                                                       style={"fontSize": "2rem", "color": "#000"}),
                                                html.P("Transgenders", className="card-text",
                                                       style={"color": "#000"}),
                                                html.P(id="Transgenders-id", className="card-text",
                                                       style={"color": "#000", 'fontWeight': 'bold'}),
                                            ],
                                            style={"textAlign": "center", 'overflow': 'hidden',
                                                   'wordWrap': 'break-word', 'height': '100%'}
                                        )
                                    ]
                                )
                            ],
                            className="mb-4",
                            style={"maxWidth": "540px", "border": "1px solid #c93a6e", "borderRadius": "10px",
                                   'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)'},
                            color="ffffff",
                            outline=True
                        )
                    ],
                    xs=12, sm=12, md=6, lg=2, xl=2
                ),
            ], justify="around", className="g-3"),

        ], style={'margin': '20px'}, className="g-3"),

        html.Div(
            [
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [
                                html.Div([
                                    dbc.Label("Location", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Global", "value": "All"},
                                            {"label": "Finger", "value": "finger"},
                                            {"label": "Wrist", "value": "wrist"},
                                            {"label": "Chest", "value": "chest"}
                                        ],
                                        value="All",
                                        id="location-radio",
                                        inline=True,
                                        className="mb-3",
                                    ),
                                    dbc.Label("Gender", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.RadioItems(
                                        options=[
                                            {"label": "Global", "value": "Global"},
                                            {"label": "Male", "value": "male"},
                                            {"label": "Female", "value": "female"},
                                            {"label": "Transgender", "value": "trans"},
                                        ],
                                        value="Global",
                                        id="gender-radio",
                                        inline=True,
                                        className="mb-3",
                                    ),
                                    dbc.Label("Age", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Input(id="age-min-input", type="number", min=0, max=100, step=1,
                                                          value=18),
                                                width=3,
                                                className="mr-1",
                                            ),
                                            dbc.Col(
                                                dbc.Input(id="age-max-input", type="number", min=0, max=100, step=1,
                                                          value=100),
                                                width=3,
                                            ),
                                        ],
                                        className="mb-3",
                                    ),
                                    dbc.Label("Height (Cms)", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Input(id="height-min-input", type="number", min=140, max=200,
                                                          step=1,
                                                          value=140),
                                                width=3,
                                                className="mr-1",
                                            ),
                                            dbc.Col(
                                                dbc.Input(id="height-max-input", type="number", min=140, max=200,
                                                          step=1,
                                                          value=200),
                                                width=3,
                                            ),
                                        ],
                                        className="mb-3",
                                    ),
                                    dbc.Label("Weight (Kgs)", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Input(id="weight-min-input", type="number", min=30, max=150, step=1,
                                                          value=30),
                                                width=3,
                                                className="mr-1",
                                            ),
                                            dbc.Col(
                                                dbc.Input(id="weight-max-input", type="number", min=30, max=150, step=1,
                                                          value=150),
                                                width=3,
                                            ),
                                        ],
                                        className="mb-3",
                                    ),
                                    dbc.Label("Systolic Blood Pressure", style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Input(id="sys-min-input", type="number", min=60, max=250, step=1,
                                                          value=60),
                                                width=3,
                                                className="mr-1",
                                            ),
                                            dbc.Col(
                                                dbc.Input(id="sys-max-input", type="number", min=60, max=250, step=1,
                                                          value=250),
                                                width=3,
                                            ),
                                        ],
                                        className="mb-3",
                                    ),
                                    dbc.Label("Diastolic Blood Pressure",
                                              style={"color": "#000", "fontWeight": "bold"}),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Input(id="dia-min-input", type="number", min=30, max=150, step=1,
                                                          value=40),
                                                width=3,
                                                className="mr-1",
                                            ),

                                            dbc.Col(
                                                dbc.Input(id="dia-max-input", type="number", min=30, max=150, step=1,
                                                          value=150),
                                                width=3,
                                            ),
                                        ],
                                        className="mb-3",
                                    ),
                                    dbc.Button("Apply filter", id="submit-filter", n_clicks=0, color="primary",
                                               className="mt-3"),
                                ], style={'margin': '20px', "height": "300px", "overflowY": "auto"})

                            ],
                            title="Filter",
                            item_id="item-1",
                        ),
                    ],
                    id="accordion",
                    active_item="",
                ),
            ],
            style={'margin': '20px'},
            className="g-3"
        ),
        html.Div(id="datatable-info"),
        html.Div(id="output-graphs-div")

    ], fluid=True),
]),
