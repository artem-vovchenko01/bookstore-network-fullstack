id=$(docker ps | grep 'nginx' | awk '{print $1}')

# docker exec DOTNET bash -c "cd /root; $*"

docker logs -f $id
