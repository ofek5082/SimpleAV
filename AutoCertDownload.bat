@echo off 
setlocal

:: Cert URLs
set url1="https://www.eicar.org/download/eicar.com"
set url2="https://www.avast.com/eicar-test-file"
set url3="https://media.kaspersky.com/virus-advisories/EICAR.com"
set url4="https://download.bitdefender.com/testfile/eicar.com"
set url5="https://files.trendmicro.com/solutions/eicar.com"

:: Use curl -o to download/update certifications
curl -o cert1.txt %url1%
curl -o cert2.txt %url2%
curl -o cert3.txt %url3%
curl -o cert4.txt %url4%
curl -o cert5.txt %url5%

:: Print a messege to indicate download complete 
echo Download complete.

:: Pause the script so the windows wont close automatically 
pause
