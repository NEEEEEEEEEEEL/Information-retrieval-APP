# Project Setup

## Clone the Repository
```bash
git clone <repo_url>
cd <repo_name>
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Get Google API Key for Gemini

1. **Go to Google AI Studio:**  
   - Visit [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account.
   
2. **Generate API Key:**  
   - Click on **"API Keys"** in the sidebar.
   - Click **"Create API Key"** and copy the key.
   
3. **Enable Gemini API (If Required):**  
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).  
   - Search for **Gemini API** and enable it.

## Set Up the `.env` File

1. Create a `.env` file in the root directory.
2. Open the file and add the following:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```
3. Save and close the file.

## Run the Streamlit App
```bash
streamlit run app.py
```

Now, open your browser and go to **http://localhost:8501** to access the app.
