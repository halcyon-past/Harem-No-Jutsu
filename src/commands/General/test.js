const { SlashCommandBuilder } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('test')
    .setDescription('Check if the bot is working'),

    async execute (interaction) {
        await interaction.reply({content: 'The bot is online and working!'});
    }
}