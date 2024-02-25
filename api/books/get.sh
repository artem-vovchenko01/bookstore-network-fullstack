id=1
if [ "$1" != "" ]; then
  id=$1
fi
curl -X GET localhost:5000/books/$id -H "Content-Type: application/json"
curl -X GET localhost:5000/books/$id -H "Content-Type: application/json" | jq
