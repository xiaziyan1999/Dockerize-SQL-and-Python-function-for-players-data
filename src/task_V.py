import pytest
import psycopg2
import seaborn as sns  
import matplotlib.pyplot as plt 
import pandas as pd


#This funciton will graphically display the 10 players who have achieved the highest improvement across all skillsets
def display_player1():
    cur, conn = connect_db()
    q1 = pd.read_sql_query(
        '''select short_name, ((skill_dribbling + skill_curve + skill_fk_accuracy + skill_long_passing + skill_ball_control)/5 - overall) as improvement
            from players_20
            order by improvement desc
            limit 10''', conn)
    df = pd.DataFrame(q1, columns=['short_name', 'improvement'])
    return df
    save_and_terminate_connection(cur, conn)
df=display_player1()
sns.set_style("whitegrid")
ax=sns.barplot(x="short_name", y="improvement", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set_title('10 players who have achieved the highest improvement across all skillsets')

#This funciton will graphically displays the 5 players with highest value (value_eur).
def display_player2():
    cur, conn = connect_db()
    q1 = pd.read_sql_query(
        '''select short_name,value_eur
           from fifa.players_20
           order by value_eur desc
           limit 5''', conn)
    df = pd.DataFrame(q1, columns=['short_name', 'value_eur'])
    return df
    save_and_terminate_connection(cur, conn)
df=display_player2()
sns.set_style("whitegrid")
ax=sns.barplot(x="short_name", y="value_eur", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set_title('5 players with highest value ')

#This funciton will graphically displays the 10 players with the largest number of player_traits.
def display_player3():
    cur, conn = connect_db()
    q1 = pd.read_sql_query(
        '''select short_name, count(player_traits)as count_traits
           from fifa.players_20  
           group by short_name
           order by count(player_traits) desc
           limit 28''', conn)
    df = pd.DataFrame(q1, columns=['short_name', 'count_traits'])
    return df
    save_and_terminate_connection(cur, conn)
df=display_player3()
sns.set_style("whitegrid")
ax=sns.barplot(x="short_name", y="count_traits", data=df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
ax.set_title('10 players with highest player traits ')