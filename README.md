# Harem-No-Jutsu

Looking for contributions to make this Discord bot better as part of Hacktober Fest.

## How to contribute

1. Fork the repository
2. Clone the repository
3. Create a new branch
4. Make your changes
5. Commit your changes
6. Push your changes
7. Create a pull request

# Discord Bot Migration to discord.js

This project aims to migrate a Discord bot from `discord.py` to `discord.js`.

## Project Setup

### 1. Install Node.js and NPM
- [x] **Node.js installed**: [Download Node.js](https://nodejs.org/) and install the latest LTS version.
- [x] **NPM initialized**: NPM should come installed with Node.js.

### 2. Create a new Project
- [x] **Project directory created**: Run the following commands:
  
```bash
mkdir discord-bot
cd discord-bot
```
- [x] **package.json initialized**:

```bash
npm init -y
```

### 3. Install discord.js

- [x] **Installed discord.js**:

```bash
npm install discord.js
```

### 4. Bot Setup

- [x] **Bot created in Discord Developer Portal**: The bot has been registered and its token is obtained from Discord Developer Portal.
- [x] **Environment variable set up**: Created .env file with the bot token.

.env file format:
```bash
DISCORD_TOKEN=your-bot-token-here
```
Also installed dotenv to load environment variables:
```bash
npm install dotenv
```

### 5. Create a basic bot structure

- [x] **Bot structure created**: The basic bot is now up and running. Below is the initial bot code:

index.js:
```javascript
require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

client.once('ready', () => {
  console.log(\`Logged in as \${client.user.tag}\`);
});

client.login(process.env.DISCORD_TOKEN);
```

## Implemented Features & Migration Status

### 6. Text (`baka!`) & Slash (`/`) Commands
- [x] **General commands**: `ohayo` (`start`, `begin`), `about` (`info`), `help`, `ping`, `test`
- [x] **Action GIF commands**: `kill`, `dance`, `kiss`, `hug`, `tickle`, `pat`, `bonk`, `cuddle`, `smirk`, `stare`, `punch`, `kick`, `slap`, `cry`, `blush` (supported via both `/command` and `baka! <command>`)

### 7. Embeds and Buttons
- [x] Rich embeds with `EmbedBuilder`
- [x] Interactive help button on `ohayo` and invite link button on `about` via `ActionRowBuilder` and `ButtonBuilder`

### 8. Sending Gifs
- [x] Random GIF selection configured in `src/data/gifs.js` and handled via `src/utils/actionCommand.js`

### 9. Slash Commands
- [x] Registered via `src/functions/handleCommands.js` and handled in `src/events/interactionCreate.js`

### 10. AI Implementation
- [x] **JavaScript (`src/utils/gemini.js`, `/ai` & `baka! ai`)**: Powered by `@google/genai` Interactions API using `gemini-3.8-flash`
- [x] **Python (`python/response.py`)**: Migrated from deprecated `google-generativeai` (`gemini-1.5-flash`) to `google-genai` Interactions API (`gemini-3.8-flash`)

### 11. Test the Bot
- Run unit tests: `npm test`
- Run the bot locally: `npm start` (set `BOT_TOKEN`, `BOT_ID`, `GUILD_ID` [optional], and `API_KEY` or `GEMINI_API_KEY` in `.env`)

### 12. Error Handling
- [x] Interaction, prefix command, and process-level error handling

### 13. Deployment
- Deploy to a cloud service: Consider using platforms like Heroku, AWS, or DigitalOcean to host your bot permanently.
- Setup automatic restart: Use tools like `pm2` to keep the bot running and automatically restart it in case of crashes.