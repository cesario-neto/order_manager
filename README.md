# Projeto Gerenciador de pedidos

Este é um projeto extremamente simples que criar pedidos em um banco de dados, que pode ser associados produtos no pedido e no final, faz o calculo do total

- Clonando repositorio
```
git clone https://github.com/cesario-neto/order_manager.git
```

- Para **Windows**:
```
cd order_manager
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py migrate
```

- Para **Linux**:
```
cd order_manager
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

Inicialmente, deve-se criar os produtos que seram comercializados no admin do projeto, após isso, passamos a usar as proprias templates do projeto para criar os pedidos e anexar produtos ao mesmo.
