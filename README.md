# fishmart.ru

## setup sources
```
mkdir code; \
cd code; \
git clone https://github.com/jintaxi/fishmart.ru.git ; \
cd fishmart.ru; \
python3.9 -m venv fishmart.ru; \
source fishmart.ru/bin/activate; \
pip install -U pip; \
pip install -r requirements.txt
```
## setup cron
`
crontab -e
`
`*/10 * * * * /home/pi/code/fishmart.ru/fishmart.ru/bin/python3.9 /home/pi/code/fishmart.ru/main.py`
