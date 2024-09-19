import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configurar el logging para obtener más información sobre los eventos
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

from_dir = r"C:/Users/Joel Botero/Downloads"  # Verifica que esta ruta sea correcta

# Clase Event Handler 
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        logging.info(f"¡Oye, {event.src_path} ha sido creado!")

    def on_deleted(self, event):
        logging.info(f"¡Oye, alguien borró {event.src_path}!")

    def on_modified(self, event):
        logging.info(f"¡Hola, {event.src_path} ha sido modificado!")

    def on_moved(self, event):
        logging.info(f"¡Alguien movió {event.src_path} a {event.dest_path}!")

# Inicia clase Event Handler 
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa el Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Comienza el Observer
observer.start()

try:
    while True:
        time.sleep(2)
        logging.info("Observando cambios en el directorio...")
except KeyboardInterrupt:
    logging.info("Deteniendo el observador...")
    observer.stop()

observer.join()
