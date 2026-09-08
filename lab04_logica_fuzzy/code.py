#!pip install scikit-fuzzy
from skfuzzy import control, gaussmf, zmf, smf, trimf
import matplotlib.pyplot as plt
import numpy as np

############################## <- Linha de # = Separação de bloco no notebook python 

#entradas
distancia = control.Antecedent(np.arange(0, 101, 1), 'distancia')
velocidade = control.Antecedent(np.arange(0, 101, 1), 'velocidade')

#saida
pressao_freio = control.Consequent(np.arange(0, 101, 1), 'pressao_freio')

#############################

#valores distancia
distancia['curta'] = trimf(distancia.universe, [0, 0, 40])
distancia['media'] = trimf(distancia.universe, [20, 50, 80])
distancia['longa'] = trimf(distancia.universe, [60, 100, 100])

#valores velocidade
velocidade['lenta'] = trimf(velocidade.universe, [0, 0, 40])
velocidade['moderada'] = trimf(velocidade.universe, [20, 50, 80])
velocidade['rapida'] = trimf(velocidade.universe, [60, 100, 100])

#valores pressao_freio
pressao_freio['suave'] = trimf(pressao_freio.universe, [0, 0, 40])
pressao_freio['media'] = trimf(pressao_freio.universe, [20, 50, 80])
pressao_freio['forte'] = trimf(pressao_freio.universe, [60, 100, 100])

################################

#view raw
distancia.view()
velocidade.view()
pressao_freio.view()

###############################

#definindo regras
regra1 = control.Rule(distancia['curta'] & velocidade['rapida'], pressao_freio['forte'])
regra2 = control.Rule(distancia['media'] & velocidade['moderada'], pressao_freio['media'])
regra3 = control.Rule(distancia['longa'] & velocidade['lenta'], pressao_freio['suave'])

# Montando o sistema de controle
regras_freio = control.ControlSystem([regra1, regra2, regra3])
freio_controle = control.ControlSystemSimulation(regras_freio)

# Definindo as entradas (exemplo: distância 20 e velocidade 60)
freio_controle.input['distancia'] = 30
freio_controle.input['velocidade'] = 70

# Computando o resultado
freio_controle.compute()

###############################

distancia.view(sim=freio_controle)
velocidade.view(sim=freio_controle)
print(freio_controle.output['pressao_freio'])
pressao_freio.view(sim=freio_controle)