from dash import html
import dash_bootstrap_components as dbc

login_page = html.Div([
    dbc.Card(
        dbc.CardBody([
            html.Div([
                html.H1(children='Log in!',
                        style={'fontWeight': 'bold',
                               'fontSize': 40, 'fontFamily': 'italic',
                               'color': 'black', 'paddingTop': '10px', 'lineHeight': '1.5',
                               'textAlign': 'left'}),
                html.H1(children='Welcome to Acuzense :)',
                        style={'fontWeight': 'bold',
                               'fontSize': 40, 'fontFamily': 'italic',
                               'color': 'black', 'paddingTop': '5px', 'lineHeight': '1.5',
                               'textAlign': 'left'}),
                html.P(children='''To keep connected with us please login with your personal
                                                information by email/mobile and password''',
                       style={'maxWidth': '90%', 'lineHeight': '1.5',
                              'fontSize': 15, 'fontFamily': 'italic',
                              'color': 'black', 'paddingTop': '0px',
                              'textAlign': 'left'}),
            ], style={'paddingTop': '10px', 'textAlign': 'left',
                      'paddingLeft': '20px', 'paddingRight': '20px'}),

            html.Div([
                dbc.Label("Username or Email", html_for="username-input",
                          style={'color': '#6e6261', 'fontFamily': 'italic', 'font-size': 20}),
                dbc.Input(type="email", id="username-input", size="lg", placeholder="Enter Email"),
                dbc.FormText("We only accept Email..."),
                dbc.FormFeedback("That looks like a Email address :-)", type="valid"),
                dbc.FormFeedback(
                    "Sorry, we only accept Email for some reason...",
                    type="invalid",
                ),
            ], style={'paddingTop': '20px', 'textAlign': 'left',
                      'paddingLeft': '20px', 'paddingRight': '20px'}),

            html.Div([
                dbc.Label("Password", html_for="password-input",
                          style={'color': '#6e6261', 'fontFamily': 'italic', 'font-size': 20}),
                dbc.InputGroup([
                    dbc.Input(type="password", id="password-input", size="lg", placeholder="Enter password"),
                    dbc.InputGroupText(html.I(id="password-icon", className="bi bi-eye-slash")),
                ], id="password-group", size="lg"),
            ], style={'paddingTop': '10px', 'textAlign': 'left',
                      'paddingLeft': '20px', 'paddingRight': '20px'}),

            html.Div([
                dbc.Button("Sign In", id='sign_up_button', n_clicks=0, size="lg", color="primary"),
            ], style={'paddingTop': '20px', 'textAlign': 'center'}),
            html.Br(),
            html.Div(id='authentication_output', children=[],
                     style={'textAlign': 'center', 'height': '5px',
                            'color': 'red',
                            'fontSize': '20px'}),
        ], className='text-center'),

        style={'padding': '25px', 'width': '80%', 'margin': '20px',
               'backgroundColor': 'rgba(255, 255, 255, 0.5)'}
    ),
], style={'textAlign': 'center', 'justifyContent': 'center', 'Height': "100vh",
          'alignItems': 'center', "backgroundImage": 'url("assets/bg_card.jpg")',
          'backgroundRepeat': 'no-repeat',
          'backgroundPosition': 'center',
          'backgroundAttachment': 'fixed',
          'backgroundSize': 'cover',
          'display': 'flex', 'overflow': 'hidden'})