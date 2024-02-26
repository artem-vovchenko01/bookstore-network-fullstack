id=$(docker ps | grep 'frontend' | awk '{print $1}')

# docker exec DOTNET bash -c "cd /root; $*"

docker logs -f $id
