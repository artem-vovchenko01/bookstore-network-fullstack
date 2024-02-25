id=$(docker ps | grep book_store_network-backend | awk '{print $1}')

# docker exec DOTNET bash -c "cd /root; $*"

docker logs -f $id
