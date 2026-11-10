const { SlashCommandBuilder } = require('discord.js');
const { buildAboutMessage } = require('../../utils/embeds');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('about')
        .setDescription('This command tells you about the creator'),
    aliases: ['info'],

    async execute(interaction) {
        await interaction.reply(buildAboutMessage());
    },

    async executePrefix(message) {
        await message.channel.send(buildAboutMessage());
    },
};
