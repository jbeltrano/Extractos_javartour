@echo off

echo "construyendo la imagen"
docker compose up -d

echo "esperando que el contenedor se levante"
timeout /t 60 > nul

if exist "init.sql"

echo "ejecutando script de la base de datos"
docker exec -i postgres-demo-compose psql -U postgres -d testdb < ./Proyecto/Backend/cmd/db/init.sql


echo "instalando librerías"

pip install -r requeriments.txt