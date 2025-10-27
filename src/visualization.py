import plotly.express as px

def plot_app_usage(df):
    fig = px.bar(df, x='app_name', y='usage_minutes', color='category',
                 title="App Usage by Category", template='plotly_dark')
    fig.show()

def plot_notifications(df):
    fig = px.scatter(df, x='notifications', y='opens', color='app_name',
                     size='usage_minutes', title="Notifications vs App Opens")
    fig.show()
