echo " > Starting to configure the project  ..."

echo "   [INFO] Getting environment variables "
python3 ./environment.py


echo "   [INFO] Create database connection "
python3 ./database.py