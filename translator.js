const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 8000;

app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');
app.use(express.static('public'));

const rapidAPIHeaders = {
  'Accept-Encoding': 'application/gzip',
  'X-RapidAPI-Key': '5db2eed680msh037897a7ec42cf3p1932bcjsnc5ad9ae870d0', // replace with your Key
  'X-RapidAPI-Host': 'cilenisapi.p.rapidapi.com'
};

const rapidAPIBaseUrl = 'https://cilenisapi.p.rapidapi.com/language_identifier';

let translatedLanguage;

app.get('/', async (req, res) => {
  try {
    const lg = await getSupportedLanguages();
    res.render('index', { lg, translatedLanguage });
  } catch (error) {
    console.error(error);
    res.status(500).send('An error occurred');
  }
});

app.post('/translate', async (req, res) => {
  const { lang1, lang2, lg1 } = req.body;
  try {
    const translation = await translateText(lg1, lang1.trim(), lang2.trim());
    translatedLanguage = translation.data.translations[0].translatedText;
    res.redirect('/');
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'An error occurred' });
  }
});

async function getSupportedLanguages() {
  const response = await axios.get(`${rapidAPIBaseUrl}/language/translate/v2/languages`, {
    headers: rapidAPIHeaders
  });
  return response.data.data.languages;
}

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
