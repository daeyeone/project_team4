from google_play_scraper import Sort, reviews
import pandas as pd


def mask_username(name):
    if not isinstance(name, str):
        return name

    if len(name) <= 1:
        return "*"
    else:
        return name[0] + "*" * (len(name) - 1)


app_ids = [
    "easy.sudoku.puzzle.solver.free",
    "sudoku.puzzle.free.game.brain",
    "com.easybrain.sudoku.android",
    "com.gamovation.sudoku",
    "com.sudoku.puzzles.free.killer.classic.fun",
    "com.mathbrain.sudoku",
    "sudoku.puzzle.classic.math.games.train.brain",
    "com.conceptispuzzles.sudoku",
    "com.easybrain.killer.sudoku.free",
    "com.theangrykraken.sudoku"
]

for idx, app_id in enumerate(app_ids, start=1):

    review_list, _ = reviews(
        app_id,
        lang='ko',
        country='kr',
        sort=Sort.NEWEST,
        count=300
    )

    df = pd.DataFrame(review_list)

    if "userName" in df.columns:
        df["userName"] = df["userName"].apply(mask_username)

    file_name = f"reviews_sudoku{idx}.csv"
    df.to_csv(file_name, index=False)

print("완료")


