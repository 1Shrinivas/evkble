import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.io as pio
import plotly
import plotly.express as px
import plotly.graph_objects as go
from pymongo import MongoClient
import re
import flask
import secrets
from flask import session
import pandas as pd
import numpy as np
import uuid
import time
import signal
import sys
import threading
from werkzeug.serving import make_server
from Home import Home_page
from Login import login_page
from dashboard import dashboard_page
from Report_page import report_page
from fda import FDA_Report

Mongo_client = MongoClient('mongodb+srv://puneetgani:puneetgani@quentdb.04y5a6m.mongodb.net/test')
database = Mongo_client['application_db']
user_access_collection = database['user_access']
MetaData_collection = database['metadata']

dataframe = pd.read_csv(r"datas/full_data_chest_finger_wrist.csv")

server = flask.Flask(__name__)

app = dash.Dash(__name__,
                server=server,
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}])

app.server.secret_key = secrets.token_hex(16)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/Home", id="nav-home"),
                        style={"fontSize": "18px", "padding": "10px"}),
            dbc.NavItem(dbc.NavLink("Presentation", href="/Report", id="nav-report"),
                        style={"fontSize": "18px", "padding": "10px"}),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/Dashboard", id="nav-dashboard"),
                        style={"fontSize": "18px", "padding": "10px"}),
            dbc.NavItem(dbc.NavLink("Continuous monitoring", href="/Continuous-monitoring",
                                    id="nav-continuous-monitoring"), style={"fontSize": "18px", "padding": "10px"}),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact", id="nav-contact"),
                        style={"fontSize": "18px", "padding": "10px"}),
        ],
        brand=html.Div(
            [
                html.Img(src="assets/FB_IMG_1702904656655.jpg", height="50px"),
                html.Span("Acuzense",
                          style={"marginLeft": "20px", "verticalAlign": "middle", 'fontWeight': 'bold',
                                 'textAlign': 'center', 'color': '#c93a6e',
                                 'fontSize': 30}),
            ],
            style={"display": "flex", "alignItems": "center"}
        ),
        brand_href="https://asmaitha.com/",
        color="#f8f9fa",
        dark=False,
        className="sticky-top"
    ),
    html.Div(id='page-content'),
    html.Div(id='hidden-div', style={'display': 'none'})
], style={'minHeight': "100vh"})


@app.callback(
    [Output(f'nav-{name}', 'style') for name in ['home', 'report', 'dashboard', 'continuous-monitoring', 'contact']],
    [Input('url', 'pathname')]
)
def update_active_links(pathname):
    default_style = {"fontSize": "18px", "padding": "10px"}
    active_style = {"color": "#c93a6e", "fontSize": "18px", "padding": "10px", 'fontWeight': 'bold'}

    home_style = active_style if pathname == "/Home" else default_style
    report_style = active_style if pathname == "/Report" else default_style
    articles_style = active_style if pathname == "/Dashboard" else default_style
    continuous_monitoring_style = active_style if pathname == "/Continuous-monitoring" else default_style
    contact_style = active_style if pathname == "/contact" else default_style

    return home_style, report_style, articles_style, continuous_monitoring_style, contact_style


@app.callback(
    [Output("username-input", "valid"), Output("username-input", "invalid")],
    [Input("username-input", "value")],
)
def check_validity(text):
    if text:
        is_mail = re.match(r"[^@]+@[^@]+\.[^@]+", text) is not None
        return is_mail, not is_mail
    return False, False


@app.callback(
    Output("password-input", "type"),
    Output("password-icon", "className"),
    [Input("password-icon", "n_clicks")],
    [State("password-input", "type")],
)
def toggle_password_visibility(n_clicks, c):
    if n_clicks:
        if n_clicks % 2 == 1:
            return "text", "bi bi-eye"
        else:
            return "password", "bi bi-eye-slash"
    return "password", "bi bi-eye-slash"


# Define the callback function that will handle the authentication
@app.callback([Output('url', 'pathname'),
               Output('authentication_output', 'children')],
              [Input('sign_up_button', 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value')],
              prevent_initial_call=True)
def authenticate_user(n_clicks, user, password):
    user_dict = list(user_access_collection.find())
    if n_clicks:
        if not user or not password:
            return '/', html.H1("Please Enter Valid Details", style={'fontWeight': 'bold',
                                                                     'fontFamily': 'Arial',
                                                                     'textAlign': 'center',
                                                                     'color': 'red',
                                                                     'fontSize': 20,
                                                                     })
        user_info = next((u for u in user_dict if u['userName'] == user), None)
        if not user_info:
            return '/', html.H1("Please Enter Valid Details", style={'fontWeight': 'bold',
                                                                     'fontFamily': 'Arial',
                                                                     'textAlign': 'center',
                                                                     'color': 'red',
                                                                     'fontSize': 20})

        if user_info['password'] != password:
            return '/', html.H1("Invalid password!", style={'fontWeight': 'bold',
                                                            'fontFamily': 'Arial',
                                                            'textAlign': 'center',
                                                            'color': 'red',
                                                            'fontSize': 20})

        if user_info and user_info['password'] == password:
            session['authenticated'] = True
            session['username'] = user
            session['session_id'] = str(uuid.uuid4())
            return '/Home', None

    return '/', None


@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    # if 'authenticated' in session and session['authenticated']:
    if pathname == "/":
        return login_page
    elif pathname == "/Home":
        return Home_page
    elif pathname == "/Report":
        return report_page
    elif pathname == "/Dashboard":
        return dashboard_page
    elif pathname == "/Continuous-monitoring":
        return html.P("This is the content of cm page. Yay!")
    elif pathname == "/contact":
        return html.P("This is the content of contact page. Yay!")
    else:
        return html.P("error!!!!")
    # else:
    #     time.sleep(0.5)
    #     return login_page


@app.callback([Output('Subscribers-id', 'children'),
               Output('Measurements-id', 'children'),
               Output('Males-id', 'children'),
               Output('Females-id', 'children'),
               Output('Transgenders-id', 'children'),
               Output('accordion', 'active_item'),
               Output('datatable-info', 'children'),
               Output('output-graphs-div', 'children')
               ],
              [Input('submit-filter', 'n_clicks')],
              [State('location-radio', 'value'),
               State('gender-radio', 'value'),
               State('age-min-input', 'value'),
               State('age-max-input', 'value'),
               State('height-min-input', 'value'),
               State('height-max-input', 'value'),
               State('weight-min-input', 'value'),
               State('weight-max-input', 'value'),
               State('sys-min-input', 'value'),
               State('sys-max-input', 'value'),
               State('dia-min-input', 'value'),
               State('dia-max-input', 'value')])
def update_dataframe(n_clicks, location, gender, min_age, max_age, min_height, max_height, min_weight,
                     max_weight, min_sys, max_sys, min_dia, max_dia):
    excel_dataframe = dataframe.copy()
    if n_clicks is not None:
        min_age = max(min_age, 18)
        max_age = min(max_age, 100)
        min_height = max(min_height, 140)
        max_height = min(max_height, 200)
        min_weight = max(min_weight, 30)
        max_weight = min(max_weight, 150)
        min_sys = max(min_sys, 60)
        max_sys = min(max_sys, 250)
        min_dia = max(min_dia, 30)
        max_dia = min(max_dia, 150)

        if location == "All":
            filtered_dataframe = excel_dataframe
        else:
            filtered_dataframe = excel_dataframe[excel_dataframe["LOCATION"] == location]

        if gender == "Global":
            filtered_dataframe = filtered_dataframe
        else:
            filtered_dataframe = filtered_dataframe[filtered_dataframe["GENDER"] == gender]

        filtered_dataframe = filtered_dataframe[(filtered_dataframe['AGE'] >= min_age) &
                                                (filtered_dataframe['AGE'] <= max_age)]

        filtered_dataframe = filtered_dataframe[(filtered_dataframe['HEIGHT'] >= min_height) &
                                                (filtered_dataframe['HEIGHT'] <= max_height)]

        filtered_dataframe = filtered_dataframe[(filtered_dataframe['WEIGHT'] >= min_weight) &
                                                (filtered_dataframe['WEIGHT'] <= max_weight)]

        filtered_dataframe = filtered_dataframe[(filtered_dataframe['Calc_SBP'] >= min_sys) &
                                                (filtered_dataframe['Calc_SBP'] <= max_sys)]

        filtered_dataframe = filtered_dataframe[(filtered_dataframe['Calc_DBP'] >= min_dia) &
                                                (filtered_dataframe['Calc_DBP'] <= max_dia)]

        if len(filtered_dataframe) > 0:
            actual_sbp = filtered_dataframe['REF_SBP'].to_numpy()
            predicted_sbp = filtered_dataframe['Calc_SBP'].to_numpy()
            difference_sbp = actual_sbp - predicted_sbp
            mean_sbp = (actual_sbp + predicted_sbp) / 2
            mean_difference_sbp = np.mean(difference_sbp)
            lower_limit_sbp = mean_difference_sbp - 15
            upper_limit_sbp = mean_difference_sbp + 15

            actual_dbp = filtered_dataframe['REF_DBP'].to_numpy()
            predicted_dbp = filtered_dataframe['Calc_DBP'].to_numpy()
            difference_dbp = actual_dbp - predicted_dbp
            mean_dbp = (actual_dbp + difference_dbp) / 2
            mean_difference_dbp = np.mean(difference_dbp)
            lower_limit_dbp = mean_difference_dbp - 15
            upper_limit_dbp = mean_difference_dbp + 15

            figure_pie_gender = px.pie(filtered_dataframe, names='GENDER', hole=.5)
            figure_pie_gender.update_layout(height=550,
                                            plot_bgcolor='#ffffff',
                                            paper_bgcolor='#ffffff',
                                            title_text='Gender',
                                            font_family="sans-serif",
                                            font_color="black",
                                            title_font_family="sans-serif",
                                            title_font_color="black",
                                            title_font_size=20,
                                            font_size=12)
            figure_pie_gender.update_traces(marker_line_width=1, marker_line_color="#ffffff")
            figure_pie_gender.for_each_xaxis(lambda x: x.update(showgrid=False))

            figure_bpm = px.histogram(filtered_dataframe, x="PPG_HR", nbins=20, color="GENDER")
            figure_bpm.update_layout(height=550,
                                     plot_bgcolor='#ffffff',
                                     paper_bgcolor='#ffffff',
                                     xaxis_title="Heartrate",
                                     yaxis_title="Counts",
                                     title_text='Heart Rate',
                                     font_family="sans-serif",
                                     font_color="black",
                                     title_font_family="sans-serif",
                                     title_font_color="black",
                                     title_font_size=20,
                                     font_size=12)
            figure_bpm.update_traces(marker_line_width=1, marker_line_color="#ffffff")
            figure_bpm.for_each_xaxis(lambda x: x.update(showgrid=False))
            figure_bpm.for_each_yaxis(lambda x: x.update(showgrid=False))

            figureSystolic = px.histogram(filtered_dataframe, x="Calc_SBP", nbins=20, color="GENDER")
            figureSystolic.update_layout(height=550,
                                         plot_bgcolor='#ffffff',
                                         paper_bgcolor='#ffffff',
                                         xaxis_title="SBP",
                                         yaxis_title="Measurements",
                                         title_text='Systolic Blood Pressure',
                                         font_family="sans-serif",
                                         font_color="black",
                                         title_font_family="sans-serif",
                                         title_font_color="black",
                                         title_font_size=20,
                                         font_size=12)
            figureSystolic.update_traces(marker_line_width=1, marker_line_color="#ffffff")
            figureSystolic.for_each_xaxis(lambda x: x.update(showgrid=False))
            figureSystolic.for_each_yaxis(lambda x: x.update(showgrid=False))

            figureDiastolic = px.histogram(filtered_dataframe, x="Calc_DBP", nbins=20, color="GENDER")
            figureDiastolic.update_layout(height=550,
                                          plot_bgcolor='#ffffff',
                                          paper_bgcolor='#ffffff',
                                          xaxis_title="DBP",
                                          yaxis_title="Measurements",
                                          title_text='Diastolic Blood Pressure',
                                          font_family="sans-serif",
                                          font_color="black",
                                          title_font_family="sans-serif",
                                          title_font_color="black",
                                          title_font_size=20,
                                          font_size=12)
            figureDiastolic.update_traces(marker_line_width=1, marker_line_color="#ffffff")
            figureDiastolic.for_each_xaxis(lambda x: x.update(showgrid=False))
            figureDiastolic.for_each_yaxis(lambda x: x.update(showgrid=False))

            graph = html.Div([
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                dcc.Graph(figure=figure_pie_gender,
                                          config={
                                              'staticPlot': False,
                                              'scrollZoom': False,
                                              'doubleClick': 'reset',
                                          }),
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                        dbc.Col(
                            html.Div([
                                dcc.Graph(figure=figure_bpm,
                                          config={
                                              'staticPlot': False,
                                              'scrollZoom': False,
                                              'doubleClick': 'reset',
                                          }),
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                    ],
                    className="g-3",
                    style={'marginBottom': '40px'}
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                dcc.Graph(figure=figureSystolic,
                                          config={
                                              'staticPlot': False,
                                              'scrollZoom': False,
                                              'doubleClick': 'reset',
                                          }),
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 20px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                        dbc.Col(
                            html.Div([
                                dcc.Graph(figure=figureDiastolic,
                                          config={
                                              'staticPlot': False,
                                              'scrollZoom': False,
                                              'doubleClick': 'reset',
                                          }),
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                    ],
                    className="g-3",
                    style={'marginBottom': '40px'}
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            html.Div([
                                dcc.Graph(
                                    id='bland-altman-plot-sbp',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=mean_sbp,
                                                y=difference_sbp,
                                                mode='markers',
                                                name='Difference SBP'
                                            ),
                                            go.Scatter(
                                                x=[mean_sbp.min(), mean_sbp.max()],
                                                y=[mean_difference_sbp, mean_difference_sbp],
                                                mode='lines',
                                                name='Mean Difference SBP',
                                                line=dict(color='red', dash='dash')
                                            ),
                                            go.Scatter(
                                                x=[mean_sbp.min(), mean_sbp.max()],
                                                y=[lower_limit_sbp, lower_limit_sbp],
                                                mode='lines',
                                                name='Lower Limit of Agreement SBP',
                                                line=dict(color='green', dash='dash')
                                            ),
                                            go.Scatter(
                                                x=[mean_sbp.min(), mean_sbp.max()],
                                                y=[upper_limit_sbp, upper_limit_sbp],
                                                mode='lines',
                                                name='Upper Limit of Agreement SBP',
                                                line=dict(color='green', dash='dash')
                                            )
                                        ],
                                        'layout': go.Layout(
                                            title='Bland-Altman Plot (Systolic Blood Pressure)',
                                            xaxis={'title': 'Mean SBP'},
                                            yaxis={'title': 'Difference (Actual SBP - Predicted SBP)'},
                                            hovermode='closest'
                                        )
                                    }
                                )
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                        dbc.Col(
                            html.Div([
                                dcc.Graph(
                                    id='bland-altman-plot-dbp',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=mean_dbp,
                                                y=difference_dbp,
                                                mode='markers',
                                                name='Difference-DBP'
                                            ),
                                            go.Scatter(
                                                x=[mean_dbp.min(), mean_dbp.max()],
                                                y=[mean_difference_dbp, mean_difference_dbp],
                                                mode='lines',
                                                name='Mean Difference BDP',
                                                line=dict(color='red', dash='dash')
                                            ),
                                            go.Scatter(
                                                x=[mean_dbp.min(), mean_dbp.max()],
                                                y=[lower_limit_dbp, lower_limit_dbp],
                                                mode='lines',
                                                name='Lower Limit of Agreement DBP',
                                                line=dict(color='green', dash='dash')
                                            ),
                                            go.Scatter(
                                                x=[mean_dbp.min(), mean_dbp.max()],
                                                y=[upper_limit_dbp, upper_limit_dbp],
                                                mode='lines',
                                                name='Upper Limit of Agreement DBP',
                                                line=dict(color='green', dash='dash')
                                            )
                                        ],
                                        'layout': go.Layout(
                                            title='Bland-Altman Plot (Diastolic Blood Pressure)',
                                            xaxis={'title': 'Mean DBP'},
                                            yaxis={'title': 'Difference (Actual DBP - Predicted DBP)'},
                                            hovermode='closest'
                                        )
                                    }
                                )
                            ], style={"border": "1px solid #c93a6e", "borderRadius": "10px",
                                      'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'margin-left': '20px',
                                      'margin-right': '20px', 'textAlign': 'center'}),
                            xs=12, sm=12, md=6, lg=6, xl=6
                        ),
                    ],
                    className="g-3",
                    style={'marginBottom': '40px'}
                ),

            ])

            unique_subscribers = len(filtered_dataframe.USR_ID.unique())
            unique_measurements = len(filtered_dataframe.MSR_ID.unique())
            males_count = filtered_dataframe[filtered_dataframe['GENDER'] == "male"]['MSR_ID'].nunique()
            females_count = filtered_dataframe[filtered_dataframe['GENDER'] == "female"]['MSR_ID'].nunique()
            trans_count = filtered_dataframe[filtered_dataframe['GENDER'] == "trans"]['MSR_ID'].nunique()

            info_df, report_df = FDA_Report(filtered_dataframe, filtered_dataframe)

            info_table = html.Div([
                dbc.Table.from_dataframe(info_df, striped=True, bordered=True, hover=True, color="secondary")
            ])

            report_table = html.Div([
                dbc.Table.from_dataframe(report_df, striped=True, bordered=True, hover=True, color="secondary")
            ])

            report_info_table = html.Div([
                info_table,
                report_table
            ], style={'margin': '20px'},
                className="g-3"
            )

            return unique_subscribers, unique_measurements, males_count, females_count, trans_count, '', \
                report_info_table, graph

        else:
            return None, None, None, None, None, '', None, \
                html.Div([
                    html.P("Oops! No data found in this range.")
                ],
                    style={'margin': '40px'},
                    className="g-3"
                )

    info_df, report_df = FDA_Report(excel_dataframe, excel_dataframe)

    info_table = html.Div([
        dbc.Table.from_dataframe(info_df, striped=True, bordered=True, hover=True, color="secondary")
    ])

    report_table = html.Div([
        dbc.Table.from_dataframe(report_df, striped=True, bordered=True, hover=True, color="secondary")
    ])

    report_info_table = html.Div([
        info_table,
        report_table
    ], style={'margin': '20px'},
        className="g-3"
    )

    unique_subscribers = len(excel_dataframe.USR_ID.unique())
    unique_measurements = len(excel_dataframe.MSR_ID.unique())
    males_count = excel_dataframe[excel_dataframe['GENDER'] == "male"]['MSR_ID'].nunique()
    females_count = excel_dataframe[excel_dataframe['GENDER'] == "female"]['MSR_ID'].nunique()
    trans_count = excel_dataframe[excel_dataframe['GENDER'] == "trans"]['MSR_ID'].nunique()

    return unique_subscribers, unique_measurements, males_count, females_count, trans_count, '', \
        report_info_table, None


app.clientside_callback(
    """
    function(value1, value2) {
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                document.getElementById('sign_up_button').click();
            }
        });
        return '';
    }
    """,
    Output('hidden-div', 'children'),
    [Input('username-input', 'value'), Input('password-input', 'value')],
    prevent_initial_call=True
)


class ServerThread(threading.Thread):

    def __init__(self, application):
        threading.Thread.__init__(self)
        self.srv = make_server('127.0.0.1', 8050, application.server)
        self.ctx = application.server.app_context()
        self.ctx.push()

    def run(self):
        self.srv.serve_forever()

    def shutdown(self):
        self.srv.shutdown()


def signal_handler(sig, frame):
    print('Shutting down gracefully...')
    server.shutdown()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    server = ServerThread(app)
    server.start()
    print('Server running on http://127.0.0.1:8050/')
