DROP MATERIALIZED VIEW IF EXISTS public.pand_ext;

CREATE MATERIALIZED VIEW public.pand_ext AS
SELECT
    pand.feature_id,
    pand.identificatie,
    pand.bouwjaar,
    pand.status,
    pand.gebruiksdoel,
    pand.oppervlakte_min,
    pand.oppervlakte_max,
	pand.aantal_verblijfsobjecten,
    pand.geom,
    ST_Centroid(pand.geom) as plaatscoordinaten,
    "3dpand".fid,
    "3dpand".b3_h_maaiveld,
    "3dpand".b3_rmse_lod22,
    "3dpand".b3_opp_grond,
    "3dpand".b3_volume_lod22,
    "lod22_2d_agg".b3_h_50p,
    "lod22_2d_agg".b3_h_70p,
    "lod22_2d_agg".b3_h_max,
    "lod22_2d_agg".b3_h_min,
    "lod22_2d_agg".b3_h_70p - "3dpand".b3_h_maaiveld as b3_h_pand,
    energielabels.pand_energieklasse as energieklasse,
    energielabels.pand_gebouwtype as gebouwtype
FROM
    pand
    JOIN "3dpand" ON "3dpand".identificatie = CONCAT('NL.IMBAG.Pand.',pand.identificatie)
    JOIN 
	(
		SELECT 
			MAX(identificatie) as identificatie,
			MAX(b3_h_50p) as b3_h_50p,
			MAX(b3_h_70p) as b3_h_70p,
			MAX(b3_h_max) as b3_h_max,
			MAX(b3_h_min) as b3_h_min
		FROM "lod22_2d" 
		GROUP BY "lod22_2d".identificatie
	) as lod22_2d_agg
	ON "lod22_2d_agg".identificatie = CONCAT('NL.IMBAG.Pand.',pand.identificatie)
    LEFT JOIN "energielabels" ON "energielabels".pand_bagpandid=pand.identificatie;

DROP INDEX IF EXISTS pand_ext_geom_geom_idx;
CREATE INDEX pand_ext_geom_geom_idx
    ON public.pand_ext USING gist
    (geom)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS pand_ext_plaatscoordinaten_geom_idx;
CREATE INDEX IF NOT EXISTS pand_ext_plaatscoordinaten_geom_idx
    ON public.pand_ext USING gist
    (plaatscoordinaten)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS pand_ext_b3_h_pand_double_idx;
CREATE INDEX pand_ext_b3_h_pand_double_idx
    ON public.pand_ext
    (b3_h_pand)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS pand_ext_identificatie_varchar_idx;
CREATE INDEX IF NOT EXISTS pand_ext_identificatie_varchar_idx
    ON public.pand_ext
    (identificatie)
    TABLESPACE pg_default;

DROP INDEX IF EXISTS pand_ext_status_varchar_idx;
-- CREATE INDEX IF NOT EXISTS pand_ext_status_varchar_idx
--     ON public.pand_ext
--      USING HASH (status)
--     TABLESPACE pg_default;
CREATE INDEX IF NOT EXISTS pand_ext_status_varchar_idx
    ON public.pand_ext
    (status)
    TABLESPACE pg_default;

-- REFRESH MATERIALIZED VIEW pand_ext;