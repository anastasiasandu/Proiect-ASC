# Proiect 0x00-ASC
Rezolvare partea a doua: <br />py
Echipa noastra: ErrorsGenerators vs echipa adversa: Unbreakables <br />
Parola echipei adverse  : Unbreakable2021 <br />
Pentru prima parte am creat un script findkey1.py in python care xoreaza primele 30 de caractere din input.txt cu primele 30 de caractere din output, iar apoi verifica ce sir se repeta pentru a gasii cheia. <br />
Metoda de rulare partea intai:  <br />
python3 findkey1.py <nume_fisier_input> <nume_fisier_output> <br />
nume_fisier_input : input.txt <br />
nume_fisier_output :  output <br />
Pentru a doua parte am gasit pe internet un cod ajutator care realizeaza decriptarea unui text criptat si afla cheia acestuia (se foloseste doar de textul criptat). Am adaptat acest cod pentru cerinta noastra. <br />
Metoda de rulare partea a doua : <br />
python3 findkey2.py -i <nume_fisier_input> -m 32 -f 32 -d <br />
nume_fisier_input : output <br />
Link-ul de la cod se gaseste in partea de surse de inspiratie <br />
Introducere <br />
Cerinta proiectului:<br /
Scrieți scripturi python encrypt.py/decrypt.py care iau ca parametru în linia de comandă o cheie și un
fișier și realizează criptarea/decriptarea XOR folosind cheia dată. Programul va folosi cheia pentru a
cripta conținutul fișierului.<br />
Membrii echipei:<br />
Hurloi Selena Andreea (grupa 142)<br />
Sandu Anastasia (grupa 142)<br />
Utilizare
Mediu de lucru:<br />
Python 3.10.0<br />
Metoda de rulare<br />
python3 xor.py parola <nume_fisier_input> <nume_fisier_output><br />
criptare: nume_fisier_input: input.txt;  nume_fisier_output output.txt;<br />
decriptare: nume_fisier_input: output.txt; nume_fisier_output: input_recuperat.txt;<br />
Surse de inspiratie: https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/ https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password https://ro.myservername.com/python-file-handling-tutorial#Binary_files_in_Python https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_xor_process.htm https://reverseengineering.stackexchange.com/questions/11033/how-to-decrypt-data-in-binary-file-by-xor-operator-using-a-given-key-at-specific https://dev.to/anishde12020/cryptography-with-python-using-fernet-40o3 https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/ https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python https://www.w3schools.com/python/ref_string_encode.asp https://www.abhishekshukla.com/python/adventures-in-cryptography-with-python-xor-cipher/ https://stackoverflow.com/questions/50509017/how-is-int-from-bytes-calculated https://www.youtube.com/watch?v=2j7fD92g-gE https://www.youtube.com/watch?v=s1PvPvDWG08&t=1129s +colegi :D <br />
Link cod ajutator : https://github.com/AlexFSmirnov/xor-decrypt 
