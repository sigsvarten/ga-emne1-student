# Lage match resultater i løkke

def show_match_result(home_team, away_team, home_score, away_score):
    if home_score > away_score:
        print(f'{home_team} wins {home_score} - {away_score}, and {away_team} lose')
    elif home_score < away_score:
        print(f' {away_team} wins. The score is {home_score} - {away_score}, and {home_team}')
    else:
        print(f'The score is {home_score} - {away_score}. It is a tie')



show_match_result('Liverpool' , 'Chelsea' ,6, 2)
show_match_result('Liverpool' , 'Chelsea' ,1, 2)
show_match_result('Liverpool' , 'Chelsea' ,2, 2)