#create schema
create schema fifa;

#create table
CREATE TABLE fifa.players_20 (
	sofifa_id INT NOT NULL, 
	player_url VARCHAR(100) NOT NULL, 
	short_name VARCHAR(100) NOT NULL, 
	long_name VARCHAR(100) NOT NULL, 
	age INT NOT NULL, 
	dob DATE NOT NULL, 
	height_cm DECIMAL NOT NULL, 
	weight_kg DECIMAL NOT NULL, 
	nationality VARCHAR(100) NOT NULL, 
	club VARCHAR(100) NOT NULL, 
	overall DECIMAL NOT NULL, 
	potential DECIMAL NOT NULL, 
	value_eur DECIMAL NOT NULL, 
	wage_eur DECIMAL NOT NULL, 
	player_positions VARCHAR(100) NOT NULL, 
	preferred_foot VARCHAR(100) NOT NULL, 
	international_reputation DECIMAL NOT NULL, 
	weak_foot DECIMAL NOT NULL, 
	skill_moves DECIMAL NOT NULL, 
	work_rate VARCHAR(100) NOT NULL, 
	body_type VARCHAR(100) NOT NULL, 
	real_face BOOLEAN NOT NULL, 
	release_clause_eur DECIMAL, 
	player_tags VARCHAR(500), 
	team_position VARCHAR(100), 
	team_jersey_number DECIMAL, 
	loaned_from VARCHAR(100), 
	joined DATE, 
	contract_valid_until DECIMAL, 
	nation_position VARCHAR(100), 
	nation_jersey_number DECIMAL, 
	pace DECIMAL, 
	shooting DECIMAL, 
	passing DECIMAL, 
	dribbling DECIMAL, 
	defending DECIMAL, 
	physic DECIMAL, 
	gk_diving DECIMAL, 
	gk_handling DECIMAL, 
	gk_kicking DECIMAL, 
	gk_reflexes DECIMAL, 
	gk_speed DECIMAL, 
	gk_positioning DECIMAL, 
	player_traits VARCHAR(500), 
	attacking_crossing DECIMAL NOT NULL, 
	attacking_finishing DECIMAL NOT NULL, 
	attacking_heading_accuracy DECIMAL NOT NULL, 
	attacking_short_passing DECIMAL NOT NULL, 
	attacking_volleys DECIMAL NOT NULL, 
	skill_dribbling DECIMAL NOT NULL, 
	skill_curve DECIMAL NOT NULL, 
	skill_fk_accuracy DECIMAL NOT NULL, 
	skill_long_passing DECIMAL NOT NULL, 
	skill_ball_control DECIMAL NOT NULL, 
	movement_acceleration DECIMAL NOT NULL, 
	movement_sprint_speed DECIMAL NOT NULL, 
	movement_agility DECIMAL NOT NULL, 
	movement_reactions DECIMAL NOT NULL, 
	movement_balance DECIMAL NOT NULL, 
	power_shot_power DECIMAL NOT NULL, 
	power_jumping DECIMAL NOT NULL, 
	power_stamina DECIMAL NOT NULL, 
	power_strength DECIMAL NOT NULL, 
	power_long_shots DECIMAL NOT NULL, 
	mentality_aggression DECIMAL NOT NULL, 
	mentality_interceptions DECIMAL NOT NULL, 
	mentality_positioning DECIMAL NOT NULL, 
	mentality_vision DECIMAL NOT NULL, 
	mentality_penalties DECIMAL NOT NULL, 
	mentality_composure DECIMAL NOT NULL, 
	defending_marking DECIMAL NOT NULL, 
	defending_standing_tackle DECIMAL NOT NULL, 
	defending_sliding_tackle DECIMAL NOT NULL, 
	goalkeeping_diving DECIMAL NOT NULL, 
	goalkeeping_handling DECIMAL NOT NULL, 
	goalkeeping_kicking DECIMAL NOT NULL, 
	goalkeeping_positioning DECIMAL NOT NULL, 
	goalkeeping_reflexes DECIMAL NOT NULL, 
	ls VARCHAR(4), 
	st VARCHAR(4), 
	rs VARCHAR(4), 
	lw VARCHAR(4), 
	lf VARCHAR(4), 
	cf VARCHAR(4), 
	rf VARCHAR(4), 
	rw VARCHAR(4), 
	lam VARCHAR(4), 
	cam VARCHAR(4), 
	ram VARCHAR(4), 
	lm VARCHAR(4), 
	lcm VARCHAR(4), 
	cm VARCHAR(4), 
	rcm VARCHAR(4), 
	rm VARCHAR(4), 
	lwb VARCHAR(4), 
	ldm VARCHAR(4), 
	cdm VARCHAR(4), 
	rdm VARCHAR(4), 
	rwb VARCHAR(4), 
	lb VARCHAR(4), 
	lcb VARCHAR(4), 
	cb VARCHAR(4), 
	rcb VARCHAR(4), 
	rb VARCHAR(4)
);
