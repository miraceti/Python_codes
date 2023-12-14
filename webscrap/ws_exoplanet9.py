import plotly.express as px
import pandas as pd

#read csv to datafrtame
df1 = pd.read_csv('exoplanet.eu_catalog.csv', sep=',')
print(df1)
df2 = df1[['name','planet_status','mass','radius','detection_type','orbital_period','discovered','star_name','star_distance']].dropna().sort_values(by=['discovered'], ascending=True)
print(df2)

# fig = px.scatter(
#     #df2.query("discovered==2010"),
#     df2,
#     x="star_distance",
#     y="radius",
#     color="detection_type",
#     size="mass",
#     hover_name="name",
#     log_x=True,
#     size_max=60,

# )

# fig.show()
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#            size="pop", color="continent", hover_name="country", facet_col="continent",
#            log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
figa = px.scatter(
    #df2.query("discovered==2010"),
    df2,
    x="star_distance",
    y="radius",
    color="detection_type",
    size="mass",
    hover_name="name",
    log_x=True,
    size_max=100,
    
    # facet_col="detection_type",
    range_x=[5,10000], range_y=[0,2.5],

    # animation_frame="discovered",
    # animation_group="name",
)
figa.show()

figb = px.scatter(
    #df2.query("discovered==2010"),
    df2,
    x="star_distance",
    y="radius",
    color="discovered",
    size="mass",
    hover_name="name",
    log_x=True,
    size_max=100,
    
    # facet_col="detection_type",
    range_x=[5,10000], range_y=[0,2.5],

    # animation_frame="discovered",
    # animation_group="name",
)

figb.show()


