id=1
if [ "$1" != "" ]; then
  id=$1
fi
SUBPATH=stores
curl -X GET localhost:5000/$SUBPATH/ -H "Content-Type: application/json" | jq
