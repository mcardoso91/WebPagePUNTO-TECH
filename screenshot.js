const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: "new",
    args: ['--no-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  
  // Go to the page
  await page.goto('http://localhost:8000', { waitUntil: 'networkidle2' });
  
  // Take a full page screenshot
  await page.screenshot({ path: '/Users/matiascardoso/Documents/PUNTO-TECH_WEB/screenshot_full.png', fullPage: true });

  // Scroll down a bit and take another screenshot of the services section
  await page.evaluate(() => {
    window.scrollTo(0, 4500); // Scroll to around where the services section is
  });
  await new Promise(r => setTimeout(r, 1000));
  await page.screenshot({ path: '/Users/matiascardoso/Documents/PUNTO-TECH_WEB/screenshot_services.png' });

  await browser.close();
  console.log("Screenshots saved.");
})();
