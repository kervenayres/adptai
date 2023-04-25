from fastapi import FastAPI
import json
from object import Player, Enemy
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuração do CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def processar_json(dados_json: dict):
    # processar o JSON recebido aqui e retornar uma resposta
    player = Player(
        NAME=dados_json['NAME'],
        LIFE=dados_json['LIFE'],
        MANA=dados_json['MANA'],
        RESISTANCE=dados_json['RESISTANCE'],
        STRENGTH=dados_json['STRENGTH'], 
        DEXTERITY=dados_json['DEXTERITY'], 
        INTELLIGENCE=dados_json['INTELLIGENCE'],
        FAITH=dados_json['FAITH'], 
        AGILITY=dados_json['AGILITY'],
    )
    player.Return()
    enemy = Enemy(
        NAME='Enemy',
        DESCRIPTION='Boss',
        DIFFICULTY=dados_json['DIFFICULTY'],
        LIFE=player.LIFE,
        MANA=player.MANA,
        RESISTANCE=player.RESISTANCE,
        STRENGTH=player.STRENGTH, 
        DEXTERITY=player.DEXTERITY, 
        INTELLIGENCE=player.INTELLIGENCE,
        FAITH=player.FAITH, 
        AGILITY=player.AGILITY,
    )
    enemy.Return()

    response = json.dumps(enemy.__dict__)
    return response