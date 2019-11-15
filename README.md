# RescuWise
Someone needs to write an elevator pitch for this thing.

## Install and run project locally: 

1. Start by cloning the repo:

   `git clone https://github.com/AshleyMatula/RescuWise.git`

2. Switch to the newly created RescuWise directory:

   `cd RescuWise`  

3. Create a python virtual enviroment:

   `virtualenv myenv -p python3`  

4. Activate your virtual enviroment:

   `source myenv/bin/activate` (`source myenv/Scripts/activate` on windows)   

5. Install the required libraries:

   `pip install -r requirements.txt` 

6. Create `.env` file in the project root directory:

   Your variables will vary a bit depending on your setup but use this template to start. Make sure to enter the credentials for your local database.

   ```
   SECRET_KEY=ja391197!tv&r$qbptd10(ecx0visy&ur#*)se&+*j(+v9#fbp

   ### LOCAL DB CREDENTIALS
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=

   ### STAGING DB CREDENTIALS
   # DATABASE_NAME=d4gt9rgkd0pnkr
   # DATABASE_USER=zltonmtygmionp
   # DATABASE_PASSWORD=44c746d7b5554894f9a0efd082c124e5d52842d0d9dae477f2cc928d6f990dd7
   # DATABASE_HOST=ec2-174-129-18-42.compute-1.amazonaws.com
   # DATABASE_PORT=5432

   AWS_ACCESS_KEY_ID=AKIA6FGA7QKHKD54PF5I
   AWS_SECRET_ACCESS_KEY=6yZWbCFNrIuyokIDJo6j89990HYxfV8hp359Fcm6
   AWS_STORAGE_BUCKET_NAME=rescuewise-uploads
   ```

7. Migrate your local database:

   `python manage.py migrate`

8. You should be all set, run your server:

   `python manage.py runserver`
