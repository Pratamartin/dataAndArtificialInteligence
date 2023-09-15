import pandas as pd

# getting the folder file
file = 'D:\\Python - Projects\\dataScienceAndArtificialIntelligence\\csv\\feedbacks.csv'

# reading CSV file
dados = pd.read_csv(file, delimiter=';')

class Feedback:
  def __init__(self, nota, comentario):
    self.nota = nota
    self.comentario = comentario

class AnalisadorFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calcular_nps(self):

    # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
    detratores = sum(1 for feedback in self.feedbacks if feedback.nota <= 6)
    promotores = sum(1 for feedback in self.feedbacks if feedback.nota >= 9)

    return (promotores - detratores) / len(self.feedbacks) * 100

feedbacks = dados.apply(lambda linha: Feedback(linha['nota'], linha['comentario']), axis=1)

analisador = AnalisadorFeedback(feedbacks)
nps = analisador.calcular_nps()

print(nps)

