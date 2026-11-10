const { HELP_BUTTON_ID, buildHelpEmbed } = require('../utils/embeds');

module.exports = {
    name: 'interactionCreate',
    async execute(interaction, client) {
        if (interaction.isButton()) {
            if (interaction.customId === HELP_BUTTON_ID) {
                await interaction.reply({ embeds: [buildHelpEmbed()] });
            }
            return;
        }

        if (!interaction.isChatInputCommand()) return;

        const command = client.commands.get(interaction.commandName);
        if (!command) return;

        try {
            await command.execute(interaction, client);
        } catch (error) {
            console.error(error);

            const errorPayload = {
                content: 'An error occurred while trying to execute this command!',
                ephemeral: true,
            };

            try {
                if (interaction.deferred || interaction.replied) {
                    await interaction.followUp(errorPayload);
                } else {
                    await interaction.reply(errorPayload);
                }
            } catch (replyError) {
                console.error('Failed to send interaction error reply:', replyError);
            }
        }
    },
};
