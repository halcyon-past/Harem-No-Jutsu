const { Client, GatewayIntentBits, Collection } = require('discord.js');
const fs = require('fs');
require('dotenv').config();

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

client.commands = new Collection();
client.aliases = new Collection();

const functions = fs
    .readdirSync('./src/functions')
    .filter((file) => file.endsWith('.js'));
const eventFiles = fs
    .readdirSync('./src/events')
    .filter((file) => file.endsWith('.js'));
const commandFolders = fs.readdirSync('./src/commands');

// Error handling
process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

process.on('uncaughtException', (err) => {
    console.error('Uncaught Exception:', err);
});

process.on('uncaughtExceptionMonitor', (err, origin) => {
    console.error('Uncaught Exception Monitor:', err, origin);
});

// Directory handling and login
(async () => {
    for (const file of functions) {
        require(`./functions/${file}`)(client);
    }
    client.handleEvents(eventFiles, './src/events');
    await client.handleCommands(commandFolders, './src/commands');

    const token = process.env.BOT_TOKEN || process.env.DISCORD_TOKEN;
    if (!token) {
        console.error('Missing BOT_TOKEN (or DISCORD_TOKEN) in environment.');
        process.exit(1);
    }
    await client.login(token);
})();
