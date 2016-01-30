:: Cmd: runner "cmd.exe /c run.bat"
:: Ce script est un exemple pour exécuter votre solution sous Windows
:: py.exe solution.py

:: Décommentez les lignes suivantes si vous utilisez Java:
@echo off
javac solution.java > NUL
java solution

:: Ajoutez vos propres commandes si vous utilisez un autre langage.
:: Assurez-vous d'ajouter "> NUL" aux commandes de compilation.
