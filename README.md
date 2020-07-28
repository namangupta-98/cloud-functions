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