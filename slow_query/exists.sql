EXPLAIN (FORMAT JSON, ANALYSE)
SELECT
    perceel_ext.identificatie AS perceel_ext_identificatie
FROM
    perceel_ext
WHERE
    EXISTS (
        SELECT
            1
        FROM
            pand_ext
        WHERE
            ST_Intersects(perceel_ext.begrenzingperceel, pand_ext.geom)
            AND pand_ext.status = 'Bouwvergunning verleend'
    )