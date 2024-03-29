DROP MATERIALIZED VIEW IF EXISTS public.perceel_n2000 CASCADE;

CREATE MATERIALIZED VIEW public.perceel_n2000 AS
SELECT 
    perceel.ogc_fid, 
    (
        SELECT ST_Distance(perceel.begrenzingperceel::geography, n2000.geom::geography)
        FROM n2000
        ORDER BY perceel.begrenzingperceel <-> n2000.geom
        LIMIT 1
    ) as n2000_dist_min
FROM perceel;

DROP INDEX IF EXISTS perceel_n2000_ogc_fid_int_idx;
CREATE INDEX IF NOT EXISTS perceel_n2000_ogc_fid_int_idx
    ON public.perceel_n2000
    (ogc_fid)
    TABLESPACE pg_default;