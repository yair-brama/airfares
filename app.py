from dash import Dash, Input, Output, callback, dcc, html
import copy
import plotly.express as px
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/airfares/airfares_merged_stdgroup.csv")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H5("Market"),
        dcc.Dropdown(
            id="market", options=sorted(df["market"].unique())
        ),
        html.H5("Origin"),
        dcc.Dropdown(
            id="origin", options=sorted(df["origin"].unique())
        ),
        html.H5("Departure Date"),
        dcc.Dropdown(
            id="departure_date",
            options=sorted(df["departure_date"].unique()),
            value=df["departure_date"][0],
        ),
        html.H5("Flight Number"),
        dcc.Dropdown(
            id="flight_number",
            options=sorted(df["flight_number"].unique()),
        ),
        html.H5("Trend"),
        dcc.Dropdown(
            id="trend",
            options=sorted(df["trend"].unique()),
        ),
        html.H5("Volatility"),
        dcc.Dropdown(
            id="stdGroup",
            options=sorted(df["stdGroup"].unique()),
        ),
        html.Br(),
        dcc.Graph(id="line"),
    ]
)


@callback(
    Output("departure_date", "options"),
    Input("flight_number", "value"),
    Input("market", "value"),
    Input("origin", "value"),
    Input("trend", "value"),
    Input("stdGroup", "value"),
)
def chained_callback_departure_date(flight_number, market, origin, trend, stdGroup):

    dff = copy.deepcopy(df)

    if market is not None:
        dff = dff.query("market == @market")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if trend is not None:
        dff = dff.query("trend == @trend")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    return sorted(dff["departure_date"].unique())


@callback(
    Output("flight_number", "options"),
    Input("departure_date", "value"),
    Input("market", "value"),
    Input("origin", "value"),
    Input("trend", "value"),
    Input("stdGroup", "value"),
)
def chained_callback_flight_number(departure_date, market, origin, trend, stdGroup):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if market is not None:
        dff = dff.query("market == @market")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if trend is not None:
        dff = dff.query("trend == @trend")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    return sorted(dff["flight_number"].unique())


@callback(
    Output("market", "options"),
    Input("departure_date", "value"),
    Input("flight_number", "value"),
    Input("origin", "value"),
    Input("trend", "value"),
    Input("stdGroup", "value"),
)
def chained_callback_market(departure_date, flight_number, origin, trend, stdGroup):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if trend is not None:
        dff = dff.query("trend == @trend")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    return sorted(dff["market"].unique())

@callback(
    Output("trend", "options"),
    Input("departure_date", "value"),
    Input("flight_number", "value"),
    Input("market", "value"),
    Input("origin", "value"),
    Input("stdGroup", "value"),
)
def chained_callback_trend(departure_date, flight_number, market, origin, stdGroup):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if market is not None:
        dff = dff.query("market == @market")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    return sorted(dff["trend"].unique())

@callback(
    Output("stdGroup", "options"),
    Input("departure_date", "value"),
    Input("flight_number", "value"),
    Input("market", "value"),
    Input("origin", "value"),
    Input("trend", "value"),
)
def chained_callback_stdgroup(departure_date, flight_number, market, origin, trend):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if market is not None:
        dff = dff.query("market == @market")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if trend is not None:
        dff = dff.query("trend == @trend")

    return sorted(dff["stdGroup"].unique())

@callback(
    Output("origin", "options"),
    Input("departure_date", "value"),
    Input("flight_number", "value"),
    Input("market", "value"),
    Input("trend", "value"),
    Input("stdGroup", "value"),
)
def chained_callback_origin(departure_date, flight_number, market, trend, stdGroup):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if market is not None:
        dff = dff.query("market == @market")

    if trend is not None:
        dff = dff.query("trend == @trend")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    return sorted(dff["origin"].unique())



@callback(
    Output("line", "figure"),
    Input("departure_date", "value"),
    Input("flight_number", "value"),
    Input("market", "value"),
    Input("origin", "value"),
    Input("trend", "value"),
    Input("stdGroup", "value"),
)
def line_chart(departure_date, flight_number, market, origin, trend, stdGroup):

    dff = copy.deepcopy(df)

    if departure_date is not None:
        dff = dff.query("departure_date == @departure_date")

    if flight_number is not None:
        dff = dff.query("flight_number == @flight_number")

    if market is not None:
        dff = dff.query("market == @market")

    if origin is not None:
        dff = dff.query("origin == @origin")

    if trend is not None:
        dff = dff.query("trend == @trend")

    if stdGroup is not None:
        dff = dff.query("stdGroup == @stdGroup")

    grouped_df = dff.groupby(dff["observation_date"])['price'].mean().reset_index()

    fig = px.line(
        x=grouped_df["observation_date"],
        y=grouped_df["price"],
        template="simple_white",
        labels={"x": "Observation Date", "y": "Price"},
    )

    return fig


if __name__ == "__main__":
    app.run()