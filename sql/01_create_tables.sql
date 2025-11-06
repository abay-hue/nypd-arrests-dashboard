-- Create fact + dims (adjust types as per actual schema)
CREATE TABLE IF NOT EXISTS dim_precinct (
  precinct_id INT PRIMARY KEY,
  borough TEXT
);

CREATE TABLE IF NOT EXISTS fact_arrests (
  arrest_id BIGINT PRIMARY KEY,
  arrest_date DATE,
  age_group TEXT,
  gender TEXT,
  race TEXT,
  offense TEXT,
  precinct_id INT REFERENCES dim_precinct(precinct_id)
);
