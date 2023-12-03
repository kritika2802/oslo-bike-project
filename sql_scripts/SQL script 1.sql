  
SELECT 
    avg(Duration) as [avg_dur]
FROM OPENROWSET(
        BULK 'https://kritikastorage.dfs.core.windows.net/oslo-city-bike/historical-data/*.csv',
        FORMAT = 'CSV', 
        HEADER_ROW = TRUE,
        PARSER_VERSION = '2.0'
    ) avg_durr
    WHERE DATEPART(year, ended_at) = 2022
        ;

