const { SlashCommandBuilder } = require('discord.js');
const { getAiResponse, splitMessage } = require('../../utils/gemini');

const WAIT_TIMEOUT_MS = 60_000;

/** Wait for a follow-up message from the invoking user in the same channel. */
async function waitForUserPrompt(channel, userId) {
    const collected = await channel.awaitMessages({
        filter: (msg) => msg.author.id === userId,
        max: 1,
        time: WAIT_TIMEOUT_MS,
        errors: ['time'],
    });
    return collected.first().content;
}

module.exports = {
    data: new SlashCommandBuilder()
        .setName('ai')
        .setDescription('Chat with the bot powered by Gemini')
        .addStringOption((option) =>
            option
                .setName('prompt')
                .setDescription('What would you like to chat about?')
                .setRequired(false)
        ),
    aliases: ['chat', 'aianime'],

    async execute(interaction) {
        let prompt = interaction.options.getString('prompt');

        if (!prompt) {
            await interaction.reply('Hi! What would you like to chat about?');
            try {
                prompt = await waitForUserPrompt(
                    interaction.channel,
                    interaction.user.id
                );
            } catch {
                await interaction.followUp(
                    "You took too long to respond! Try again when you're ready."
                );
                return;
            }

            try {
                const { text } = await getAiResponse(prompt);
                const chunks = splitMessage(text);
                for (const chunk of chunks) {
                    await interaction.followUp(chunk);
                }
            } catch (error) {
                console.error('AI response error:', error);
                await interaction.followUp(
                    "Sorry, I couldn't generate a response right now."
                );
            }
            return;
        }

        await interaction.deferReply();
        try {
            const { text } = await getAiResponse(prompt);
            const chunks = splitMessage(text);
            await interaction.editReply(chunks[0]);
            for (let i = 1; i < chunks.length; i += 1) {
                await interaction.followUp(chunks[i]);
            }
        } catch (error) {
            console.error('AI response error:', error);
            await interaction.editReply(
                "Sorry, I couldn't generate a response right now."
            );
        }
    },

    async executePrefix(message, args) {
        let prompt = args.join(' ').trim();

        if (!prompt) {
            await message.channel.send('Hi! What would you like to chat about?');
            try {
                prompt = await waitForUserPrompt(
                    message.channel,
                    message.author.id
                );
            } catch {
                await message.channel.send(
                    "You took too long to respond! Try again when you're ready."
                );
                return;
            }
        }

        try {
            const { text } = await getAiResponse(prompt);
            const chunks = splitMessage(text);
            for (const chunk of chunks) {
                await message.channel.send(chunk);
            }
        } catch (error) {
            console.error('AI response error:', error);
            await message.channel.send(
                "Sorry, I couldn't generate a response right now."
            );
        }
    },
};
