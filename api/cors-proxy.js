// /api/cors-proxy.js
const fetch = require('node-fetch');

module.exports = async (req, res) => {
    // Parse the URL to fetch from the query parameters
    const { url } = req.query;
    if (!url) {
        return res.status(400).send('URL parameter is required');
    }

    try {
        const response = await fetch(url);
        const data = await response.text();
        
        // Set CORS headers
        res.setHeader('Access-Control-Allow-Origin', '*');
        res.setHeader('Content-Type', response.headers.get('content-type'));
        
        // Return the content from the fetched URL
        res.status(200).send(data);
    } catch (error) {
        res.status(500).send('Failed to fetch the URL');
    }
};

