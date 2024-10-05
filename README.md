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

## Remaining To-Do

### 6. Add Commands

- Add basic text commands like ohayo, about, etc.
- Example:

```javascript
client.on('messageCreate', async (message) => {
  if (message.content.toLowerCase().startsWith('baka! ohayo')) {
    message.channel.send(\`Ohayo \${message.author}!\`);
  }
});
```

### 7. Create Embeds and Buttons

- Create embed messages: Use MessageEmbed to create rich embeds with colors and titles.
- Add interactive buttons: Use ActionRowBuilder and ButtonBuilder to allow users to interact with the bot.

### 8. Sending Gifs

- Send random gifs based on commands: Load gifs from an array and randomly select one to send.

Example:

```javascript
const kills = ['https://example.com/gif1.gif', 'https://example.com/gif2.gif'];

client.on('messageCreate', (message) => {
  if (message.content.startsWith('baka! kill')) {
    const gif = kills[Math.floor(Math.random() * kills.length)];
    message.channel.send({ content: \`\${message.author} killed someone!\`, files: [gif] });
  }
});
```

### 9. Add Slash Commands

- Implement slash commands for better user experience. Use Discord’s slash command framework to register and handle commands.

Example:

```javascript
client.on('ready', async () => {
  const guild = client.guilds.cache.get('GUILD_ID');
  await guild.commands.create({
    name: 'ohayo',
    description: 'Says ohayo!',
  });
});

client.on('interactionCreate', async (interaction) => {
  if (!interaction.isCommand()) return;

  if (interaction.commandName === 'ohayo') {
    await interaction.reply(\`Ohayo \${interaction.user.username}!\`);
  }
});
```

### 10. AI Implementation

- Implement an AI API of your choice for example: `Groq.com`, `OpenAI`, `Gemini`, etc

### 11. Test the Bot

- Test locally: Use node index.js to start the bot and test various commands in your Discord server.

### 12. Error Handling

- Add proper error handling: Ensure all commands handle errors gracefully, and log any issues that occur during bot interactions.

### 13. Deployment

- Deploy to a cloud service: Consider using platforms like Heroku, AWS, or DigitalOcean to host your bot permanently.
- Setup automatic restart: Use tools like pm2 to keep the bot running and automatically restart it in case of crashes.