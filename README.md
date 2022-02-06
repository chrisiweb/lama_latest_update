# LaMA - LaTeX Mathematik Assistent
*Aktuelle Version: [v3.3.0]*

__LaMA ist ein Programm, das AHS-Mathematiklehrer·innen das systematische Abspeichern von Unterstufen-, Oberstufen-Typ1- und Oberstufen-Typ2-Aufgaben ermöglicht. LaMA erleichtert die Suche dieser Aufgaben sowie die Erstellung von Prüfungen, wie Schularbeiten, Grundkompetenzchecks, usw.__  

## CHANGELOG
v3.4.0: [BETA]
- new: automatically creating worksheets
- new: convert graphic-files to eps via drag&drop
- new: define eps-quality
- bugfix: edit typ2 examples in sage

v3.3.0:
- new: show GK-Catalogue
- new: different percentages of grades in LaMA and Cria
- new: 1/2 points for Typ1-examples
- new (admin): save edited files directly in sage
- bug fix: auto-refresh DDB after given intervall
- bug fix: sage - newpage error fixed
- bug fix: keep set infos in sage

v3.2.2:
- bug fix: save .lama file, when create sage file
- bug fix: check internet connection, when editing drafts
- bug fix: enable date in sage
- bug fix: escape error, when database is not refreshed

v3.2.1:
- bug fix: search typ2-files, when no GKs are selected
- bug fix: update srdp-mathematik.sty (& hide tabu.sty)
- bug fix: refresh Miktex FNDB when srdp-tables.sty does not exist
- bug fix: bookmark only for sections

v3.2.0:
- new function: advanced search
- new function: cleanup database (Admin)
- new function: connect file with exisiting images
- bug fix: edit drafts
- bug fix: set title sage
- bug fix: change grade for drafts
- bug fix: edit files with images
- bug fix: speed up load lama file

v3.1.6:
- bug fix: save local variations
- bug fix: compile with -dALLOWPSTRANSPARENCY to enable transparency in new Ghostscript version (> 9.53.3)
- bug fix: feedback combobox
- bug fix: hide/show items
- bug fix: search mode LaMA Cria

v3.1.5:
- bug fix: create automatic groups
- bug fix: create gks in one file
- bug fix: save points and spaces inn .lama-file

v3.1.4:
- bug fix: save lama_settings in AppData folder

v3.1.3:
- bug fix: disable developer mode on mac

v3.1.2:
- bug fix: send feedback
v3.1.1:
- bug fix: error when website is not reachable


v3.1.0:
- new: change mode of "notenschluessel" (half points, percentage)
- new: save individual percentage (notenschluessel)

v3.0.3:
- bug fix: initiate LaMA issues

v3.0.1, v3.02:
- bug fix

v3.0.0:
- move database to GitHub

v2.3.0
 - new function: individual edit of examples
 - new settings: autosave, standard source, dark mode
 - option do not show "notenschluessel" added
 - bug fix: save new examples in cria 

v2.2.1
 - bug fix: Path of PDF-Reader with space returns error

v2.2.0
 - new function: update srdp-mathematik via LaMA
 - new fuction: LaMA settings (define pdf-reader path, pre-choice programm)  
 - bug fix: error when saving variation of L-GKs
 - bug fix: number of examples gets not updated, when example is deleted
 - bug fix: position of scroll bar in sage fixed 
 - bug fix: occasionally more than one example were added when clicked in sage


v2.1.1
 - number GKCs, and show date
 - number=0, means no numbering of headline
 - bug fix: error when saving examples directly in folders

v2.1.0
 - new function: create variation of existing file
 - change to "Zusatzthemen"
 - bug fix: sending feedback raises error via gmail adress
 - bug fix: error when sending "Allgemeine Rückmeldung" in LaMA Cria
 - bug fix: incorrect sorting of typ2 examples
 - bug fix: error when adding examples to Sage
 - bug fix: open PDF on Windows
 - bug fix: error saving local files  

v2.0.3
 - bug fix: save test in different drive
 - bug fix: search examples including drafts
 - bug fix: creating files for users including images
 - bug fix: loading LaMA file through double click

v2.0.2
 - bug fix: error when creating test with 'beurteilungsraster'
 - bug fix: change ausgleichspunkte not working

v2.0.1
 - bug fix: error when app closed and only .tex-file was created
 - bug fix: create groups in sage
 - bug fix: error when creating test in LaMA cria 
 - correct spelling mistake

v2.0.0
 - merge LaMA and LaMA Cria to one program
 - change GUI and color scheme
 - change Loading window

v1.9.1
 - Bug fix: Errors when files with images saved directly 

v1.9.0
  - New: Drafts can be searched and included in tests
  - New: Files can be saved locally and used
  - Bug fix

v1.8.6
  - Bug fix: Edit maximum size for SAGE widgets for small screens

v1.8.5
  - Bug Fix: Update did not work, when permission of update is not changed manually
  - Spacing when creating a test: 99cm= \newpage  


v1.8.4
  - added ScrollArea for "Grundkompetenzen" for small screens
  - "Übungsblatt" and "Nachschularbeit" can be created
  - "Übungsblatt" & "Grundkompetenzcheck" disables Option "Notenschlüssel/Beurteilungsraster"
  - "Schularbeit" can be reseted
  - Creation of .pdf and/or .lama can be skipped, when creating a test


v1.8.3
  - Password for writing bug report removed from source code

v1.8.2
- Bug Fix:
  - Tests cannot be created on macOS, when there are spaces in the filename
  - MacOS raises error when folder is opened after creating a test

v1.8.1
- Bug Fix: No PDF output when SumatraPDF is not installed


