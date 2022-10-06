-- Script that lists all the cities of California that can be found in the hbtn_0d_usa database
SELECT id, name
    FROM cities
    WHERE state_id = (SELECT id FROM states name = 'California');
