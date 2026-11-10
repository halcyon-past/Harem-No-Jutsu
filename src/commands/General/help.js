const { SlashCommandBuilder } = require('discord.js');
const { buildHelpEmbed } = require('../../utils/embeds');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('help')
        .setDescription('Show the list of available commands'),
    aliases: ['commands'],

    async execute(interaction) {
        await interaction.reply({ embeds: [buildHelpEmbed()] });
    },

    async executePrefix(message) {
        await message.channel.send({ embeds: [buildHelpEmbed()] });
    },
};
