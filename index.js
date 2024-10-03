require('dotenv').config();
const { Client, GatewayIntentBits, ActivityType } = require('discord.js');

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent, GatewayIntentBits.DirectMessages],
});

const statuses = ['with halcyon-past', 'with YockerFX', 'with ContributerXY'];

function updateStatus() {
    const status = statuses[Math.floor(Math.random() * statuses.length)];
    client.user.setPresence({
        activities: [{ name: status, type: ActivityType.Streaming, url: 'https://twitch.tv/yockerfx' }],
        status: 'online',
    });
}

setInterval(updateStatus, 10000);

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
    updateStatus();
});

client.login(process.env.BOT_TOKEN);
