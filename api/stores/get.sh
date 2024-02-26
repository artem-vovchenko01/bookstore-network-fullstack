id=1
if [ "$1" != "" ]; then
  id=$1
fi
SUBPATH=stores
curl -X GET localhost:5000/$SUBPATH/$id -H "Content-Type: application/json"
curl -X GET localhost:5000/$SUBPATH/$id -H "Content-Type: application/json" | jq
