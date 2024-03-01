DROP MATERIALIZED VIEW IF EXISTS public.perceel_ext;

CREATE MATERIALIZED VIEW public.perceel_ext AS

SELECT
    perceel.ogc_fid,
    perceel.gml_id,
    perceel.identificatie,
    perceel.begingeldigheid,
    perceel.kadastralegemeentecode,
    perceel.kadastralegemeentewaarde,
    perceel.sectie,
    perceel.perceelnummer,
    perceel.typeoppervlakwaarde,
    perceel.begrenzingperceel,
    perceel.plaatscoordinaten,
    CONCAT(perceel.kadastralegemeentewaarde,' ',perceel.sectie,' ',perceel.perceelnummer) as plotcodesummary,
    MAX(perceel_bouwvlak.bouwvlak_oppervlakte) as bouwvlak_oppervlakte,
    MAX(perceel_pand.pand_oppervlakte_min) as pand_oppervlakte_min,
    MAX(perceel_pand.pand_count) as pand_count,
    MAX(perceel_pand.pand_oppervlakte_min / NULLIF(perceel.typeoppervlakwaarde, 0)) as perceel_pand_oppervlakte_ratio,
	MAX(perceel_pand.pand_oppervlakte_min / NULLIF(perceel_bouwvlak.bouwvlak_oppervlakte, 0)) as bouwvlak_pand_oppervlakte_ratio
FROM
    perceel
    LEFT JOIN perceel_bouwvlak ON perceel.ogc_fid = perceel_bouwvlak.ogc_fid
    LEFT JOIN perceel_pand ON perceel.ogc_fid = perceel_pand.ogc_fid
GROUP BY
    perceel.ogc_fid;

DROP INDEX IF EXISTS perceel_ext_begrenzingperceel_geom_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_begrenzingperceel_geom_idx
    ON public.perceel_ext USING gist
    (begrenzingperceel)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_plaatscoordinaten_geom_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_plaatscoordinaten_geom_idx
    ON public.perceel_ext USING gist
    (plaatscoordinaten)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_typeoppervlakwaarde_int_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_typeoppervlakwaarde_int_idx
    ON public.perceel_ext
    (typeoppervlakwaarde)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_bouwvlak_pand_oppervlakte_ratio_int_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_bouwvlak_pand_oppervlakte_ratio_int_idx
    ON public.perceel_ext
    (bouwvlak_pand_oppervlakte_ratio)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_perceel_pand_oppervlakte_ratio_int_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_perceel_pand_oppervlakte_ratio_int_idx
    ON public.perceel_ext
    (perceel_pand_oppervlakte_ratio)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_plotcodesummary_int_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_plotcodesummary_int_idx
    ON public.perceel_ext
    (plotcodesummary)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS perceel_ext_identificatie_int_idx;
CREATE INDEX IF NOT EXISTS perceel_ext_identificatie_int_idx
    ON public.perceel_ext
    (identificatie)
    TABLESPACE pg_default;

-- REFRESH MATERIALIZED VIEW perceel;