import urllib.request
import re

req = urllib.request.Request(
    'https://theperforaa.myshopify.com',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Fix protocol-relative URLs (//cdn.shopify.com -> https://cdn.shopify.com)
html = html.replace('"//cdn.shopify.com', '"https://cdn.shopify.com')
html = html.replace("'//cdn.shopify.com", "'https://cdn.shopify.com")

# Fix internal shopify root links
html = html.replace('href="/"', 'href="#"')
html = html.replace('href="/collections/all"', 'href="https://theperforaa.myshopify.com/collections/all"')
html = re.sub(r'href="/products/([^"]+)"', r'href="https://theperforaa.myshopify.com/products/\1"', html)

# Add a sleek portfolio banner at top
portfolio_banner = (
    '<div style="background: linear-gradient(90deg, #4c2882, #6b3ba6); color: #ffffff; '
    'text-align: center; padding: 12px 20px; font-family: -apple-system, BlinkMacSystemFont, '
    '\'Segoe UI\', Roboto, sans-serif; font-size: 14px; font-weight: 600; display: flex; '
    'align-items: center; justify-content: center; gap: 16px; z-index: 9999999; position: relative;">'
    '<span>✨ <strong>Perfora Teeth Whitening E-Commerce Store</strong> (Shopify Custom Theme Demo)</span>'
    '<a href="https://theperforaa.myshopify.com" target="_blank" rel="noopener" '
    'style="background: #ffffff; color: #4c2882; padding: 6px 14px; border-radius: 4px; '
    'text-decoration: none; font-size: 13px; font-weight: 700; transition: opacity 0.2s;">Visit Live Store &rarr;</a>'
    '</div>'
)

if '<body' in html:
    html = re.sub(r'(<body[^>]*>)', r'\1' + portfolio_banner, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully generated index.html! Bytes:', len(html))
