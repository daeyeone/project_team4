from google_play_scraper import Sort, reviews
import pandas as pd


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

    filtered = []
    for r in review_list:
        filtered.append({
            "reviewId": r.get("reviewId"),
            "content": r.get("content"),
            "score": r.get("score"),
            "date": r.get("at").strftime("%Y-%m-%d") if r.get("at") else None
        })

    df = pd.DataFrame(filtered)

    file_name = f"reviews_sudoku{idx}.csv"
    df.to_csv(file_name, index=False, encoding="utf-8-sig")

print("파일 생성완료")
