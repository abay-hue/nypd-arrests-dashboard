-- Example insert (replace with COPY FROM or INSERT SELECT)
-- COPY fact_arrests FROM 'path/to/extract.csv' CSV HEADER;
-- Example aggregation view:
CREATE OR REPLACE VIEW vw_arrests_by_precinct AS
SELECT precinct_id, COUNT(*) AS arrests
FROM fact_arrests
GROUP BY 1;
