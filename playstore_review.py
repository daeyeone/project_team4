from google_play_scraper import Sort, reviews, app

import pandas as pd


app_id = "com.sudoku.puzzles.free.killer.classic.fun"
app_info = app(app_id)


review_list, _ = reviews(
    app_id,
    lang='ko',
    country='kr',
    sort=Sort.NEWEST,
    count=300
)

df = pd.DataFrame(review_list)
df.to_csv("reviews_sudoku5.csv", index=False)


