# fishmart.ru

## Setup sources
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

## Setup enviroment
Find [bot token](https://t.me/botfather) and insert it into .zshrc (or .bashrc) at the end of the file in variable `TOKEN`

It will look like `export TOKEN="1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGH"`

## Setup cron
Open `crontab -e`

Then paste this at the end of the file
```
*/10 * * * * /home/pi/code/fishmart.ru/fishmart.ru/bin/python3.9 /home/pi/code/fishmart.ru/main.py
```
