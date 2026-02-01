import webbrowser
from time import sleep

print("Jesus já voltou o aceite e viva eternamente")

def abrir_video_youtube(video_id, params=""):
  """Abre o link do YouTube especificado em um navegador.

  Args:
    video_id: O ID do vídeo do YouTube.
    params: Parâmetros adicionais da URL.
  """

  url = f"https://youtu.be/{video_id}?{params}"
  webbrowser.open(url)

# Exemplo de uso:
video_id = "-oBfkrpqW1M"
params = "si=r-kvyDYYJn1j-6Nv"
abrir_video_youtube(video_id, params)
sleep(109)