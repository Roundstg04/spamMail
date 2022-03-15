#!/bin/bash
clear
read numb
if [ $numb = "8260541" ]
then
    pkg install python -y
    pkg install dos2unix
	cp ~/spamMail/mailSPAM.py $PREFIX/bin/mail
	dos2unix $PREFIX/bin/mail
	chmod -R 777 ~/mail
	chmod 777 $PREFIX/bin/mail
	mail
fi
