/**
 * Nav to routes module.
 *
 * Convert links in configured navbar into routes for prerendering.
 */
const fs = require('fs');
const path = require('path');

const inPath = path.join(__dirname, 'docs/_navbar.md');
const outPath = path.join(__dirname, 'routes.json');

fs.readFile(inPath, 'utf-8', (_, data) => {
    var matches = data.match(/\w+.md/gi);
    matches.push('');
    var results = matches.map(i => i.replace('.md', ''));
    results = results.map(i => `/#/${i}`);

    fs.writeFile(outPath, JSON.stringify(results, null, 4), err => {
        if (err) {
            throw new Error(err);
        }
        console.log('Done.');
    });
});
