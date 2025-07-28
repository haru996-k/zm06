import requests
from bs4 import BeautifulSoup

def npb_scores():
    url = "https://www.nikkansports.com/baseball/professional/score/"
    headers = {"User-Agent":
               ("Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/115.0.0.0 Safari/537.36") }
    
    res = requests.get(url, headers = headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    result_lines = ["【NPBスコア速報（日刊スポーツ)】"]
    matches = soup.select("div.scoreTable")

    if not matches:
        result_lines.append("本日の速報はありません。")

    else:
        for match in matches:
            teams = match.select("td.team")
            scores = match.select("td.score")

            if len(teams) == 2 and len(scores) == 2:
                team1 = teams[0].get_text(strip=True)
                team2 = teams[1].get_text(strip=True)
                score1 = scores[0].get_text(strip=True)
                score2 = scores[1].get_text(strip=True)
                result_lines.append(f"{team1} {score1} - {score2} {team2}")
            else:
                result_lines.append("スコアの取得に失敗しました。")
    
    return "\n".join(result_lines)