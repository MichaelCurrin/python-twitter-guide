/**
 * Nav to routes module.
 *
 * Convert links in configured navbar into routes for prerendering.
 */
const fs = require('fs');
const path = require('path');
const { SitemapStream } = require('sitemap');

const NAV_PATH = path.join(__dirname, 'docs', '_navbar.md');

const VAR = 'var';
const ROUTES_NAME = 'routes.json';
const SITEMAP_NAME = 'sitemap.xml';
const ROBOTS_NAME = 'robots.txt';

const ROUTES_PATH = path.join(__dirname, VAR, ROUTES_NAME);
const SITEMAP_PATH = path.join(__dirname, VAR, SITEMAP_NAME);
const ROBOTS_PATH = path.join(__dirname, VAR, ROBOTS_NAME);
const HOSTNAME = 'https://python-twitter-guide.netlify.app';

function writeRoutes(names) {
    console.log(`Writing: ${ROUTES_NAME}`);

    // Make into Docsify routes so presite can scan them.
    paths = names.map(i => `/#/${i}`);

    fs.writeFile(ROUTES_PATH, JSON.stringify(paths, null, 4), err => {
        if (err) {
            throw new Error(err);
        }
    });
}

// Based on https://github.com/ekalinin/sitemap.js/blob/master/examples/write-to-file.js
function writeSitemap(names) {
    console.log(`Writing: ${SITEMAP_NAME}`);

    const { createWriteStream } = require('fs');

    const sitemap = new SitemapStream({ hostname: HOSTNAME });

    const writeStream = createWriteStream(SITEMAP_PATH);
    sitemap.pipe(writeStream);

    // e.g. '/page-2'
    let paths = names.map(n => `/${n}`);
    for (let path of paths) {
        sitemap.write(path);
    }
    sitemap.end();
}

function writeRobots() {
    console.log(`Writing: ${ROBOTS_NAME}`);

    let content = `Sitemap: ${HOSTNAME}/${SITEMAP_NAME}`;

    fs.writeFile(ROBOTS_PATH, content, err => {
        if (err) {
            throw new Error(err);
        }
    });
}

function writeAll(names) {
    writeRoutes(names);
    writeSitemap(names);
    writeRobots();
}

fs.readFile(NAV_PATH, 'utf-8', (_, data) => {
    var matches = data.match(/\w+.md/gi);
    // Add root as it get missed by regex.
    matches.push('');
    var names = matches.map(i => i.replace('.md', ''));

    writeAll(names);
});
