  
SELECT 
    start_station_name, end_station_name, count(*) as trips
FROM OPENROWSET(
        BULK 'https://kritikastorage.dfs.core.windows.net/oslo-city-bike/historical-data/*.csv',
        FORMAT = 'CSV', 
        HEADER_ROW = TRUE,
        PARSER_VERSION = '2.0'
    ) avg_durr
        GROUP BY start_station_name, end_station_name
        ORDER BY trips desc
        ;

