const { EmbedBuilder, SlashCommandBuilder } = require('discord.js');
const { NAMES } = require('../data/gifs');

const MENTION_REGEX = /^<@!?\d{14,}>$/;

/** Pick a random element from a non-empty array. */
function pickRandom(items) {
    return items[Math.floor(Math.random() * items.length)];
}

/** Format an action template with author, target, and random name placeholders. */
function formatTemplate(template, { author, target = '', name = '' }) {
    return template
        .replaceAll('{author}', author)
        .replaceAll('{target}', target)
        .replaceAll('{name}', name);
}

/**
 * Build an EmbedBuilder for an action GIF command.
 * @param {object} config Action command definition from src/data/gifs.js.
 * @param {string} authorMention Mention string for the invoking user.
 * @param {string|null} targetMention Mention string if a Discord user was targeted.
 * @param {boolean} hasTextArg Whether non-mention text arguments were provided.
 */
function buildActionEmbed(config, authorMention, targetMention, hasTextArg = false) {
    const randomName = pickRandom(NAMES);
    let fieldName = config.fieldTitle;
    let fieldValue;
    let imageUrl;

    if (targetMention) {
        fieldValue = formatTemplate(config.withUserTemplate, {
            author: authorMention,
            target: targetMention,
        });
        imageUrl = pickRandom(config.gifs);
    } else if (hasTextArg) {
        fieldName = config.selfFieldTitle || config.fieldTitle;
        fieldValue = formatTemplate(config.withTextArgTemplate, {
            author: authorMention,
            name: randomName,
        });
        imageUrl = config.soloGif || pickRandom(config.gifs);
    } else {
        fieldName = config.selfFieldTitle || config.fieldTitle;
        fieldValue = formatTemplate(config.soloTemplate, {
            author: authorMention,
            name: randomName,
        });
        if (config.soloGif) {
            imageUrl = config.soloGif;
        } else if (config.soloGifs) {
            imageUrl = pickRandom(config.soloGifs);
        } else {
            imageUrl = pickRandom(config.gifs);
        }
    }

    return new EmbedBuilder()
        .setTitle(config.title)
        .setColor('Purple')
        .addFields({ name: fieldName, value: fieldValue })
        .setImage(imageUrl);
}

/** Create a unified slash + prefix command module from an action config. */
function createActionCommand(config) {
    const data = new SlashCommandBuilder()
        .setName(config.name)
        .setDescription(config.description)
        .addUserOption((option) =>
            option
                .setName('user')
                .setDescription(`User to ${config.name}`)
                .setRequired(false)
        );

    return {
        data,
        aliases: config.aliases || [],
        async execute(interaction) {
            const targetUser = interaction.options.getUser('user');
            const targetMention = targetUser ? `<@${targetUser.id}>` : null;
            const embed = buildActionEmbed(
                config,
                `<@${interaction.user.id}>`,
                targetMention,
                false
            );
            await interaction.reply({ embeds: [embed] });
        },
        async executePrefix(message, args) {
            const firstArg = args[0] || '';
            const mentionedUser = message.mentions.users.first();
            const targetMention = mentionedUser
                ? `<@${mentionedUser.id}>`
                : MENTION_REGEX.test(firstArg)
                  ? firstArg
                  : null;
            const hasTextArg = !targetMention && args.length > 0;
            const embed = buildActionEmbed(
                config,
                `<@${message.author.id}>`,
                targetMention,
                hasTextArg
            );
            await message.channel.send({ embeds: [embed] });
        },
    };
}

module.exports = {
    pickRandom,
    buildActionEmbed,
    createActionCommand,
};
