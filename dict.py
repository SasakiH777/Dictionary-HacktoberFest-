dict = {"apple":"A fruit",
       "abound":"to exist in large numbers",
       "abundance":"the situation in which there is more than enough of something",
       "abundantly":"in large quantities or amounts",
       "amount":"a collection or mass, especially of something that cannot be counted"}


def meaning(word):
  return dict[word]


strn = "Apple".lower()
print(meaning(strn))
