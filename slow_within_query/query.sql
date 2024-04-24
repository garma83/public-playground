EXPLAIN (ANALYZE true, FORMAT json)  SELECT
    plots.ogc_fid,
	COUNT(*)
FROM
    perceel
	LEFT JOIN addresses ON ST_DWithin(plots.geom::geography, addresses.geom::geography, 5000)
GROUP BY
    plots.ogc_fid
	LIMIT 100;