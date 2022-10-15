dict = {"apple":"A fruit",
       "abound":"to exist in large numbers",
       "abundance":"the situation in which there is more than enough of something",
       "abundantly":"in large quantities or amounts",
       "amount":"a collection or mass, especially of something that cannot be counted",
       "babble":"to talk or say something in a quick, confused, excited, or silly way",
       "babbled":"past simple and past participle of babble",
       "babe":"a small baby",
       "babel":"the confusing sound of many people talking at the same time or using different languages",
       "baboon":"a type of large monkey, found in Africa and Asia, with a long, pointed face like a dog and large teeth"}


def meaning(word):
  try:
       return dict[word]
  except:
       return "couldn't find the word :("
  


strn = "Apple".lower()
print(meaning(strn))
