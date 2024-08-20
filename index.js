const { GoogleGenerativeAI } = require('@google/generative-ai');
const fs = require('fs').promises;
const axios = require('axios');
const express = require('express');
const bodyParser = require('body-parser');

async function getApiKey() {
  try {
    const data = await fs.readFile('API.txt', 'utf8');
    const apiKey = data.match(/API_KEY="(.+?)"/)[1];
    return apiKey;
  } catch (error) {
    console.error('Error reading API key:', error);
    process.exit(1);
  }
}

(async () => {
  const gemini_api_key = await getApiKey();
  const googleAI = new GoogleGenerativeAI(gemini_api_key);
  const geminiConfig = {
    temperature: 0.4,
    topP: 1,
    topK: 32,
    maxOutputTokens: 4096,
  };

  const geminiModel = googleAI.getGenerativeModel({
    model: 'gemini-1.5-flash',
    geminiConfig,
  });

  const app = express();
  app.use(bodyParser.json());

  app.post('/generate', async (req, res) => {
    try {
      const { url } = req.body;
      if (!url) {
        return res.status(400).send({ error: 'URL is required' });
      }

      // Get image from URL
      const imageResponse = await axios.get(url, { responseType: 'arraybuffer' });
      const imageBase64 = Buffer.from(imageResponse.data, 'binary').toString('base64');

      const promptConfig = [
        { text: 'find the quizz on this image and answer it. response only answer' },
        {
          inlineData: {
            mimeType: 'image/jpeg',
            data: imageBase64,
          },
        },
      ];

      const result = await geminiModel.generateContent({
        contents: [{ role: 'user', parts: promptConfig }],
      });
      const textResponse = await result.response;
      res.send({ response: textResponse.text() });
      console.log('response', textResponse.text());
    } catch (error) {
      console.log(' response error', error);
      res.status(500).send({ error: 'An error occurred' });
    }
  });

  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
})();