const { ActivityType } = require('discord.js');

module.exports = {
    name: 'ready',
    once: true,
    async execute(client) {
        console.log(`${client.user.tag} is now online!`);
        console.log('Enabling status...');

        const updateStatus = () => {
            const servers = client.guilds.cache.size;
            const users = client.guilds.cache.reduce(
                (total, guild) => total + (guild.memberCount || 0),
                0
            );

            const statuses = [
                {
                    name: 'Type baka! ohayo or /ohayo 👻',
                    type: ActivityType.Playing,
                },
                {
                    name: `${servers} servers`,
                    type: ActivityType.Watching,
                },
                {
                    name: `${users} users`,
                    type: ActivityType.Listening,
                },
            ];

            const selected = statuses[Math.floor(Math.random() * statuses.length)];
            client.user.setActivity(selected);
        };

        updateStatus();
        setInterval(updateStatus, 10000);

        console.log('Successfully enabled status!');
    },
};
