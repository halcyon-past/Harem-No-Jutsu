const {
    ActionRowBuilder,
    ButtonBuilder,
    ButtonStyle,
    EmbedBuilder,
} = require('discord.js');
const {
    ACTION_COMMANDS,
    BOT_INVITE_URL,
    CREATOR_INSTAGRAM_URL,
} = require('../data/gifs');

const HELP_BUTTON_ID = 'ohayo_help';

/** Build the help embed listing all migrated commands. */
function buildHelpEmbed() {
    const fields = [
        {
            name: "You need help don't you?",
            value:
                "Here's a list of commands to save your ass!!\nYou can use `/command` slash commands or `baka! <command>` in lowercase.",
        },
        {
            name: 'ohayo',
            value: 'Starts your journey with this bot',
        },
        {
            name: 'about',
            value: "It's basically a section about the mastermind behind this bot",
        },
        {
            name: 'ai',
            value: 'Chat with the bot powered by Gemini',
        },
        ...ACTION_COMMANDS.map((cmd) => ({
            name: cmd.name,
            value: cmd.description,
        })),
    ];

    return new EmbedBuilder()
        .setTitle('Ohayo!!')
        .setColor('Purple')
        .addFields(fields);
}

/** Build the Ohayo welcome embed and interactive help button row. */
function buildOhayoMessage(authorMention) {
    const embed = new EmbedBuilder()
        .setTitle('Ohayo!!')
        .setColor('Purple')
        .addFields(
            {
                name: 'Is it morning already?',
                value: `ohayo ${authorMention} san!!`,
            },
            {
                name: 'Wanna Add this cool bot to your own server?',
                value: BOT_INVITE_URL,
            }
        );

    const button = new ButtonBuilder()
        .setCustomId(HELP_BUTTON_ID)
        .setLabel('Click Me For Help!!')
        .setStyle(ButtonStyle.Success)
        .setEmoji('👻');

    const row = new ActionRowBuilder().addComponents(button);

    return { embeds: [embed], components: [row] };
}

/** Build the About embed and invite link button row. */
function buildAboutMessage() {
    const embed = new EmbedBuilder()
        .setTitle('Ohayo!!')
        .setColor('Green')
        .addFields(
            {
                name: 'What is this bot?',
                value:
                    'This bot is an inspiration from the senpai bot which used to have gif for funny situations to use in between conversations. Since it has been discontinued Aritro Saha programmed this bot for the same intention to make chats more fun!! Hope you will enjoy it here!!',
            },
            {
                name: 'Wanna support the creator?',
                value: `you don't have to do much just follow him in Instagram\n${CREATOR_INSTAGRAM_URL}\nto get started with the bot type \`\`\`baka! ohayo\`\`\` or use \`/ohayo\``,
            }
        );

    const button = new ButtonBuilder()
        .setLabel('Click Me To Invite')
        .setStyle(ButtonStyle.Link)
        .setURL(BOT_INVITE_URL)
        .setEmoji('🥵');

    const row = new ActionRowBuilder().addComponents(button);

    return { embeds: [embed], components: [row] };
}

module.exports = {
    HELP_BUTTON_ID,
    buildHelpEmbed,
    buildOhayoMessage,
    buildAboutMessage,
};
