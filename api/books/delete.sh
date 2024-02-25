if [ "$1" != "" ]; then
  id=$1
fi
curl -X DELETE localhost:5000/books/$id -H "Content-Type: application/json"
