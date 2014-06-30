cuffs
=====

A username/password holder created with Python 2.7

Run:
>python cuffs.py

* Use: Allows user to store private login information such as username/passwords.

* Encryption/Decryption method: A simple character-to-ASCII shift by a hardcoded key in the program.

* Protection: ".cuffs" is created with a hidden extension. When opening this .cuffs file, no valuable information can be obtained from it.

- Encrypted data in the ".cuffs" file shows: 
>Frf^?ts2C%Zxjwsfrj?%xtrjzxjw1%Ufxx|twi?%xtrjufxx|twi^O
- Actual data: 
>Amazon-> Username: someuser, Password: somepassword



* Things to Note: A ".cuffs" file will be created in the same directory, so if cuffs.py is moved or deleted, be sure to also delete the .cuffs file.



