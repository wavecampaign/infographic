from ipyleaflet.basemaps import Bunch

nasaBasemaps = Bunch(
NASAGIBS = Bunch(        
AMSR2SurfPrecipitationRate =     dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/AMSR2_Surface_Precipitation_Rate_Day/default/%s/2km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.AMSR2SurfPrecipitationRate'

),
AMSRU2SeaIceConcentration12 = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/AMSRU2_Sea_Ice_Concentration_12km/default/%s/2km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.AMSRU2SeaIceConcentration12'

),
AquariusSeaSurfaceSalinityL37DayRunningMean = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/Aquarius_Sea_Surface_Salinity_L3_7Day_RunningMean/default/%s/2km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.AquariusSeaSurfaceSalinityL37DayRunningMean'

),
CYGNSSL3WindSpeedDaily = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/CYGNSS_L3_Wind_Speed_Daily/default/%s/2km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.CYGNSSL3WindSpeedDaily'

),
GHRSST_L4_G1SST_Sea_Surface_Temperature = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/GHRSST_L4_G1SST_Sea_Surface_Temperature/default/%s/1km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.GHRSST_L4_G1SST_Sea_Surface_Temperature'

),
GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI/default/%s/2km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.GRACE_Tellus_Liquid_Water_Equivalent_Thickness_Mascon_CRI'

),
MODIS_Aqua_Chlorophyll_A = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/MODIS_Aqua_Chlorophyll_A/default/%s/1km/{z}/{y}/{x}.png',
         max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.MODIS_Aqua_Chlorophyll_A'

),
SMAP_L3_Passive_Day_Soil_Moisture = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/SMAP_L3_Passive_Day_Soil_Moisture/default/%s/2km/{z}/{y}/{x}.png',
      max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.SMAP_L3_Passive_Day_Soil_Moisture'

),
SMAP_L3_Sea_Surface_Salinity = dict( 
url='https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/SMAP_L3_Sea_Surface_Salinity_CAP_8Day_RunningMean/default/%s/2km/{z}/{y}/{x}.png',
       max_zoom = 9,
            attribution = 'Imagery provided by services from the Global Imagery Browse Services (GIBS), operated by the NASA/GSFC/Earth Science Data and Information System (<a href="https://earthdata.nasa.gov">ESDIS</a>) with funding provided by NASA/HQ.',
            name = 'NASAGIBS.SMAP_L3_Sea_Surface_Salinity'

)),
NASAPODAAC = Bunch(
ascata_l2_coastal = dict( 
url='https://ops-podaac-tools.jpl.nasa.gov/onearth/wmts/ascata_l2_coastal___wind_speed___2880_x_1440___day/default/%s/EPSG4326_8km/{z}/{y}/{x}.png',
          max_zoom = 9,
          attribution = 'Imagery provided by services from the NASA EOSDIS Physical Oceanography Distributed Active Archive Center (PO.DAAC).',
            name = 'NASAPODAAC.ascata_l2_coastal'

),
jpl_l4_mur_ssta = dict( 
url='https://ops-podaac-tools.jpl.nasa.gov/onearth/wmts/jpl_l4_mur_ssta___ssta___36000_x_18000___daynight/default/%s/EPSG4326_1km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the NASA EOSDIS Physical Oceanography Distributed Active Archive Center (PO.DAAC).',
            name = 'NASAPODAAC.jpl_l4_mur_ssta'

),
modis_a_jpl_l2p = dict( 
url='https://ops-podaac-tools.jpl.nasa.gov/onearth/wmts/modis_a_jpl_l2p_v2014_0___modis_t_jpl_l2p_v2014_0___sst___46080_x_23040___night/default/%s/EPSG4326_500m/{z}/{y}/{x}.png',
          max_zoom = 9,
                  attribution = 'Imagery provided by services from the NASA EOSDIS Physical Oceanography Distributed Active Archive Center (PO.DAAC).',
                  name = 'NASAPODAAC.modis_a_jpl_l2p'

),
oscar_l4_oc_third_deg = dict( 
url='https://ops-podaac-tools.jpl.nasa.gov/onearth/wmts/oscar_l4_oc_third_deg___oceancurrent_speed___1088_x_544___daynight/default/%s/EPSG4326_8km/{z}/{y}/{x}.png',
          max_zoom = 9,
          attribution = 'Imagery provided by services from the NASA EOSDIS Physical Oceanography Distributed Active Archive Center (PO.DAAC).',
          name = 'NASAPODAAC.oscar_l4_oc_third_deg'

),
sea_surface_height_alt_interim_grids = dict( 
url='https://ops-podaac-tools.jpl.nasa.gov/onearth/wmts/sea_surface_height_alt_interim_grids_l4_2sats_5day_6thdeg_v_jpl1609___sla___2160_x_1080___daynight/default/%s/EPSG4326_8km/{z}/{y}/{x}.png',
          max_zoom = 9,
            attribution = 'Imagery provided by services from the NASA EOSDIS Physical Oceanography Distributed Active Archive Center (PO.DAAC).',
            name = 'NASAPODAAC.sea_surface_height_alt_interim_grids'

)
))
