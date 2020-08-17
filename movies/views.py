import requests

import pandas as pd

from django.shortcuts import render


# Create your views here.
def movies(request):

    def get_all(type):

        r = requests.get('https://ghibliapi.herokuapp.com/{}'.format(type))

        return(r.json())

    # Create films data frame
    films = get_all('films')
    df_films = pd.DataFrame(films).loc[:, ['id', 'title']]

    # Create people data frame
    people = get_all('people')
    df_people = pd.DataFrame(people).loc[:, ['name', 'films']]
    s = df_people['films'].apply(pd.Series, 1).stack()
    s = s.apply(lambda x: x.split('/')[-1])
    s.index = s.index.droplevel(-1)
    s.name = 'film_id'
    del df_people['films']
    df_people = df_people.join(s)

    # Left join
    df = pd.merge(df_films, df_people, left_on='id', right_on='film_id', how='left')
    df = df.groupby(['id', 'title']).name.apply(list).reset_index()
    del df['id']
    df = df.to_dict(orient='records')

    context = {'data': df}

    return render(request, 'movies/movies.html', context)
