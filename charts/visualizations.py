import plotly.express as px
import plotly.graph_objects as go

def create_skills_pie_chart(matched_skills, missing_skills):
    labels = ['Matched', 'Missing']
    values = [len(matched_skills), len(missing_skills)]
    
    if sum(values) == 0:
        return None
        
    fig = px.pie(
        names=labels, 
        values=values, 
        hole=0.4,
        color_discrete_sequence=['#2e7d32', '#c62828']
    )
    fig.update_layout(
        margin=dict(t=30, b=10, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def create_ats_gauge(score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "ATS Score"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 50], 'color': "#ffebee"},
                {'range': [50, 75], 'color': "#fff3e0"},
                {'range': [75, 100], 'color': "#e8f5e9"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    fig.update_layout(margin=dict(t=50, b=20, l=20, r=20), height=300)
    return fig
