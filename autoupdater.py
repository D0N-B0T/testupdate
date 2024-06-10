import os

import sys

import subprocess

import urllib.request

#xD

def get_latest_version(repo_url):

    """

    Descarga el archivo más reciente del repositorio de GitHub.

    """

    latest_file_url = f"{repo_url}/raw/main/autoupdate.py"  # Asegúrate de que esta URL apunta al archivo correcto

    try:

        response = urllib.request.urlopen(latest_file_url)

        latest_script = response.read().decode('utf-8')

        return latest_script

    except Exception as e:

        print(f"Error al descargar la última versión: {e}")

        return None



def update_script(latest_script):

    """

    Reemplaza el archivo actual con el último script descargado.

    """

    current_file = os.path.realpath(__file__)

    try:

        with open(current_file, 'w') as file:

            file.write(latest_script)

        print("Script actualizado con éxito.")

    except Exception as e:

        print(f"Error al actualizar el script: {e}")



def restart_script():

    """

    Reinicia el script.

    """

    try:

        subprocess.Popen([sys.executable] + sys.argv)

        print("Reiniciando el script...")

    except Exception as e:

        print(f"Error al reiniciar el script: {e}")

    sys.exit()



if __name__ == "__main__":

    repo_url = "https://github.com/D0N-B0T/testupdate"  # Cambia esta URL por la de tu repositorio



    print("Comprobando actualizaciones...")

    latest_script = get_latest_version(repo_url)

    

    if latest_script:

        update_script(latest_script)

        restart_script()

    else:

        print("No se pudo obtener la última versión del script.")

