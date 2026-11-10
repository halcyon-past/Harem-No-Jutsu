const { REST, Routes } = require('discord.js');
const fs = require('fs');
const nodePath = require('path');

module.exports = (client) => {
    /** Register a single command module into client.commands and client.aliases. */
    function registerCommand(command) {
        if (!command?.data?.name) return;
        const name = command.data.name.toLowerCase();
        client.commands.set(name, command);
        client.commandArray.push(command.data.toJSON());

        if (Array.isArray(command.aliases)) {
            for (const alias of command.aliases) {
                client.aliases.set(alias.toLowerCase(), name);
            }
        }
    }

    client.handleCommands = async (commandFolders, path) => {
        client.commandArray = [];

        for (const folder of commandFolders) {
            const folderPath = nodePath.join(path, folder);
            if (!fs.statSync(folderPath).isDirectory()) continue;

            const commandFiles = fs
                .readdirSync(folderPath)
                .filter((file) => file.endsWith('.js'));

            for (const file of commandFiles) {
                const exported = require(`../commands/${folder}/${file}`);
                const items = Array.isArray(exported) ? exported : [exported];
                for (const command of items) {
                    registerCommand(command);
                }
            }
        }

        const token = process.env.BOT_TOKEN || process.env.DISCORD_TOKEN;
        const clientId = process.env.BOT_ID;
        const guildId = process.env.GUILD_ID;

        if (!token || !clientId) {
            console.warn(
                'Skipping slash command registration: BOT_TOKEN (or DISCORD_TOKEN) and BOT_ID must be set.'
            );
            return;
        }

        const rest = new REST({ version: '10' }).setToken(token);

        try {
            console.log('Started refreshing application (/) commands.');

            const route = guildId
                ? Routes.applicationGuildCommands(clientId, guildId)
                : Routes.applicationCommands(clientId);

            await rest.put(route, { body: client.commandArray });

            console.log('Successfully reloaded application (/) commands.');
        } catch (error) {
            console.error('Failed to reload application (/) commands:', error);
        }
    };
};
