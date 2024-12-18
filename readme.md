## 環境構築と動作
conda create -n section7_env flask
conda activate section7_env
conda deactivate

##
export FLASK_APP=myapp.py

##
flask db init
flask db migrate -m "message"
flask db upgrade

pip list --format=freeze > requirements.txt