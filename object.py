from dataclasses import dataclass
import numpy as np
from random import randint, choice

def ID_generate():
    ID = randint(1, 999)
    return ID


@dataclass
class Player:
    "Class of declaration player"
    ID: int = ID_generate()
    NAME: str = ''
    # LEVEL: int = 0
    LIFE: int = 1
    MANA: int = 1
    RESISTANCE: int = 1
    STRENGTH: int = 1
    DEXTERITY: int = 1
    INTELLIGENCE: int = 1
    FAITH: int = 1
    AGILITY: int = 1
    # EQUIPAMENT: str = 'Híbrido'


    def Return(self):
        # Atributos padrão básico
        total_life = 100.0 
        total_intelligence = 15.0
        total_faith = 8.3
        total_resistance = total_strength = total_dexterity =  10.0
        total_agility = 1.0
        total_mana = 30.0
        total_weight = 0.0

        # Dados vão ser puxados do banco de dados -> Esses aqui são só por implementação do programa

        # def Level_confirm(self):
        #     attribute_list = [self.LIFE, self.MANA, self.RESISTANCE, self.STRENGTH, self.DEXTERITY,
        #                  self.INTELLIGENCE, self.FAITH, self.AGILITY]
        #     assert self.LEVEL == sum(attribute_list), "Attribute count differs from level"
        #     return True if False else False

        def Life(self) -> self.LIFE:
            nonlocal total_life
            lv = self.LIFE

            np.random.seed(7081 + lv)

            total_life = (np.random.uniform(low=4, high=7, size=15)* lv) + total_life 
            total_life = total_life[np.random.randint(0, len(total_life), (1,))] # Randomização para pegar um entre os 15 elementos
            self.LIFE = round(total_life.item(), 2)
            return self.LIFE
        
        def Mana(self) -> self.MANA:
            nonlocal total_mana
            lv = self.MANA

            np.random.seed(2142 + lv)

            total_mana = (np.random.uniform(low=6, high=8, size=15)* lv) + total_mana 
            total_mana = total_mana[np.random.randint(0, len(total_mana), (1,))] # Randomização para pegar um entre os 15 elementos
            return round(total_mana.item(), 2)            
        
        def Resistance(self) -> self.RESISTANCE:
            # TODO: Implementar sistema de peso máximo que pode ser carregado
            nonlocal total_resistance
            lv = self.RESISTANCE

            np.random.seed(4667 + lv)

            total_resistance = (np.random.uniform(low=4, high=7, size=15)* lv) + total_resistance 
            index = np.random.randint(0, len(total_resistance), (1,)) # Randomização para pegar um entre os 15 elementos
            converter = ''.join([x for x in str((total_resistance[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100

        def Strength(self) -> self.STRENGTH:
            nonlocal total_strength
            lv = self.STRENGTH

            np.random.seed(8902 + lv)

            total_strength = (np.random.uniform(low=2, high=6, size=15)* lv) + total_strength 
            index = np.random.randint(0, len(total_strength), (1,)) # Randomização para pegar um entre os 15 elementos
            converter = ''.join([x for x in str((total_strength[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100 # dano + (dano * (Strenght/100))

        def Intelligence(self) -> self.INTELLIGENCE:
            nonlocal total_intelligence
            lv = self.INTELLIGENCE

            np.random.seed(1413 + lv)

            total_intelligence = (np.random.uniform(low=2, high=5, size=15)* lv) + total_intelligence 
            index = np.random.randint(0, len(total_intelligence), (1,)) # Randomização para pegar um entre os 15 elementos
            converter = ''.join([x for x in str((total_intelligence[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100

        def Faith(self) -> self.FAITH:
            nonlocal total_faith
            lv = self.FAITH

            np.random.seed(6901 + lv)

            total_faith = (np.random.uniform(low=2, high=5, size=15)* lv) + total_faith 
            index = np.random.randint(0, len(total_faith), (1,)) # Randomização para pegar um entre os 15 elementos
            converter = ''.join([x for x in str((total_faith[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100
        
        def Weight(self) -> total_weight:
            nonlocal total_weight
            total_weight = 70.0 #Kg
            print('Peso:', total_weight + float(str(total_life.item())[0:2]))
            return total_weight + float(str(total_life.item())[0:2])

        def Agility(self) -> self.AGILITY: # velocidade de movimento
            # TODO: Implementar sistema de penalidade de movimento por sobrepeso 
            nonlocal total_agility
            lv = self.AGILITY

            total_agility = total_agility + (lv / 10) # desolacmento em m/s
            return total_agility

        def Dexterity(self) -> self.DEXTERITY: # velocidade de ataque
            nonlocal total_dexterity
            total_dexterity = self.DEXTERITY * 1.4 # A quantidade a ser diminuida até afetar segundos (default 1s)
            weight = int(total_weight)

            match max(self.STRENGTH, self.INTELLIGENCE, self.FAITH):
                case self.STRENGTH:
                    equipament = 'Físico'
                case self.INTELLIGENCE:
                    equipament = 'Mágico'
                case _:
                    equipament = 'Híbrido'

            if equipament == 'Físico':
                velocity = 0
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 1:
                    return 1
                return round(total_dexterity, 1)
            elif equipament == 'Mágico':
                velocity = 2
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 2:
                    return 2
                return round(total_dexterity, 1)
            else:
                velocity = 1.4
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 3:
                    return 3
                return round(total_dexterity, 1)
            
            
        def Definition(self):
            self.LIFE = Life(self) 
            self.MANA = Mana(self)
            self.RESISTANCE = Resistance(self)
            self.STRENGTH = Strength(self)
            self.INTELLIGENCE = Intelligence(self)
            self.FAITH = Faith(self)
            self.AGILITY = Agility(self)
            self.DEXTERITY = Dexterity(self)

        # Level_confirm(self) 
        Definition(self)
        Weight(self)


@dataclass
class Enemy:
    "Class of declaration enemy"
    ID: int = ID_generate()
    NAME: str = ''
    DESCRIPTION: str = ''
    DIFFICULTY: str = 'Fácil'
    DAMAGE_TYPE: str = choice(['Híbrido', 'Físico', 'Mágico'])
    LIFE: float = 100.0
    MANA: float = 30.0
    RESISTANCE: int = 1
    STRENGTH: int = 1
    DEXTERITY: int = 1
    INTELLIGENCE: int = 1
    FAITH: int = 1
    AGILITY: int = 1


    def Return(self):
        # Atributos padrão básico
        total_life = self.LIFE
        total_resistance = self.RESISTANCE
        total_intelligence = total_faith = total_dexterity = total_agility = 1.0
        total_strength = self.STRENGTH
        total_weight = 0.0
        total_mana = self.MANA

        match self.DAMAGE_TYPE:
            case 'Híbrido':
                q = 0.0
            case 'Mágico':
                q = -0.2
            case 'Físico':
                q = 0.3

        match self.DIFFICULTY:
                # A IA vai fazer os testes para adaptar o x e y (modificador-> exp:1.6, 1.7)
            case 'Fácil': # randomizar entre 83% ~ 92% de chance de vitória -> se os testes n derem isso, modificar 'q'
                np.random.seed(111)
                modifier =(np.random.uniform(low=1.6 + q, high=1.7 + q, size=15))
                modifier = round((modifier[np.random.randint(0, len(modifier), (1,))]).item(), 2)
            case 'Normal': # 50% ~ 82%
                np.random.seed(112)
                modifier =(np.random.uniform(low=2.5 + q, high=2.7 + q, size=15))
                modifier = round((modifier[np.random.randint(0, len(modifier), (1,))]).item(), 2)
            case 'Difícil': # 27% ~ 49%
                np.random.seed(113)
                modifier =(np.random.uniform(low=2.9 + q, high=3.1 + q, size=15))
                modifier = round((modifier[np.random.randint(0, len(modifier), (1,))]).item(), 2)



        # Dados vão ser puxados do banco de dados -> Esses aqui são só por implementação do programa

        def Life(self) -> self.LIFE:
            nonlocal total_life
            np.random.seed(781)

            total_life = (np.random.uniform(low=4.1, high=4.7, size=15) * modifier**2) * total_life
            total_life = total_life[np.random.randint(0, len(total_life), (1,))] # Randomização para pegar um entre os 15 elementos
            return round(total_life.item(), 2)
        
        def Mana(self) -> self.MANA:
            nonlocal total_mana

            np.random.seed(2142 + int(modifier))

            total_mana = (np.random.uniform(low=6, high=8, size=15) * modifier ** 2) + total_mana 
            total_mana = total_mana[np.random.randint(0, len(total_mana), (1,))] # Randomização para pegar um entre os 15 elementos
            total_mana = round(total_mana.item(), 2)

            match self.DAMAGE_TYPE:
                case 'Híbrido':
                    return round(total_mana + total_mana * 1.3, 2)
                case 'Mágico':
                    return round(total_mana + total_mana * 3.4, 2)
                case 'Físico':
                    return 0.0
        
        def Resistance(self) -> self.RESISTANCE:
            """o status de resistência a dano é um atributo que representa a capacidade do
            personagem de resistir a ataques inimigos sem sofrer dano ou reduzir o dano recebido.
            
            A resistência vai ser a porcentagem do dano a ser diminuido.
            Caso seja maior que o dano, o dano vai ser zerado.

            A resistência do enemy nunca é maior do que a do player.
            """
            nonlocal total_resistance

            # TODO: A fórmula para diminuição do dano é -> dano -= (dano * (total_resistance/100))

            resistance = abs(total_resistance - ((modifier + q * 10) * 2))
            if resistance > total_resistance:
                total_resistance = resistance - total_resistance
                return round(total_resistance, 2)
            else:
                total_resistance = resistance
                return round(total_resistance, 2)
            

        def Strength(self) -> self.STRENGTH:
            """ 
            A força é sempre maior que a do player. Caso seja tipo físico. Se for híbrido, a média entre não
            é discrepante, para que seja balanceado o dano físico e mágico.
            O que afetará a força será o nível de dificuldade, o tipo de inimigo e quantidade de vida.

            A força é um número inteiro igual a resistência que vai servir de multiplicador para os ataques.
            """
            nonlocal total_strength
            lv = self.STRENGTH - modifier
            

            np.random.seed(8200 + int(lv))

            total_strength = (np.random.uniform(low=3.7, high=4, size=15)* abs(lv)) + total_strength 
            index = np.random.randint(0, len(total_strength), (1,)) # Randomização para pegar um entre os 15 elementos
            converter = ''.join([x for x in str((total_strength[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100 # dano + (dano * (Strenght/100))


        def Intelligence(self) -> self.INTELLIGENCE:
            nonlocal total_intelligence
            lv = self.INTELLIGENCE - modifier
            

            np.random.seed(1101 + int(lv))

            total_intelligence = (np.random.uniform(low=4.2, high=4.6, size=15)* abs(lv)) + total_intelligence
            index = np.random.randint(0, len(total_intelligence), (1,))
            converter = ''.join([x for x in str((total_intelligence[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100 

        def Faith(self) -> self.FAITH:
            nonlocal total_faith
            lv = self.FAITH - modifier
            

            np.random.seed(2101 + int(lv))

            total_faith = (np.random.uniform(low=2, high=6, size=15)* abs(lv)) + total_faith
            index = np.random.randint(0, len(total_faith), (1,))
            converter = ''.join([x for x in str((total_faith[index]).item())]) 
            return int(converter[0:converter.index('.')]) / 100 
        
        def Weight(self) -> total_weight:
            # TODO: Implementar aumento do peso com itens
            nonlocal total_weight
            total_weight = 100.0 #Kg
            print('Peso:', total_weight + float(str(total_life.item())[0:3]))
            return total_weight + float(str(total_life.item())[0:3])

        def Agility(self) -> self.AGILITY: # velocidade de movimento
            """
            Velocidade de movimento vai ser afetado pelo peso total
            """
            nonlocal total_agility
            lv = self.AGILITY

            total_agility = total_agility + (lv / 10) # desolacmento em m/s
            w = 0
            for kg in range(1, int(total_weight) + 1):
                w += 0.1

            return total_agility - w

        def Dexterity(self) -> self.DEXTERITY: # velocidade de ataque 
            """
            Velocidade de ataque vai ser afetado pelo peso da arma se for físico,
            inteligência se for mágico e fé se for mágico do outro tipo.
            """
            nonlocal total_dexterity
            total_dexterity = self.DEXTERITY * 1.4 # A quantidade a ser diminuida até afetar segundos (default 1s)
            weight = int(total_weight) 
            equipament = self.DAMAGE_TYPE
            if equipament == 'Físico':
                velocity = 0
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 3:
                    return 3
                return round(total_dexterity, 1) + 2
            elif equipament == 'Mágico':
                velocity = 2
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 5:
                    return 4
                return round(total_dexterity, 1)
            else:
                velocity = 1.4
                for ms in range(1, weight + 1):
                    velocity += ms/10
                total_dexterity -= velocity
                if total_dexterity < 7:
                    return 5
                return round(total_dexterity, 1)
            
        def Definition(self):
            self.LIFE = Life(self) 
            self.MANA = Mana(self)
            self.RESISTANCE = Resistance(self)
            self.STRENGTH = Strength(self)
            self.INTELLIGENCE = Intelligence(self)
            self.FAITH = Faith(self)
            self.AGILITY = Agility(self)
            self.DEXTERITY = Dexterity(self)
            
        Definition(self)
        Weight(self)