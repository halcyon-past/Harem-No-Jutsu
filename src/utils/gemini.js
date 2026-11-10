const { GoogleGenAI } = require('@google/genai');

const DEFAULT_MODEL = 'gemini-3.8-flash';
const SYSTEM_INSTRUCTION =
    'You are a friendly, playful anime-themed Discord bot assistant. Keep responses concise and under 2000 characters when possible.';

let client = null;

/** Return a lazily initialized GoogleGenAI client. */
function getClient() {
    if (!client) {
        const apiKey = process.env.GEMINI_API_KEY || process.env.API_KEY;
        if (!apiKey) {
            throw new Error(
                'Missing Gemini API key: set GEMINI_API_KEY or API_KEY in the environment.'
            );
        }
        client = new GoogleGenAI({ apiKey });
    }
    return client;
}

/**
 * Generate a response for a user prompt via the Gemini Interactions API.
 * @param {string} userInput
 * @param {string} [previousInteractionId]
 * @returns {Promise<{ text: string, interactionId: string | undefined }>}
 */
async function getAiResponse(userInput, previousInteractionId) {
    if (!userInput || !userInput.trim()) {
        return {
            text: "Well, you're awfully silent...",
            interactionId: previousInteractionId,
        };
    }

    const ai = getClient();
    const params = {
        model: DEFAULT_MODEL,
        input: userInput,
        system_instruction: SYSTEM_INSTRUCTION,
    };
    if (previousInteractionId) {
        params.previous_interaction_id = previousInteractionId;
    }

    const interaction = await ai.interactions.create(params);
    const text = (interaction.output_text || '').trim();

    return {
        text: text || 'I have no idea what you are talking about',
        interactionId: interaction.id,
    };
}

/** Split text into chunks that fit within Discord's 2000-character limit. */
function splitMessage(text, maxLength = 2000) {
    if (!text) return [''];
    const chunks = [];
    for (let i = 0; i < text.length; i += maxLength) {
        chunks.push(text.slice(i, i + maxLength));
    }
    return chunks;
}

module.exports = {
    DEFAULT_MODEL,
    getAiResponse,
    splitMessage,
};
