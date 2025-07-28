import requests
from datetime import datetime

def mlb_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"
    res = requests.get(url)
    data = res.json()

    team_translation = {
        "Blue Jays": "ブルージェイズ",
        "Orioles": "オリオールズ",
        "Rockies": "ロッキーズ",
        "Guardians": "ガーディアンズ",
        "Diamondbacks": "ダイヤモンドバックス",
        "Tigers": "タイガース",
        "Rays": "レイズ",
        "Yankees": "ヤンキース",
        "Dodgers": "ドジャース",
        "Reds": "レッズ",
        "Red Sox": "レッドソックス",
        "Twins": "ツインズ",
        "Braves": "ブレーブス",
        "Royals": "ロイヤルズ",
        "Phillies": "フィリーズ",
        "White Sox": "ホワイトソックス",
        "Cubs": "カブス",
        "Brewers": "ブルワーズ",
        "Marlins": "マーリンズ",
        "Cardinals": "カージナルス",
        "Nationals": "ナショナルズ",
        "Astros": "アストロズ",
        "Rangers": "レンジャーズ",
        "Angels": "エンゼルス",
        "Mets": "メッツ",
        "Padres": "パドレス",
        "Pirates": "パイレーツ",
        "Giants": "ジャイアンツ",
        "Mariners": "マリナーズ",
        "Athletics": "アスレチックス"
    }

    result = [f"【MLBスコア速報】\n{datetime.now().date()}"]

    games = data.get("events", [])
    if not games:
        result.append("本日の試合はありません。")
        return "\n".join(result)
        
    for game in games:
        competitions = game.get("competitions", [])
        if not competitions:
            continue
        competition = competitions[0]

        teams = competition.get("competitors", [])
        status = competition.get("status", {}).get("type", {}).get("description", "不明")

        away_team = next((t for t in teams if t.get("homeAway") == "away"), {})
        home_team = next((t for t in teams if t.get("homeAway") == "home"), {})

        away = away_team.get("team", {}).get("name", "不明")
        home = home_team.get("team", {}).get("name", "不明")
        away_score = away_team.get("score")
        home_score = home_team.get("score")

        away_jp = team_translation.get(away, away)
        home_jp = team_translation.get(home, home)

        if away_score and home_score:
            result.append(f"{away_jp} {away_score} - {home_score} {home_jp}（{status}）")
        else:
            result.append(f"{away_jp} vs {home_jp}（{status}）")

    return "\n".join(result)
