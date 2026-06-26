import dotenv from 'dotenv';
dotenv.config({ quiet: true });

const { CLIENT_ID, CLIENT_SECRET, REDIRECT_URI } = process.env;

if (!CLIENT_ID || !CLIENT_SECRET) {
    throw new Error('[!] Missing SoundCloud CLIENT_ID and CLIENT_SECRET.\nThey must be set in environment variables. (.env)');
}

export const config = {
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    redirectUri: REDIRECT_URI || 'http://localhost:8080/callback',
};