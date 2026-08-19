# Final Setup

## 1. Personal context
Fill:
- context/dream-life.md
- context/yearly-goals.md
- context/voice-tone.md

## 2. Google AI
Create a Gemini API key and add it to GitHub:
Settings → Secrets and variables → Actions → New repository secret
- Name: GOOGLE_API_KEY
- Value: your Gemini API key

Optional repository variables:
- GEMINI_TEXT_MODEL = gemini-2.5-flash
- GEMINI_TTS_MODEL = gemini-2.5-flash-preview-tts
- GEMINI_TTS_VOICE = Kore

## 3. Gmail OAuth
The Gmail API requires authorized user credentials for sending mail. Create a Google Cloud project, enable Gmail API, create OAuth client credentials, authorize the account, and obtain a user token with:
https://www.googleapis.com/auth/gmail.send

Store the resulting authorized-user token JSON as:
- GitHub Secret: GMAIL_TOKEN_JSON

Store the destination email as:
- GitHub Secret: MEDITATION_EMAIL

## 4. GitHub
Push the repository and manually run:
Actions → Daily Meditation Agent → Run workflow

Then verify:
- Gemini generates the script.
- `scripts/YYYY-MM-DD.md` is committed.
- TTS creates audio.
- Gmail receives the meditation.

## 5. Apple Shortcut
After the first successful email:
1. Create a Personal Automation for receiving an email.
2. Filter by your meditation sender/subject.
3. Extract the audio attachment.
4. Save it to Files/iCloud Drive.
5. Show a notification: “Your meditation is ready 🎧”.
6. Play the audio.
7. Optionally delete the file after playback.

Important: test this manually with one email before enabling automatic execution.

## 6. Failure alerts
The workflow has a failure hook, but a production failure email sender still needs to be configured. The simplest route is to add an SMTP/API email provider or use a separate existing email automation.

## 7. Storage
The workflow intentionally does not commit audio files to GitHub. Audio is transient and is delivered by email. The generated scripts are retained in `scripts/`.
