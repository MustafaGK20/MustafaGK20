import pandas as pd
import numpy as np

films = pd.read_csv("imdb-1000.csv")
print(films.columns)
print(films.shape)

# empty data
print("EmptyData: ",(films.isnull()).sum())
#print(films.dropna(subset=["content_rating"], how="any"))
films["content_rating"].fillna(value="Empty" , inplace=True)
print(films["content_rating"].value_counts(dropna=False))

#filter
print((films[(films["star_rating"]>=8.5)&(films["star_rating"]<=9)][["star_rating","title"]]).head())

#query
print(films.query("duration >= 150  | star_rating>=9.0")[["star_rating","duration","title"]])

#aggregate
print(films.groupby("star_rating").aggregate([min,np.median,max]))

print(films.groupby("content_rating").aggregate([min,np.median,max]))

#pivotTable

starRating = pd.cut(films["star_rating"], [7,8.5,9.5])
print(starRating.head(10))

print(films.pivot_table("duration", ["star_rating",starRating], "genre").head())

