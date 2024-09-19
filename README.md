This project is a virtual administrative assistant that automates key office tasks using AI. It includes a PDF generator that formats and creates professional documents, and an email generator powered by Llama 3 on GroqCloud, which drafts emails based on user input. Both features streamline administrative workflows, improving efficiency.

1. Create API Key from GroqCloud
Sign in to GroqCloud: Go to the GroqCloud website and sign in to your account.
Create an API Key:
Navigate to your account settings or API section.
Look for an option like API Keys.
Click on Create New API Key.
Copy the API key when it is generated and save it securely as it will be used for authentication in your application.
2. Create a Secret Key for Google Vision API
Set Up Google Cloud Project:

Go to the Google Cloud Console.
Sign in with your Google account.
Create a new project by clicking the Select Project dropdown at the top, then click New Project.
Give the project a name and click Create.
Enable Google Vision API:

After creating the project, navigate to the API & Services section.
In the Library tab, search for Vision API.
Click on Google Cloud Vision API and then click Enable.
Create API Key:

In the API & Services section, click on Credentials.
Click Create Credentials and select API Key.
Once the API key is generated, copy it and store it securely.
You can optionally restrict the API key to specific IP addresses or services to enhance security.
Create a Service Account and Secret Key (Optional but Recommended):

In the Credentials tab, click Create Credentials and select Service Account.
Fill in the required details and click Create.
Under Key Type, select JSON and click Create. A JSON file containing your private key will be downloaded. This file will be used to authenticate your application with Google Cloud.
