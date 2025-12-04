import pandas as pd
import re
import os

file_list = [f"reviews_sudoku{i}.csv" for i in range(1, 11)]

def clean_text(text):
    text = str(text)
    text = re.sub(r"[^가-힣0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

keyword_groups = {
    "광고": ["광고", "ad", "애드"],
    "난이도": ["난이도", "레벨", "difficulty", "쉬움", "어려움"],
    "과금": ["과금", "결제", "유료", "돈", "아이템"],
    "오류": ["오류", "버그", "튕김", "멈춤", "강제종료"],
    "UI": ["UI", "디자인", "화면", "레이아웃", "색감"],
    "기능 다양성": ["타임어택", "챌린지", "기록", "저장", "모드"]
}

for idx, file_name in enumerate(file_list, start=1):
    if not os.path.exists(file_name):
        continue


    df = pd.read_csv(file_name)

    df["clean_text"] = df["content"].apply(clean_text)

    group_counts = {key: 0 for key in keyword_groups}

    for review in df["clean_text"]:
        review_lower = review.lower()
        for group, keywords in keyword_groups.items():
            if any(k in review_lower for k in keywords):
                group_counts[group] += 1

    keywords_df = pd.DataFrame(list(group_counts.items()), columns=["keyword", "count"])

    output_name = f"keywords_sudoku{idx}.csv"
    keywords_df.to_csv(output_name, index=False)

    print(keywords_df)

