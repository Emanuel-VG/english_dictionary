import urllib.request


def download_file(url, save_path):
    try:
        with urllib.request.urlopen(url) as response, open(save_path, 'wb') as file:
            # Tamaño del archivo (si está disponible)
            file_size = int(response.getheader('Content-Length', 0))
            print(f"Descargando {save_path} ({file_size / 1024:.2f} KB)...")

            # Leer y guardar el archivo en bloques
            chunk_size = 8192
            downloaded = 0
            while chunk := response.read(chunk_size):
                file.write(chunk)
                downloaded += len(chunk)
                print(
                    f"Progreso: {downloaded / file_size * 100:.2f}%", end="\r")

        print(f"\nArchivo guardado en: {save_path}")
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")


# Ejemplo para descargar un archivo
url = "https://example.com/video.mp4"
save_path = "video_descargado.mp4"
download_file(url, save_path)
