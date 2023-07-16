# PET monitoring script :gear:
## Requirements :arrow_down:
 - Get your credentials in **Google Cloud Console** and put it in root directory.
   - Normally the credentials file has another name, so you have to rename file as *credentials.json*.
   - Before download your credentials, activate **Drive**, **Classroom** and **Sheets** Api's in your project. 
 - You must have **docker** and **docker-compose** latests versions installed in your machine.
 - You must create an empty spreadsheet in Google Drive and get its ID.

## Usage :computer:
 - To use script just type the command below and follow instructions in your terminal:
```bash
make
```
 - Docker images will be pulled for your machine and dependencies will be installed. 
 - Two links will appear into your terminal. So you have to click them and accept all authentications. These authentications will let the script run in your google drive.

## Removing :wastebasket:
 - After use script, type command below:
```bash
make clean
```
 - It will turn off the application and remove some containers.
 - Maybe there's a container and an image left in your docker. You can delete them manually.
