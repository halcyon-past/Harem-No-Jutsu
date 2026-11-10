const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('ping')
    .setDescription(`Check the bot's latency`),

    async execute(interaction, client) {
        await interaction.reply({ content: `Pong!\n\`(took ${client.ws.ping}ms)\`` });
    },

    async executePrefix(message, _args, client) {
        await message.channel.send({ content: `Pong!\n\`(took ${client.ws.ping}ms)\`` });
    },
};