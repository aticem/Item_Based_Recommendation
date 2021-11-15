
def create_user_movie_df():
    import pandas as pd
    movie = pd.read_csv('movie.csv')
    rating = pd.read_csv('rating.csv')
    df = movie.merge(rating, how="left", on="movieId")
    df = df.iloc[:50000, :]
    df['title'] = df.title.str.replace('(\(\d\d\d\d\))', '')
    df['title'] = df['title'].apply(lambda x: x.strip())
    a = pd.DataFrame(df["title"].value_counts())
    rare_movies = a[a["title"] <= 1000].index
    common_movies = df[~df["title"].isin(rare_movies)]
    user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return user_movie_df


user_movie_df = create_user_movie_df()

user_movie_df

def item_based_recommender(movie_name, user_movie_df):
    movie = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)

item_based_recommender("Babe", user_movie_df) v 
item_based_recommender("Sherlock Holmes", user_movie_df)


# GENELLEME PROBLEMI

item_based_recommender("Matrix", user_movie_df)



def item_based_recommender(movie_name):
    # film user move df'de yoksa önce ismi barındıran ilk filmi getir.
    # eger o da yoksa filmin isminin ilk iki harfini barındıran ilk filmi getir.
    if movie_name not in user_movie_df:
        # ismi barındıran ilk filmi getir.
        if [col for col in user_movie_df.columns if movie_name.capitalize() in col]:
            new_movie_name = [col for col in user_movie_df.columns if movie_name.capitalize() in col][0]
            movie = user_movie_df[new_movie_name]
            print(F"{movie_name}'i barındıran ilk  film: {new_movie_name}\n")
            print(F"{new_movie_name} için öneriler geliyor...\n")
            return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)
        # filmin ilk 2 harfini barındıran ilk filmi getir.
        else:
            new_movie_name = [col for col in user_movie_df.columns if col.startswith(movie_name.capitalize()[0:2])][0]
            movie = user_movie_df[new_movie_name]
            print(F"{movie_name}'nin ilk 2 harfini barındıran ilk film: {new_movie_name}\n")
            print(F"{new_movie_name} için öneriler geliyor...\n")
            return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)
    else:
        print(F"{movie_name} için öneriler geliyor...\n")
        movie = user_movie_df[movie_name]
        return user_movie_df.corrwith(movie).sort_values(ascending=False).head(10)


item_based_recommender("Sherlock Holmes")