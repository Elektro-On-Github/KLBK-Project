In questo repo trovi il progetto KLBK (KeyLoggerBacKdoor). Leggi questa breve guida su come configurare il tutto.

hack.bat ---> Questo file puó essere eseguito solo in modo esterno a Windows (Consiglio una ISO di WindowsPE), una volta aperto andrá ad eliminare i file di WindowsDefeneder ed andrá a disabilitare l'antivirus permanentemente, conservando l'applicazione UWP nativa di Windows (Per non dare sospetti). Dopo aver disabilitato WinDef andrá a copiarsi su:"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup", per fare in modo che l'eseguibile si esegue ad ogni avvio di Windows, di qualsiasi utente.
script.py ---> Lo script in python che contiene il keylogger e la backdoor.
speaker.ico ---> Icona da inserire durante la compilazione dello script (facoltativo)

=============================================================================


Step 1 -- Editare lo script

Prima di compilare lo script é necessario modificarlo a seconda delle proprie esigenze. 
In poche parole devi andare a modificare il parametro "url" e l'url del ciclo While che trovi ai piedi del codice. Puoi inserire l'url di qualsiasi server web,
sia locale (192.168.x.x, 10.x.x.x, ecc...) o pubblico, compresi domini (esempio: listener.com), per configurare un server pubblico con dominio
devi aprire la porta 80 del tuo router/modem oppure abiliti il DMZ (nelle impostazioni del modem) e inserisci l'ip locale. 
(Consiglio di impostare un IP locale statico per hostare un server!! Altrimenti dovrai continuamente cambiare le impostazioni del DMZ!!)
Una volta aperto il server nella rete locale e nella rete pubblica dovrai configurare un DNS, quindi trasformare il tuo ip pubblico (84.x.x.x)
in un nome (elektrowindowsKLBK.ddns.net). Per fare ció consiglio di utilizzare NOIP, una piattaforma che consente di creare DNS. Consiglio di installare
il DUC di NOIP nella macchina che hosterá il server!

Step 2 --- Offuscare

Una volta editato lo script e aver definito i parametri bisogna offuscarlo (per renderdere piú difficile la decompilazione del nostro script da terzi)
per offuscare vai su: https://pyobfuscate.com/rename-obf 
ed incolla il codice.

Step 3 --- Compilare 

NB!: PRIMA DI COMPILARE DEVI INSTALLARE LE LIBRERIE NECESSARIE PER LO SCRIPT!!

Adesso che hai creato un nuovo file con il codice offuscato lo devi compilare.
La sintassi del comando Pyinstaller é:

pyinstaller --onefile --noconsole "percorso_script.py" --icon

--onefile = compila in .exe 
--noconsole = non mostra il terminale quando esegui l'exec
--icon = applica l'icona (facoltativo)

Step 4 --- Fine!

Hai compilato lo script! Adesso per vedere i tasti premuti dalla vittima controlla l'access.log di apache, 
mentre se vuoi eseguire gli scrpt da remoto basta modificare il file "default.txt" ed entro 10 secondi verrano eseguiti ;)


Se hai dubbi su qualcosa scrivimi un commento nel video: https://youtu.be/WUCcFfZopac


Buon hacking!

AGGIORNAMENTO: Ho aggiunto il file "unin.bat", esso va a reinstallare Windows Defender e rimuovere tutti gli eseguibili che si trovano nella cartella di avvio di Windows, quindi rimuovere completamente KLBK dal PC (lo script deve essere eseguito su Windows PE se non si é amministratori nella macchina in uso.)
