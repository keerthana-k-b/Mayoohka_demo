const fs = require('fs');
const code = fs.readFileSync('js/products.js', 'utf8');

// evaluate
const ctx = {};
const fn = new Function('ctx', code + '\nctx.PRODUCTS = PRODUCTS;\nctx.CATEGORIES = CATEGORIES;');
fn(ctx);

fs.writeFileSync('scratch/products.json', JSON.stringify(ctx.PRODUCTS, null, 2));
console.log('Exported products:', ctx.PRODUCTS.length);
