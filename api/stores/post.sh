SUBPATH=stores
curl  -X POST localhost:5000/$SUBPATH/ -H "Content-Type: application/json" -d \
  "{
    \"country\" : \"UA\", 
    \"city\" : \"Kyiv\",
    \"address\" : \"Kyiv\",
    \"capacity\" : 100,
    \"utilization\" : 50,
    \"worksFrom\" : 5,
    \"worksUntil\" : 9,
    \"workingDays\" : 5
  }" --trace-ascii /dev/stdout  
