-- Creating database and table with some important and traditional requeriments for the 'ID'
-- and also start to manage the foreign key concept.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,	
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
