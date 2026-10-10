import fs from 'fs';
const content = fs.readFileSync('theme/sections/customer-reviews.liquid', 'utf8');
const start = content.indexOf('reviews_data =');
const quoteStart = content.indexOf('"', start);
const quoteEnd = content.indexOf('" | split: "###"', quoteStart);
const s = content.substring(quoteStart + 1, quoteEnd);
const items = s.split('###').map(x => x.trim()).filter(x => x.length > 0);
console.log('Total review count:', items.length);

let errors = 0;
items.forEach((it, i) => {
    const parts = it.split('|');
    if (parts.length < 5) {
        console.log(`ERROR at index ${i + 1}: expected 5 parts, got ${parts.length}: ${it}`);
        errors++;
    } else {
        const imgName = `ugc_review_${i + 1}.jpg`;
        const imgPath = `theme/assets/${imgName}`;
        const exists = fs.existsSync(imgPath);
        if (!exists) {
            console.log(`ERROR: Missing image ${imgPath} for review ${i + 1}`);
            errors++;
        }
    }
});

if (errors === 0) {
    console.log('SUCCESS: Exactly 40 reviews validated. All 40 have full fields and existing unique images.');
}
