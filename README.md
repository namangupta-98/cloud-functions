## GCP Cloud Functions
* They are part of FaaS (Function as a service).
* They let you automatically run backend code in response to events or Https requests.
* Your code is stored in Google Cloud and runs in a managed environment.
* You don't have to worry about managing or scaling your severs.

## Start a Project
* To start a project create a new project either on [Firebase Console](https://console.firebase.google.com/) or [GCP Console](https://console.cloud.google.com/)
* install gcloud sdk and set path
* gcloud init //(to initialize gcloud project)
* gcloud projects list //(lists all the projects in gcp)
* gcloud config set project project_id //(configure project)
* gcloud functions deploy hello_world --runtime python37 --trigger-http //(deploy function on gcp)

#### We have to create a .env.yaml to store environment variables and requirements.txt to store other dependencies in the same directory as main.py
* gcloud functions deploy send_mail --env-vars-file .env.yaml --runtime python38 --trigger-http //(deploy with some environment variables)

#### Schedule Cloud Functions
* gcloud components install beta //(to install beta components)
* gcloud components update //(to update the components)
* gcloud pubsub topics create cloud-functions-test
* gcloud pubsub subscriptions create cron-sub --topic cloud-functions-test
Create a cronjob at Cloud Scheduler in GCP.
