# CleanIt Project

Este projeto surgiu da necessidade de organizar a minha pasta de Downloads por se encontrar  desorganizada, misturando documentos importantes, fotos, instaladores, etc…

Com este problema em mente, decidi desenvolver uma solução que permitisse automatizar o processo de organizar todos os ficheiros de um diretório à escolha do utilizador para diferentes diretórios conforme as respetivas extensões.

A solução CleanIt utilizou as seguintes ferramentas:

* Python ^3.11.0
* Click ^8.1.7
* Path ^16.9.0
* Poetry 1.7.1   (Poetry mandatory in user's machine)
* PyTest ^7.4.3

( Esta solução também permite apagar toda a organização que foi efetuada para as pastas do Desktop e criar o caos total novamente numa pasta à escolha. )


## Getting started

First of, if you are extracting the solution from a compressed archive file (.tar.gz), the first step should be to extract the project using: `tar xvzf cleanit_project-1.0.0.tar.gz`

The next step is to install all the essential libraries, which can be done using the following commands (Poetry must be installed in the user’s machine): `poetry install`

The output should look like this:

``` 
>> poetry install

Creating virtualenv cleanit-project-PGoL1Ov1-py3.12 in /Users/joaomartins/Library/Caches/pypoetry/virtualenvs
Updating dependencies
Resolving dependencies... (1.0s)

Package operations: 6 installs, 0 updates, 0 removals

  Installing iniconfig (2.0.0)
  Installing packaging (23.2)
  Installing pluggy (1.3.0)
  Installing click (8.1.7)
  Installing path (16.9.0)
  Installing pytest (7.4.3)

Writing lock file

Installing the current project: cleanit_project (1.0.0)
```

After the poetry dependencies are installed and resolved, the new environment was also created.

In order to activate the poetry environment the user must run: poetry shell

Now, you are ready to go and run the multiple commands the application has to offer.


## Apply CleanIt command

To run the solution that will clean a specific folder of the user and send the organised files to an user choice’s, the following command must be applied: `poetry run cleanit`

The program will ask the user which is the folder he wants to organise _**<path_to_clean>**_. The user must insert the absolute path to the directory or else it will clean the Desktop as default.

Next step is to insert the absolute path where we want to send the organised files **_<path_to_send_organized_files>_**. If the user doesn’t insert a valid path to send the files, the program will keep the files in the same directory as default.

The output should look like this:

```
>> poetry run cleanit

Where do you want to organise? Absolute path []: <path_to_clean>
Where do you want to move files? Absolute path []: <path_to_send_organized_files>
CleanIt PROCESSING
CleanIt PROCESSING .
CleanIt PROCESSING ..
CleanIt PROCESSING ...





        ┌───── •✧✧• ─────┐
        ±   -CLEAN IT-   ± 
        └───── •✧✧• ─────┘
        

--------Cleaning Process RUNNING--------
=> 6 <= files moved from '/Users/joaomartins/Documents' to '/Users/joaomartins/Desktop' folder.
```

## (optional)Apply Chaos command

Although this solution is expected to clean and organise the specified folder, it can also create chaos.  

The main purpose of the chaos command is to send all the files inside the organised folders to a specified directory.

In order to run chaos the user must use the following command: `poetry run chaos`

The output might look like this:

```
>> poetry run chaos

Where do you want to apply CHAOS? Absolute path []: <path_to_apply_chaos>
Where do you want to send CHAOS? Absolute path []: <path_to_send_chaos>
PROCESSING
PROCESSING .
PROCESSING ..
PROCESSING ...





    ┌───── •✧✧• ─────┐
    ±     -CHAOS-    ± 
    └───── •✧✧• ─────┘
    
    
=> 6 <= files moved from '/Users/joaomartins/Desktop' to '/Users/joaomartins/Downloads' folder.
````

## Run tests

All the functionalities, automations, helper's methods were tested using PyTest.

In order to properly run the developed tests applied to this program the user must run the following command:

```
>> poetry run pytest

========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.12.1, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/joaomartins/Documents/Programs/cleanit_project
collected 6 items                                                                                                                                                      

tests/test_chaos_automation.py .                                                                                                                                 [ 16%]
tests/test_clean_automation.py .                                                                                                                                 [ 33%]
tests/test_helpers.py ...                                                                                                                                        [ 83%]
tests/test_paths.py .                                                                                                                                            [100%]

========================================================================== 6 passed in 0.17s ===========================================================================

```



In case of doubt, feel free to contact: **João Ribeiro** <joao.martins.ribeiro@devoteam.com>
