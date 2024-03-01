EXPLAIN (FORMAT JSON, ANALYSE)
SELECT
    perceel_ext.identificatie AS perceel_ext_identificatie
FROM
    perceel_ext
    LEFT JOIN pand_ext ON ST_Intersects(perceel_ext.begrenzingperceel, pand_ext.geom)
WHERE
    pand_ext.status = 'Bouwvergunning verleend'
GROUP BY
    perceel_ext.identificatie