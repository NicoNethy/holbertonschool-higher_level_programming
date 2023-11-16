-- script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id -- especificar la condición que se debe cumplir para combinar las filas de dos tablas
ORDER BY cities.id ASC;