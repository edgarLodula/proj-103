import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "D:\User\Documents\ bijus\python\Projetos\Projeto 103"
to_dir = "D:\User\Documents\ bijus\python\Projetos\Projeto 103\ arquivos_baixados"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("arquivo({event.src_path}) foi criado")
    def on_modified(self, event):
        print("alguem mudou o arquivo({event.src_path})")
    def on_moved(self, event):
        print("arquivo({event.src_path}) foi movido")
    def on_deleted(self, event):
        print("arquivo({event.src_path}) foi deletado")        

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


while True:
    time.sleep(2)
    print("executando...")
    