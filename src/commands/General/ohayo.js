const { SlashCommandBuilder } = require('discord.js');
const { buildOhayoMessage } = require('../../utils/embeds');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ohayo')
        .setDescription('This command starts your journey with this bot'),
    aliases: ['start', 'begin'],

    async execute(interaction) {
        const payload = buildOhayoMessage(`<@${interaction.user.id}>`);
        await interaction.reply(payload);
    },

    async executePrefix(message) {
        const payload = buildOhayoMessage(`<@${message.author.id}>`);
        await message.channel.send(payload);
    },
};
