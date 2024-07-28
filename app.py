import streamlit as st
import pickle
import json
import pandas as pd
import requests



def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=48465a0e03c7d658a52b28098b98ad65&language=en-US".format(movie_id))
    data = response.json()
    st.text(data)
    st.text("https://api.themoviedb.org/3/movie/{}?api_key=48465a0e03c7d658a52b28098b98ad65&language=en-US".format(movie_id))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie = []
    recommended_movie_poster = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_poster .append(fetch_poster(movie_id))
        recommended_movie.append(movies.iloc[i[0]].title)

    return movie_name, movie_poster


st.header('Movie Recommender System')
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Recommendation'):
    movie_name, movie_poster = recommend(selected)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
