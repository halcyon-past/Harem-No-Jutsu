const PREFIX = 'baka!';

/** Parse a `baka!` prefix message into { commandName, args } or null. */
function parsePrefixMessage(content) {
    if (!content) return null;
    const trimmed = content.trim();
    if (!trimmed.toLowerCase().startsWith(PREFIX)) return null;

    const rest = trimmed.slice(PREFIX.length).trim();
    if (!rest) return null;

    const parts = rest.split(/\s+/);
    const commandName = parts[0].toLowerCase();
    const args = parts.slice(1);
    return { commandName, args };
}

module.exports = {
    name: 'messageCreate',
    parsePrefixMessage,
    async execute(message, client) {
        if (message.author.bot) return;

        const parsed = parsePrefixMessage(message.content);
        if (!parsed) return;

        const canonicalName =
            client.aliases.get(parsed.commandName) || parsed.commandName;
        const command = client.commands.get(canonicalName);
        if (!command || typeof command.executePrefix !== 'function') return;

        try {
            await command.executePrefix(message, parsed.args, client);
        } catch (error) {
            console.error(`Error executing prefix command ${canonicalName}:`, error);
            try {
                await message.channel.send(
                    'An error occurred while trying to execute this command!'
                );
            } catch (replyError) {
                console.error('Failed to send prefix error reply:', replyError);
            }
        }
    },
};
