#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import requests
from pathlib import Path

path_programm=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0]))))))
#print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))))


if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
    if path_programm == '':
        path_programm = "."

print('Programm wird aktualisiert...')
print("""
Liebe:r LaMA-Nutzer:in,
aufgrund einer größeren strukturellen Änderung bei der Installation von
LaMA, muss das Programm neu installiert werden.
Dazu wird auch die Aufgaben-Datenbank noch einmal neu heruntergeladen.
LaMA ist nach erfolgreicher Installation unter "Programme" zu finden. 
Alle bisherigen Ordner von LaMA werden nicht mehr benötigt und können 
anschließend gelöscht werden. 

Die Neuinstallation passiert großteils automatisch, 
kann jedoch mehrere Minuten in Anspruch nehmen. 
Wir bitten um Verständnis!

Sollten Probleme auftreten, bitte kontaktieren Sie uns unter lama.helpme@gmail.com

""")
      
rsp = input("Soll die Neuinstallation von LaMA gestartet werden? (j/n)")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

if rsp=="j":
    print("Neue Version von LaMA wird heruntergeladen ...")

    if sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
        path_installer = os.path.join(
            Path.home(), "Downloads", "LaMA_setup.dmg"
        )

    opened_file=os.path.basename(sys.argv[0])
    name, extension=os.path.splitext(opened_file)

    # newapp_path=os.path.join(path_programm,'LaMA_programdata','_database','_config','update','update_mac','LaMA%s'%extension)
    # mainfile_path=os.path.join(path_programm,'LaMA%s'%extension)

    download_link = (
        "https://github.com/mylama/lama/releases/latest/download/LaMA_setup.dmg"
    )

    try:
        with requests.get(download_link, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 102400  # 1 KB Blöcke
            downloaded = 0
            items = list(range(0, total_size))
            l = len(items)
            printProgressBar(0, l, prefix = 'Download:', length = 50)
            with open(path_installer, 'wb') as f:
                for chunk in r.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        percent = int(downloaded * 100 / total_size)
                        printProgressBar(downloaded, l, prefix = 'Download:',  length = 50)
            print("LaMA wurde erfolgreich heruntergeladen.")
        if sys.platform.startswith('darwin'):  # macOS
            subprocess.call(['open', path_installer])
        os._exit(0)
    except requests.exceptions.ConnectionError:
        print('Das Programm konnte nicht aktualisiert werden. Stellen Sie sicher, dass eine stabile Internetverbindung besteht und versuchen Sie es erneut.' )
        os._exit(0)




# for i, item in enumerate(items):
#     if i==50:
#         if sys.platform.startswith('linux'):
#             p=subprocess.Popen('cp "{0}" "{1}"'.format(newapp_path, mainfile_path), stdout=subprocess.PIPE,shell=True)
#         elif sys.platform.startswith('darwin'):
            
#             p=subprocess.Popen('cp "{0}" "{1}"'.format(newapp_path, mainfile_path), stdout=subprocess.PIPE,shell=True)
#         else:
#             p=subprocess.Popen('copy "{0}" "LaMA{1}"'.format(newapp_path, extension), stdout=subprocess.PIPE,shell=True)

#         (output, err) = p.communicate()
#         p_status=p.wait()

#     sleep(0.01)
#     # Update Progress Bar
#     printProgressBar(i + 1, l, prefix = 'Installation:',  length = 50)

# if p_status==0:
#     print('\nProgramm wurde erfolgreich aktualisiert. Drücken Sie "Enter", um fortzufahren...')
# else:
#     #print(newapp_path)
#     print('\nProgramm konnte nicht aktualisiert werden. Bitte versuchen Sie es später erneut.\nFehler: "%s"\n\nDrücken Sie "Enter", um mit der älteren Version fortzufahren...'%str(output)[2:-5]) 
    
# input()

# if sys.platform.startswith('linux'):
#     if extension=='.py':
#         subprocess.run("python3 " + mainfile_path, shell=True)
#     else:
#         subprocess.run(mainfile_path, shell=True)
# elif sys.platform.startswith('darwin'):
#     os.system(mainfile_path)
#     #subprocess.run("python3 " + mainfile_path, shell=True)
# else:
#     os.startfile(mainfile_path)
 

