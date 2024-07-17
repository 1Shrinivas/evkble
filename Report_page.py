from dash import html

pdf_path = 'assets/BP_slides.pdf'

report_page = html.Div([
    html.H3("Analysis Report",
            style={'textAlign': 'left', 'lineHeight': '2', 'maxWidth': '70%', 'color': '#000000',
                   'fontSize': '20px', 'fontWeight': 'bold', 'paddingLeft': '20px'}),
    html.Iframe(src=f'/{pdf_path}', width='100%', height='800px')
], style={'margin': '20px'}, className="g-3")
