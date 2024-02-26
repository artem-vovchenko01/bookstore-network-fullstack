if [ "$1" != "" ]; then
  id=$1
fi
SUBPATH=stores
curl -X DELETE localhost:5000/$SUBPATH/$id -H "Content-Type: application/json"
