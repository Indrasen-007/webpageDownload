download.py
This project will open the webpage and save the webpage as pdf.
I am using Selium to automate it, and it maintain the same session, I am opening the crome in debug mode
Ref : https://www.youtube.com/watch?v=Zrx8FSEo9lk
```
C:\Program Files\Google\Chrome\Application>chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\\Users\\insin\\Desktop\\Python\\chromeData"
```
The program reads the url info from input.json
Iterate over each file, opens the browser and save the webpage as pdf.
I have already logged into the educative website
Navigate to download folder and run the program