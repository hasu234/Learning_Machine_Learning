import Levenshtein

input_ = 'মুহিবুর রহমান সিদ্দিকী'

output_ = 'মুহিবুররহমান সিদ্দিকী'


dist = Levenshtein.distance(input_.replace(" ", ""), output_.replace(" ", ""))
score = 1 - dist / len(input_)
print(score*100)
