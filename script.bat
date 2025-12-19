@echo off

echo "construyendo la imagen"
docker compose up -d

echo "esperando que el contenedor se levante"
timeout /t 60 > nul
cls

if not exist "init.sql" (
	echo "no se encontro init.sql en %CD%"
	exit /b 1
)

echo "ejecutando script de la base de datos"
docker exec -i postgres-demo-compose psql -U javarturs -d javarturs_db < init.sql
cls

echo "instalando librerías"
pip install -r requirements.txt