### 🤖 Sales Batch Prediction Model 

![svg](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![svg](https://img.shields.io/badge/dbeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)

Using batch prediciton method to predict total sales of a store.


#### 📌️ First Steps

1. Clone the project

```
    git clone <this-project-github-link>
```
<br>

2. Create a enviroment

```bash
    python3 -m venv venv
    source venv/bin/activate
```
<br>

3. Install dependencies 

```bash
    pip install -r requirements.txt
```
<br>

4. Install a open-source database administration 
[Install DBeaver](https://dbeaver.io/download/)
<br>

5. Create a `.env` file in the `config` folder with database conection information: 

```bash
    DB_USER="my_user"
    DB_PASSWORD="my_password"
    DB_HOST="my_database_ip"
    DB_PORT="my_connection_port"
    DB_DATABASE="my_database_name"
```

#### 🎯 How to run the project

In root folder execute the commands:

```bash
# Train model
python -m src.train.py
```

```bash
# Predict model
python -m src.predict.py
```

To change model configuration, access the files:

* `src/variables/train.py` : change train configuration.
* `src/variables/preditcion.py` : change prediction configuration.


#### 📂️ Folders

* `config/` : Project configuration.
<br>

* `data/` : Content all the data used or created by this project.
<br>

* `models/` : Models created by this project.
<br>

* `notebooks/` : Notebooks for data exploration. 
<br>

* `src/` : Source code for the project.