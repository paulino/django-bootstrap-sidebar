#!/usr/bin/env node

/**
 * GoogleFonts Downloader for Self-Hosted Websites
 *
 * This script downloads selected fonts and updates the URLs in the received CSS
 * to refer to local files. It generates a file named "fonts.css" that refers to
 * the "fonts" directory where the files are downloaded.
 *
 * Example:
 *
 * node gfontsdw.js 'https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,700;1,300;1,700&display=swap'
 */

const fs = require('fs');
const https = require('https');
const path = require('path');

const VERSION = "1";

// Settings: the following options are not implemented as command line args
const FORMAT = "woff2"; // Valid values: "woff", "ttf"

const HEADERS = {
    "woff2": {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    },
    "woff": {
        "User-Agent": "AppleWebKit/537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    },
    "ttf": {}
};

// Check command line
if (process.argv.length < 3) {
    console.error(`Google Fonts Downloader version ${VERSION}.\n`);
    console.error(`Usage: node gfontsdw.js <css_url> output-directory\n`);
    process.exit(255);
}

const outputDir = process.argv[3] || ".";
const cssUrl = process.argv[2];
const regUrl = /src:.*url\(([^)]*)/g;

// Fonts output directory
if (!fs.existsSync(path.join(outputDir,"/fonts"))) {
    fs.mkdirSync(path.join(outputDir,"/fonts"));
}


function downloadFile(fileUrl, outputPath) {
    return new Promise((resolve, reject) => {
        const file = fs.createWriteStream(outputPath);
        https.get(fileUrl, (response) => {
            if (response.statusCode !== 200) {
                reject(new Error(`Failed to download file: ${fileUrl}`));
                return;
            }
            response.pipe(file);
            file.on('finish', () => {
                file.close(resolve);
            });
        }).on('error', (err) => {
            fs.unlink(outputPath, () => reject(err));
        });
    });
}

// Download and process the CSS
https.get(cssUrl, { headers: HEADERS[FORMAT] }, (res) => {
    if (res.statusCode !== 200) {
        console.error(`Failed to fetch CSS from ${cssUrl}`);
        process.exit(1);
    }

    let cssData = '';
    res.on('data', (chunk) => {
        cssData += chunk;
    });

    res.on('end', async () => {
        const urls = Array.from(new Set([...cssData.matchAll(regUrl)].map(match => match[1])));
        let newCss = cssData;

        for (const fontUrl of urls) {
            const fontName = path.basename(fontUrl);
            const outputPath = path.join(outputDir,"fonts", fontName);

            if (!fs.existsSync(outputPath)) {
                console.log(`Downloading: ${outputPath}`);
                await downloadFile(fontUrl, outputPath);
            } else {
                console.log(`Already exists: ${outputPath}`);
            }

            newCss = newCss.replaceAll(fontUrl, `fonts/${fontName}`);
        }

        fs.writeFileSync(path.join(outputDir,"fonts.css"), newCss);
        console.log("Generated: 'fonts.css'");
    });
}).on('error', (err) => {
    console.error(`Error fetching CSS: ${err.message}`);
    process.exit(1);
});