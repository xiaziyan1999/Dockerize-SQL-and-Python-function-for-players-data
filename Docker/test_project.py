import pytest
import psycopg2
import time

def connect_db():
        conn = psycopg2.connect(
                        host="0.0.0.0", 
                        port="5432", #5432
                        user="postgres", 
                        password="mysecretpassword", 
                        database="postgres",
                        options="-c search_path=fifa"
                    )
        cur = conn.cursor()
        return cur, conn
        
def save_and_terminate_connection(cur, conn):
    cur.close()
    conn.commit()
    conn.close()
    

def create_schema(conn):
    with conn as cursor:
        cursor.execute(open("create_table.sql","r").read())



#List the x players who achieved highest improvement across all skillsets.     
def improvement(num):
    command = """  select short_name
                    from fifa.players_20
                    order by ((skill_dribbling+skill_curve+skill_fk_accuracy+skill_long_passing+skill_ball_control)/5)-overall  desc
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany(num)
    return row
    save_and_terminate_connection(cur, conn)

#What are the y clubs that have largest number of players with contracts ending in 2021?
def club_largest_2021(num):
    command = """  select club from fifa.players_20
                    where contract_valid_until=2021
                    group by club
                    order by count(short_name) desc
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany(num)
    return row
    save_and_terminate_connection(cur, conn)

# List the z clubs with largest number of players in the dataset where z >= 5.  
def club_z_greater5(num):
    command = """  select club from fifa.players_20
                    group by club
                    having count(distinct short_name) >=5
                    order by count(distinct short_name)desc,club desc
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany(num)
    return row
    save_and_terminate_connection(cur, conn)

#What is the most popular nation_position in the dataset?
def nation_position():
    command = """  select nation_position from fifa.players_20
                    group by nation_position
                    order by count(nation_position) desc
                    limit 1
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany()
    return row
    save_and_terminate_connection(cur, conn)

#What is the most popular team_position in the dataset?
def team_position():
    command = """  select team_position from fifa.players_20
                    group by team_position
                    order by count(team_position) desc
                    limit 1;
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany()
    return row
    save_and_terminate_connection(cur, conn)

#What is the most popular nationality for the players in the dataset?
def nationality():
    command = """  select nationality from fifa.players_20
                    group by nationality
                    order by count(short_name) desc
                    limit 1;
                    ;"""
    cur, conn = connect_db()
    cur.execute(command)
    row = cur.fetchmany()
    return row
    save_and_terminate_connection(cur, conn)

def test_task2():
    assert improvement(3) is not None, "Returned should not be None"
    assert club_largest_2021(3) is not None, "Returned should not be None"
    assert club_z_greater5(3) is not None, "Returned should not be None"
    assert nation_position() is not None, "Returned should not be None"
    assert team_position() is not None, "Returned should not be None"
    assert nationality() is not None, "Returned should not be None"

    assert len(improvement(3)) == 3, "Returned should be length 3"
    assert len(club_largest_2021(4)) == 4, "Returned should be length 4"
    assert len(club_z_greater5(5)) == 5, "Returned should be length 5"
    assert len(nation_position()) == 1, "Returned should be length 1"
    assert len(team_position()) == 1, "Returned should be length 1"
    assert len(nationality()) == 1, "Returned should be length 1"

    assert improvement(3) == [('T. Haye',), ('Àlex Corredera',), ('Nuno Cedrim',)], "Returned value"
    assert club_largest_2021(4) == [('1. FC Kaiserslautern',), ('FC Ingolstadt 04',), ('FC Girondins de Bordeaux',), ('Kasimpaşa SK',)], "Returned value"
    assert club_z_greater5(5) == [('Wolverhampton Wanderers',), ('West Ham United',), ('Watford',), ('VfL Wolfsburg',), ('Valencia CF',)], "Returned value"
    assert nation_position() == [('SUB',)], "Returned value"
    assert team_position() == [('SUB',)], "Returned value"
    assert nationality() == [('England',)], "Returned value"

conn = connect_db()
create_schema(conn)
time.sleep(20)
nationality()