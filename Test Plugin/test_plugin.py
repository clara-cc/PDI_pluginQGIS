# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:52:26 2024

@author: Clara

'Code de prise en main d'un plugin test'
"""

#################### IMPORT #############################
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic


################### CLASSE ###############################

class Interface(QDialog):
    
    def __init__(self):
        # constructeur
        super(Interface, self).__init__()
        
        # charge le plugin créer avec Qt Designer
        uic.loadUi(r'C:\Users\Clara\Documents\ENSG\ING2\PDI\Test Plugin\test\Test_dialog_base.ui', self)
        
        self.show()
 
    


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(interface.exec_())

    
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget
# from PyQt5 import uic

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         # Chargement de l'interface utilisateur depuis le fichier .ui
#         uic.loadUi(r'C:\Users\Clara\Documents\ENSG\ING2\PDI\Test Plugin\test\Test_dialog_base.ui', self)
        
#         self.setWindowTitle("Sélection de fichier")
#         self.setGeometry(100, 100, 400, 200)
        
#         # Le bouton est déjà défini dans le fichier .ui, donc vous n'avez pas besoin de le recréer ici
#         # Vous pouvez simplement vous connecter au clic du bouton
#         self.pushButton.clicked.connect(self.open_file_dialog)
    
#     def open_file_dialog(self):
#         file_dialog = QFileDialog()
#         file_path, _ = file_dialog.getOpenFileName(self, "Sélectionnez un fichier", "", "Tous les fichiers (*)")
        
#         if file_path:
#             print("Fichier sélectionné:", file_path)

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()