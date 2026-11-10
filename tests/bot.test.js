const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const { Collection } = require('discord.js');

const { ACTION_COMMANDS, GIFS } = require('../src/data/gifs');
const { buildActionEmbed } = require('../src/utils/actionCommand');
const {
    HELP_BUTTON_ID,
    buildHelpEmbed,
    buildOhayoMessage,
    buildAboutMessage,
} = require('../src/utils/embeds');
const { splitMessage } = require('../src/utils/gemini');
const { parsePrefixMessage } = require('../src/events/messageCreate');

test('all GIF URLs are non-empty strings', () => {
    for (const [category, urls] of Object.entries(GIFS)) {
        assert.ok(urls.length > 0, `${category} should not be empty`);
        for (const url of urls) {
            assert.equal(typeof url, 'string');
            assert.ok(url.startsWith('http'), `Invalid URL in ${category}: ${url}`);
        }
    }
});

test('handleCommands loads all slash commands and aliases cleanly', async () => {
    const client = {
        commands: new Collection(),
        aliases: new Collection(),
    };
    require('../src/functions/handleCommands')(client);

    const savedToken = process.env.BOT_TOKEN;
    const savedDiscordToken = process.env.DISCORD_TOKEN;
    const savedBotId = process.env.BOT_ID;
    delete process.env.BOT_TOKEN;
    delete process.env.DISCORD_TOKEN;
    delete process.env.BOT_ID;

    try {
        const commandFolders = fs.readdirSync('./src/commands');
        await client.handleCommands(commandFolders, './src/commands');
    } finally {
        if (savedToken !== undefined) process.env.BOT_TOKEN = savedToken;
        if (savedDiscordToken !== undefined) process.env.DISCORD_TOKEN = savedDiscordToken;
        if (savedBotId !== undefined) process.env.BOT_ID = savedBotId;
    }

    const expectedCommands = [
        'ping',
        'test',
        'ohayo',
        'about',
        'help',
        'ai',
        ...ACTION_COMMANDS.map((c) => c.name),
    ];

    for (const name of expectedCommands) {
        assert.ok(client.commands.has(name), `Missing command: ${name}`);
    }

    assert.equal(client.commandArray.length, expectedCommands.length);
    for (const payload of client.commandArray) {
        assert.match(payload.name, /^[a-z0-9_-]{1,32}$/);
        assert.ok(
            payload.description.length >= 1 && payload.description.length <= 100,
            `Description out of bounds for ${payload.name}: ${payload.description.length}`
        );
    }

    assert.equal(client.aliases.get('murder'), 'kill');
    assert.equal(client.aliases.get('chat'), 'ai');
    assert.equal(client.aliases.get('start'), 'ohayo');
    assert.equal(client.aliases.get('info'), 'about');
});

test('buildActionEmbed handles kill and dance edge cases', () => {
    const killConfig = ACTION_COMMANDS.find((c) => c.name === 'kill');
    const soloKill = buildActionEmbed(killConfig, '<@1>', null, false).toJSON();
    assert.equal(
        soloKill.image.url,
        'https://c.tenor.com/0w3AFTfAiaoAAAAC/sukuna-itadori.gif'
    );

    const targetedKill = buildActionEmbed(killConfig, '<@1>', '<@2>', false).toJSON();
    assert.ok(targetedKill.fields[0].value.includes('<@2>'));
    assert.ok(GIFS.kills.includes(targetedKill.image.url));

    const danceConfig = ACTION_COMMANDS.find((c) => c.name === 'dance');
    const soloDance = buildActionEmbed(danceConfig, '<@1>', null, false).toJSON();
    assert.ok(GIFS.danceSolo.includes(soloDance.image.url));

    const textDance = buildActionEmbed(danceConfig, '<@1>', null, true).toJSON();
    assert.ok(GIFS.dancePartner.includes(textDance.image.url));
});

test('ohayo, about, and help embeds build expected components', () => {
    const ohayo = buildOhayoMessage('<@123>');
    assert.equal(ohayo.embeds.length, 1);
    assert.equal(ohayo.components[0].components[0].data.custom_id, HELP_BUTTON_ID);

    const about = buildAboutMessage();
    assert.equal(about.embeds.length, 1);
    assert.ok(about.components[0].components[0].data.url);

    const help = buildHelpEmbed().toJSON();
    assert.ok(help.fields.length >= 18);
});

test('parsePrefixMessage handles case and spacing variations', () => {
    assert.deepEqual(parsePrefixMessage('baka! ohayo'), {
        commandName: 'ohayo',
        args: [],
    });
    assert.deepEqual(parsePrefixMessage('BAKA!kill <@12345678901234>'), {
        commandName: 'kill',
        args: ['<@12345678901234>'],
    });
    assert.deepEqual(parsePrefixMessage('Baka! ai tell me a joke'), {
        commandName: 'ai',
        args: ['tell', 'me', 'a', 'joke'],
    });
    assert.equal(parsePrefixMessage('hello world'), null);
    assert.equal(parsePrefixMessage('baka!'), null);
});

test('splitMessage splits long text into <=2000 character chunks', () => {
    const longText = 'a'.repeat(4500);
    const chunks = splitMessage(longText);
    assert.equal(chunks.length, 3);
    assert.equal(chunks[0].length, 2000);
    assert.equal(chunks[1].length, 2000);
    assert.equal(chunks[2].length, 500);
});
