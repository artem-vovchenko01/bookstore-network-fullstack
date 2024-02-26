SUBPATH=stores
curl -X PUT localhost:5000/$SUBPATH/5 -H "Content-Type: application/json" -d \
  "{
    \"id\" : 5,
    \"name\" : \"7 habits\", 
    \"description\" : \"Self-improvement book\",
    \"categoryId\" : 3,
    \"type\" : \"paper\",
    \"pages\" : 750,
    \"lang\" : \"US\",
    \"author\" : \"Steven\",
    \"publisher\" : \"Oxford Press\",
    \"year\" : 2015
  }" | jq

