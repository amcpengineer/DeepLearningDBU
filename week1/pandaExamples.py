import pandas as pd

reviews = pd.read_csv("docs/winemag-data-130k-v2.csv", index_col=0)

#################################################################################################################

# Create a variable bargain_wine with the title of
# the wine with the highest points-to-price ratio in the dataset.

bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax()].title
print(bargain_wine)

#################################################################################################################

# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or
# "fruity"? Create a Series descriptor_counts counting how many times each of these two words appears in the description
# column in the dataset. (For simplicity, let's ignore the capitalized versions of these words.)
#Use a map to check each description for the string tropical, then count up the number of times this is True

def count_word(word, series):
    return series.map(lambda desc: word in desc).sum()

tropical = count_word("tropical", reviews.description)
fruity = count_word("fruity", reviews.description)
descriptor_counts = pd.Series([tropical, fruity], index=["tropical", "fruity"])

#################################################################################################################
#We('d like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points '
#   '')is too hard to understand - we')d like to translate them into simple star ratings. A score of 95 or higher
#   counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

#Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should
# automatically get 3 stars, regardless of points.

#Create a series star_ratings with the number of stars corresponding to each review in the dataset.
def stars(row):
    if row.country == "Canada":
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
#print(star_ratings)

#################################################################################################################

#What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. Sort in descending order. Your output should look something like this:
#Unknown                    21247
#Napa Valley                 4480
#                           ...
#Bardolino Superiore            1
#Primitivo del Tarantino        1
#Name: region_1, Length: 1230, dtype: int64

reviews.region_1.fillna("Unkown")
newData = (reviews.groupby('region_1').value_counts()).sort_values(ascending=False)

print(newData)




