import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from startingFile.IFoodDevWeek import nps

# Definição das constantes que usaremos para visualizar o NPS
NPS_ZONAS =   ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
NPS_VALORES = [-100, 0, 50, 75, 100]
NPS_CORES =   ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

def criar_grafico_nps(nps):
  # Inicia a figura e os eixos.
  fig, ax = plt.subplots(figsize=(10, 2))

  # Itera sobre as zonas para criar a barra de cores do gráfico.
  for i, zona in enumerate(NPS_ZONAS):
    ax.barh([0], width=NPS_VALORES[i+1]-NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i])

  # Cria a "seta" que vai indicar o NPS no gráfico.
  ax.barh([0], width=1, left=nps, color='black')
  # Remove os ticks do eixo Y
  ax.set_yticks([])
  # Define os limites do eixo X
  ax.set_xlim(-100, 100)
  # Define os ticks do eixo X
  ax.set_xticks(NPS_VALORES)

  # Inclui um texto com o valor de NPS, o qual ficará alinhado com a "seta" criada anteriormente.
  plt.text(nps, 0, f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black'))

  # Cria a legenda do gráfico
  patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))]
  plt.legend(handles=patches, bbox_to_anchor=(1,1))

  # Inclui um título no gráfico.
  plt.title('Gráfico de NPS da iFood Dev Week')

  # Mostra o gráfico.
  plt.show()

criar_grafico_nps(nps)