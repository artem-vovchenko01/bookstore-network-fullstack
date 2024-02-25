curl  -X POST localhost:5000/books/ -H "Content-Type: application/json" -d \
  "{
    \"name\" : \"7 habits of HIGHLY effective people\", 
    \"description\" : \"Self-improvement book\",
    \"categoryId\" : 3,
    \"type\" : \"paper\",
    \"pages\" : 750,
    \"lang\" : \"US\",
    \"author\" : \"Steven\",
    \"publisher\" : \"Oxford Press\",
    \"year\" : 2015
  }" --trace-ascii /dev/stdout  
