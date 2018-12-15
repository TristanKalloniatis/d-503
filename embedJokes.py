import csv
print("Loading word embeddings...")
gloveEmbeddingsFile=open('fetch_data/Glove/glove.6B.50d.csv','r')
gloveEmbeddings=csv.reader(gloveEmbeddingsFile)
gloveEmbeddingsDictionary={}
for row in gloveEmbeddings:
    key=row[0]
    value=row[1:]
    gloveEmbeddingsDictionary[key]=value
joke=raw_input("Enter sample joke: ")
jokeWords=joke.split(' ')
for word in jokeWords:
    cleanedWord=word.lower().rstrip(",.?!;:-")
    if cleanedWord in gloveEmbeddingsDictionary:
        print(gloveEmbeddingsDictionary[cleanedWord])
    else:
        print("UNKNOWN WORD: " + cleanedWord)
