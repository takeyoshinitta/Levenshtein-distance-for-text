# Levenshtein-distance-for-text

Product URL: https://levenshtein-distance-text.herokuapp.com/

<img width="1286" alt="Screenshot 2023-02-03 at 12 16 36 PM" src="https://user-images.githubusercontent.com/86846312/216721320-38f2deae-ddef-49f4-8ba7-8a2a922a4d6a.png">

<img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>: Substitution or Non-error, 
↑: Deletion, 
←: Insertion

|      |  HYP |   I  | have |  to  |finish|  my  | homework |
|------|------|------|------|------|------|------|----------|
| REF  |   0  |   1  |   2  |   3  |   4  |   5  |     6    |
|  I   |   1  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>0  |  ←1  |  ←2  |  ←3  |  ←4  |    ←5    |
| like |   2  |  ↑1  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>1  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>2  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>3  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>4  |    <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>5    |
| to   |   3  |  ↑2  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>2  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>1  |  ←2  |  ←3  |    ←4    |
| play |   4  |  ↑3  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>3  |  ↑2  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>2  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>3  |    <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>4    |
|tennis|   5  |  ↑4  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>4  |  ↑3  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>3  |  <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>3  |    <img src="https://user-images.githubusercontent.com/86846312/216723919-740586ea-6027-4d21-b9b4-c9a2bb1d785c.png" width=10px height=10px>4    |
