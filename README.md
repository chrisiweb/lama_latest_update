# LaMA - LaTeX Mathematik Assistent
*Aktuelle Version: [v4.6.2]*

__LaMA ist ein Programm, das AHS-Mathematiklehrer·innen das systematische Abspeichern von Unterstufen-, Oberstufen-Typ1- und Oberstufen-Typ2-Aufgaben ermöglicht. LaMA erleichtert die Suche dieser Aufgaben sowie die Erstellung von Prüfungen, wie Schularbeiten, Grundkompetenzchecks, usw.__  

## CHANGELOG
v4.6.3:
- enable sending service files to developer to ensure better support 
- bug fixes
  
v4.6.2:
- bug fix
  
v4.6.1:
- bug fix: upload content for database not working properly
- bug fix: WW single_subtraction not working
- enable/disable date, when titlepage is switched off
- bug fix: change to German commas in solution of WW
- bug fix: error when no image and not titlepage is selected
- bug fix: gaps in binomials
- enable automatic group creation from LaTeX file
- bug fix: double images are added in sage
- bug fix: avoid futile brackets in WW
- bug fix: import examples with images
- bug fix: errors in WW
- bug fix: rechoose nonogramm, when too small
- bug fix: roman numerals
- bug fix: steps number line
  
v4.6.0:
- new Worksheet Wizard: Primefactorization 
- bug fix: escape KeyError for broken examples creator
- bug fix: hide & shoe items
- bug fix: wizard coordinate system - turn off nonogramm
- bug fix: 'beurteilung' not assigned
- bug fix: number line starting value
- bug fix: wizard error create coordinates system
- bug fix: raise error, if SA name cannot be changed
- bug fix: do not reset solution_off to solution_on

v4.5.2:
- bug fix: error create coordinate system
  
v4.5.1:
- bug fix: Error when creating Add/Subtract worksheets with wizard
- bug fix: Occasional error when creating example with division with 0
    
v4.5.0:
- new: date can no be set "empty"
- new: titlepage can now be changed individually
- bug fix: check for newest update
- bug fix: deleted logo
- bug fix: convert png to eps

v4.4.1:
- bug fix: load LaMA files

v4.4.0:
- new: Worksheet Wizard: "Zahlenstrahl"
- new: enable half points for examples
- bug fix: images with underscores
- bug fix: edit english content
- bug fix: hide developer mode when not active
- bug fix: progress window for loading LaMA files
- bug fix: eliminate MacOS Font Warning
- bug fix: enumerate ww coordinates

v4.3.0:
- new: Worksheet Wizard: "Stellenwerte"
- new: Worksheet Wizard: "Roman Numerals"
- new: Worksheet Wizard: "Coordinate System"
- change of refresh_ddb window
- bug fix: resort items Sek1
- bug fix: edit file, when topic exists

v4.2.1:
- bug fix: create dirs on MacOS
- bug fix: rewrite "_" in title for LaTeX

v4.2.0:
- new: create worksheet for binomial expansions in Worksheet Wizard
- bug fix: correct chosen_program, when changed
- bug fix: edit local saved examples

v4.1.5:
- enable hide/show date in custom sage
- enable hide/show name
- bug fix: wrong initial subchapters in cria creator
- bug fix: error, when latex distribution not installed
- bug fix: refresh_ddb, when srdp-package is updated
- bug fix: refresh_ddb, when json.decodeerror occurs
- bug fix: worksheet wizard - multiplication

v4.1.4:
- bug fix: error when typ2 indivdual edit is opened in user mode

v4.1.3:
- bug fix: show group A/B in Sage, when chosen
- bug fix: show AF when new task ist saved
- new setting option: change search pdf output - newpage 

v4.1.2:
- bug fix: enter text in feedback lineedit (cria)

v4.1.1:
- bug fix: title of "Übungsblatt"
- bug fix: error when single_file is not checked

v4.1.0:
- new: save and use individual grading scales
- new: change language of tasks to English
- bug fix: save new files as user
- bug fix: hide/show items of typ2 tasks
- bug fix: create sage files in one file

v4.0.1:
- bug fix: error when initially installed

v4.0.0:
- new: automatically creating worksheets
- new: convert graphic-files to eps via drag&drop
- new: define eps-quality
- new: enable drag&drop with tasks
- new: import task list
- bug fix: edit typ2 examples in sage

v3.4.3:
- bug fix: create latex files in sage

v3.4.2:
- don't show console on windows
- show latex ouptut in LaMA-Loading Screen
- update "beurteilungsraster"
- create reset_popup variable
- bug fix: load lama files
- bug fix: update srdp-mathematik.sty 


v3.4.1:
- edit GUI from Sage
- bug fix: enable/show page numbering
- enable inital popup window
- bug fix: loading when no internet connection
- bug fix: settings file not complete


v3.4.0:
- new: enable group-variations
- bug fix: edit typ2 examples in sage
- bug fix: use typ2 examples with no introducing text
- bug fix: hide/show items in SAGE
- bug fix: LaMA Cria KO-Checkbox not working
- bug fix: save half points
- bug fix: save & load .lama files

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


