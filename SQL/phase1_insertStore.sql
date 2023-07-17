-- inserting supertore location - not available East on Ontario
insert into stores (merchant_id, province_id, merchant_storeid, location_name)
values (1,	1,	2,	'1077',	'GRANDVIEW - VANCOUVER'),
       (1, 1, '1590', 'EAST VILLAGE - CALGARY'),
	   (1, 3, '1505', 'MCPHILLIPS - WINNIPEG'),
	   (1, 7, '1077', 'DON MILLS AND EGLINTON'),
	   (1, 10, '1533', 'GOLDEN MILE');

-- noFrills - not available Eat of ontario
insert into stores (merchant_id, province_id, merchant_storeid, location_name)
values (2, 2, '3641', 'BRANDON & JOANNY''S NOFRILLS VANCOUVER'),
	   (2, 1, '3628', 'STEVE''S NOFRILLS SPRUCE GROVE'),
	   (2, 3, '7141', 'CHRIS'' NOFRILLS WINNIPEG'),
	   (2, 10, '3978', 'CRAWFORD''S NOFRILLS REGINA'),
	   (2, 7, '3643', 'ROCCO''S NOFRILLS TORONTO');

-- SaveOnFoods
insert into stores (merchant_id, province_id, merchant_storeid, location_name)
values (4,	2,	"2249",	"Capilano"),
       (4, 1, '6633', 'Calgary - Richmond Square'),
	   (4, 3, '4415', 'St James'),
	   (4, 10, '5505', 'Regina South');

-- IGA BC
insert into stores (merchant_id, province_id, merchant_storeid, location_name)
values (5, 2, 'port_moody', 'IGA - Port Moody - Newport (221 Ioco Road)');


-- select query with joins
select stores.store_id, merchants.merchant_name, provinces.province_name, stores.location_name
from stores
left join merchants
on stores.merchant_id = merchants.merchant_id
left join provinces
on stores.province_id = provinces.province_id
order by store_id
