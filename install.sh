#!/bin/bash
clear
read numb
if [ $numb = "8260541" ]
then
    pkg install python -y
    pkg install dos2unix
	cp ~/spamMail/mailSPAM.py $PREFIX/bin/spamMail
	dos2unix $PREFIX/bin/spamMail
	chmod -R 777 ~/spamMail
	chmod 777 $PREFIX/bin/spamMail
	spamMail
fi
