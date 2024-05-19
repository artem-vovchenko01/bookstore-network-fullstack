docker compose stop frontend backend nginx
docker compose up -d --no-deps --build frontend
sleep 4
docker compose up -d --no-deps --build backend
docker compose up -d --no-deps --build nginx
./logs_back.sh
