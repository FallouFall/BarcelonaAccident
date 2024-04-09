# AUTOGENERATED! DO NOT EDIT! File to edit: AccidentBcn.ipynb.

# %% auto 0
__all__ = []

# %% AccidentBcn.ipynb 4
from datetime import datetime

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,mean_squared_error
import  pandas as pd
import  numpy as np
import time
import warnings
warnings.filterwarnings('ignore')
import streamlit.components.v1 as components
import base64

# ----- Page configs -----
st.set_page_config(
        page_title = "Fallou Fall Portfolio" ,
        page_icon = "🧪" ,
        )

# ----- Left menu -----
with st.sidebar :
    st.image("eae_img.png" , width = 200)
    st.write(
            """I delved into the extensive dataset of car accidents in Barcelona, Catalonia. Through meticulous analysis, I uncovered temporal and spatial patterns, identified key factors contributing to accidents, and developed predictive models to forecast future occurrences. My findings provided valuable insights for policymakers and urban planners, guiding efforts to enhance traffic safety measures and mitigate risks. Ultimately, the journey exemplified the power of data science in driving positive societal change and fostering safer communities.""")
    st.write(
            "Data extracted from: https://opendata-ajuntament.barcelona.cat/data/es/dataset/accidents_causa_conductor_gu_bcn/resource/5a040155-38b3-4b19-a4b0-c84a0618d363/download/2023_accidents_causa_conductor_gu_bcn_.csv")

# ----- Title of the page -----

st.title("🚖 Catalunya Accidents 2023🚖")

#nrows = st.slider("Select the number of rows to read:", min_value=150, max_value=24000, step=500)
try :
    url = "https://opendata-ajuntament.barcelona.cat/data/es/dataset/accidents_causa_conductor_gu_bcn/resource/5a040155-38b3-4b19-a4b0-c84a0618d363/download/2023_accidents_causa_conductor_gu_bcn_.csv"
    df = pd.read_csv(url ,index_col=False)

except FileNotFoundError :
    st.error("Error: Data file not found. Please check the path.")

st.dataframe(df.head(5))




st.divider()
st.subheader("Barcelona Accients")
px.set_mapbox_access_token("pk.eyJ1Ijoic25vd21hbjIxIiwiYSI6ImNsdW9ueHU1MjA3NzUyaXI5bTV3NXlja3AifQ.Q3KozS09j8cSaQs-hMHgQQ")

fig = px.scatter_mapbox(df,
                        lat="Latitud_WGS84",
                        lon="Longitud_WGS84",
                        size_max=4,
                        zoom=13,
                        width=800,
                        height=600)
fig.update_traces(marker=dict(color='red'))
st.plotly_chart(fig)
st.divider()




st.divider()
st.subheader("Barrio Mas Accidents")
with st.container() :
    barrio = df['Nom_barri'].value_counts().nlargest(30).sort_values(ascending = True)
    fig = px.bar(x = barrio.values , y = barrio.index , orientation = 'h' , width = 800 , height = 600 ,
            labels = { 'x' : 'Accident' , 'y' : 'TOP Barrio' } ,
            title = 'Top 20  Barrio Accidents' ,
            color = barrio.index , color_continuous_scale = ['deepskyblue'] * len(barrio.index) ,
            color_discrete_sequence = px.colors.qualitative.Pastel * len(barrio.index) ,
            )
st.plotly_chart(fig)
st.divider()




st.subheader("Causa")
top_N = 10
top_causes = df['Descripcio_causa_mediata'].value_counts().nlargest(top_N)
colors = px.colors.qualitative.Pastel[:top_N]

color_map = {category: color for category, color in zip(top_causes.index, colors)}
fig = px.histogram(df[df['Descripcio_causa_mediata'].isin(top_causes.index)],
                   x='Descripcio_causa_mediata',
                   title=f"Top {top_N} Causas",
                   height=650, width=800,
                   color='Descripcio_causa_mediata',
                   color_discrete_map=color_map)
st.plotly_chart(fig)



st.divider()
st.subheader("Horario mas Accidents")
with st.container() :
    horaire = df['Hora_dia'].value_counts().sort_index()
    colors = px.colors.qualitative.Pastel[:len(horaire)]
    color_map = { category : color for category , color in zip(horaire.index , colors) }

    # Create the bar chart
    fig = px.bar(x = horaire.index , y = horaire.values ,
            labels = { 'x' : 'Horaire' , 'y' : 'Accident' } ,
            title = 'Hora_dia Mas Accident' ,
            height = 600 , width = 800 ,
            color_discrete_sequence = colors)  # Using color_discrete_sequence

st.plotly_chart(fig)



st.divider()
st.subheader("Mes mas accidents")
mes_count = df['Nom_mes'].value_counts().sort_index()
colors = px.colors.qualitative.Pastel[:len(mes_count)]
color_map = {category: color for category, color in zip(mes_count.index, colors)}

fig = px.bar(x=mes_count.index, y=mes_count.values,
             labels={'x': 'Nom_mes', 'y': 'Accident'},
             title='Nom_mes Mas Accident',
             height=600, width=800,
             color=mes_count.index,
             color_discrete_map=color_map)
st.plotly_chart(fig)





st.divider()
st.subheader("Torn Accient")
turnover_counts = df['Descripcio_torn'].value_counts()
colors = px.colors.qualitative.Pastel[:len(turnover_counts)]
# Create pie chart
fig = px.pie(values=turnover_counts.values,
             names=turnover_counts.index,
             title='Tiempo  Mas Accidentes',
             color_discrete_sequence=colors,
             hole=0.3)
st.plotly_chart(fig)







#i calculate the number of accident for each district and add it to the dataframe
df['district_appearance'] = df.groupby('Codi_districte')['Codi_districte'].transform('count')



#model k mean
data = df[['Longitud_WGS84', 'Latitud_WGS84']]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_data)

#distotion calculation
coords = df[['Longitud_WGS84','Latitud_WGS84']]
distortions = []
K = [1,2,3,4,5]
for k in K:
    kmeansModel = KMeans(n_clusters=k)
    kmeansModel = kmeansModel.fit(coords)
    distortions.append(kmeansModel.inertia_)






st.divider()
st.subheader("Distortion Model")
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=K,
    y=distortions,
    mode='lines+markers',  # Combined line and markers mode
    marker=dict(
    size=8,  # Adjust marker size as desired
    )
))

fig.update_layout(
    title='Elbow Method For Optimal k',
    xaxis_title='k',
    yaxis_title='Distortions',
    width=800,
    height=600,
)
st.plotly_chart(fig)
st.divider()





st.subheader("Accidents Cluster ZONE")
df['cluster'] = kmeans.labels_
fig = px.scatter_mapbox(df, lat='Latitud_WGS84', lon='Longitud_WGS84', color='cluster',
                        color_continuous_scale=px.colors.qualitative.Light24,
                        zoom=10, height=600,width = 800)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(title='Clustering of Accident Data')
st.plotly_chart(fig)





#Soulouhete cal
kmeans = KMeans(n_clusters=5, init='k-means++')
kmeans.fit(coords)
y = kmeans.labels_
#print("k = 5", " silhouette_score ", silhouette_score(coords, y, metric='euclidean'))


#predict the cluster based on localisation
df['cluster'] = kmeans.predict(df[['Longitud_WGS84','Latitud_WGS84']])


def drivesafe( df , longitude , latitude ) :
    cluster = kmeans.predict(np.array([longitude , latitude]).reshape(1 , -1))[0]
    return df[df['cluster'] == cluster].iloc[0 :5][
        ['Nom_carrer' , 'Nom_barri' , 'Latitud_WGS84' , 'Longitud_WGS84' , 'cluster']]




longitude=df['Longitud_WGS84']
latitude=df['Latitud_WGS84']
longitude =st.selectbox(' Longitude', longitude)
latitude =st.selectbox(' Latitude', latitude)


st.markdown(
    """
    <style>
    .stButton>button {
        background-color: red;
        color:#ffffff
    }
    </style>
    """,
    unsafe_allow_html=True
)
if st.button('Predict'):
    prediction = drivesafe(df,longitude,latitude)
    score=pd.DataFrame(prediction)
    df['cluster'] = kmeans.labels_
    fig = px.scatter_mapbox(score , lat = 'Latitud_WGS84' , lon = 'Longitud_WGS84' , color = 'cluster' ,
            color_continuous_scale = px.colors.qualitative.Light24 ,
            size = 'cluster',
            zoom = 12 , height = 600 , width = 800)
    fig.update_layout(mapbox_style = "open-street-map")
    fig.update_layout(title = 'Clustering of Accident Data')

    st.plotly_chart(fig)
    score



