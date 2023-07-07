import pandas as pd

##
# data imports
##

data = pd.read_csv('./Data/csv/movies_dataset.csv').astype(str)

##
# preprocessing
##

# find all genres for movies in the dataset
genresAllMovies = [data.loc[i]['genres'].split(', ') for i in data.index]
# sort the genres and put into a list
genres = sorted(list(set([item for sublist in genresAllMovies for item in sublist])))
# create a new dataframe consisting of only the movie's id and title
dataTitleID = data[['id', 'title']].copy()

##
# generate a URL and JSON
##

URLs = []
genreData = []
website = 'https://www.themoviedb.org/movie/'
# loop through movies and generate a link to the moviedb site for the corresponding movie
# then generate a json for the model
for i in dataTitleID.index:
    temp = website
    id = dataTitleID.iloc[i]['id']
    title = dataTitleID.iloc[i]['title']
    # convert title to url format
    titleDict = {" ": "-", "?": "", ":": "", "!": "", ".": "", "\'": "-"}
    for char in titleDict.keys():
        title = title.replace(char, titleDict[char])
    
    # append id and movie name to temp result, then append to url list
    temp += "{}-{}".format(id, title)
    URLs.append(temp) 

    # generate a json containing binary genre data
    genreBinaryData = [1 if genre in genresAllMovies else 0 for genre in genres]
    genreBinaryData.append(data.loc[i]['title'])
    genreData.append(genreBinaryData)
    #print(genreBinaryData[i])

print(URLs[1:10])
print(genreData[1:10])
print(genres)






#print(data.head(5)) 