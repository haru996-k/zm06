import requests
from bs4 import BeautifulSoup

def npb_scores():
    url = "https://baseball.yahoo.co.jp/npb/"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    games = soup.select(".bb-score__game")
    if not games:
        return "本日の速報はありません。"
    
    result_lines = ["現在のNPBスコア速報（スポーツナビ）"]
    for game in games:
        teams = game.select(".bb-score__team-name")
        scores = game.select(".bb-score__score")
        status = game.select_one(".bb-score__status").get_text(strip=True)

        if len(teams) == 2 and len(scores) == 2:
            team1 = teams[0].get_text(strip=True)
            team2 = teams[1].get_text(strip=True)
            score1 = scores[0].get_text(strip=True)
            score2 = scores[1].get_text(strip=True)
            result_lines.append(f"{team1} {score1} - {score2} {team2} ({status})")

        else:
            result_lines.append("一部試合情報が取得できませんでした。")

    return "\n".join(result_lines)