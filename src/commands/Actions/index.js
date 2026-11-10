const { ACTION_COMMANDS } = require('../../data/gifs');
const { createActionCommand } = require('../../utils/actionCommand');

module.exports = ACTION_COMMANDS.map(createActionCommand);
