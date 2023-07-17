CREATE TABLE IF NOT EXISTS public.brands
(
    brand_id integer NOT NULL DEFAULT 'nextval('brands_brandid_seq'::regclass)',
    brand_name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT brands_pkey PRIMARY KEY (brand_id)
)

CREATE TABLE IF NOT EXISTS public.merchants
(
    merchant_id integer NOT NULL DEFAULT 'nextval('merchants_merchantid_seq'::regclass)',
    merchant_name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT merchants_pkey PRIMARY KEY (merchant_id)
)

CREATE TABLE IF NOT EXISTS public.product_groupings
(
    group_id integer,
    product_id integer,
    CONSTRAINT product_groupings_groupid_fkey FOREIGN KEY (group_id)
        REFERENCES public.product_groups (group_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT product_groupings_productid_fkey FOREIGN KEY (product_id)
        REFERENCES public.products (product_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public.product_groups
(
    group_id integer NOT NULL DEFAULT 'nextval('prodcuts_groups_groupid_seq'::regclass)',
    search_query character varying(255) COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT 'CURRENT_TIMESTAMP',
    CONSTRAINT prodcuts_groups_pkey PRIMARY KEY (group_id)
)

CREATE TABLE IF NOT EXISTS public.products
(
    product_id integer NOT NULL DEFAULT 'nextval('prodcuts_productid_seq'::regclass)',
    product_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    unit_price money,
    total_price money,
    size_amount numeric,
    store_id integer,
    is_available boolean,
    image_url text COLLATE pg_catalog."default",
    merchant_productid character varying(255) COLLATE pg_catalog."default",
    brand_id integer,
    size_unit integer,
    CONSTRAINT prodcuts_pkey PRIMARY KEY (product_id),
    CONSTRAINT fk_products_brands FOREIGN KEY (brand_id)
        REFERENCES public.brands (brand_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_products_meassurement_unit FOREIGN KEY (size_unit)
        REFERENCES public.meassurement_units (unit_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT prodcuts_storeid_fkey FOREIGN KEY (store_id)
        REFERENCES public.stores (store_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE IF NOT EXISTS public.provinces
(
    province_id integer NOT NULL DEFAULT 'nextval('provinces_provinceid_seq'::regclass)',
    province_name character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT provinces_pkey PRIMARY KEY (province_id)
)

CREATE TABLE IF NOT EXISTS public.stores
(
    store_id integer NOT NULL DEFAULT 'nextval('stores_storeid_seq'::regclass)',
    merchant_id integer,
    province_id integer,
    merchant_storeid character varying(255) COLLATE pg_catalog."default",
    location_name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT stores_pkey PRIMARY KEY (store_id),
    CONSTRAINT stores_merchantid_fkey FOREIGN KEY (merchant_id)
        REFERENCES public.merchants (merchant_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT stores_provinceid_fkey FOREIGN KEY (province_id)
        REFERENCES public.provinces (province_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)


CREATE TABLE IF NOT EXISTS public.meassurement_units
(
    unit_id integer NOT NULL DEFAULT 'nextval('meassurement_units_unit_id_seq'::regclass)',
    unit_name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT meassurement_units_pkey PRIMARY KEY (unit_id)
)
