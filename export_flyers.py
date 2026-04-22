import os
import asyncio
from playwright.async_api import async_playwright

async def export_pngs():
    base_dir = r"C:\Users\ADM\Desktop\DevOps_KrM\Lidiane Turismo\Costa do Sauipe"
    export_dir = os.path.join(base_dir, "Exports")
    
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        
    print("Starting HTML to PNG export using Playwright...")
    
    files = [f for f in os.listdir(base_dir) if f.startswith("flyer_") and f.endswith(".html")]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Set viewport to exact flyer size
        page = await browser.new_page(viewport={'width': 1080, 'height': 1920})
        
        for f in files:
            html_path = os.path.join(base_dir, f)
            url = "file:///" + html_path.replace("\\", "/")
            out_name = f.replace(".html", ".png")
            out_path = os.path.join(export_dir, out_name)
            
            print(f"Exporting {f}...")
            try:
                await page.goto(url, wait_until="networkidle")
                
                # Execute JS to perfectly reset the container for capturing
                await page.evaluate('''() => {
                    // Reset body
                    document.body.style.margin = '0';
                    document.body.style.padding = '0';
                    document.body.style.display = 'block';
                    document.body.style.minHeight = 'auto';
                    document.body.style.background = 'transparent';
                    document.body.style.overflow = 'hidden';
                    
                    // Reset container
                    const container = document.querySelector('.story-container');
                    if (container) {
                        container.style.transform = 'none';
                        container.style.margin = '0';
                        container.style.position = 'absolute';
                        container.style.top = '0';
                        container.style.left = '0';
                        container.style.borderRadius = '0';
                        container.style.boxShadow = 'none';
                    }
                }''')
                
                # Take screenshot of the exact container element, ensuring flawless cropping
                container = await page.query_selector('.story-container')
                if container:
                    await container.screenshot(path=out_path)
                    print(f"Success: Saved to {out_path}")
                else:
                    print(f"Error: .story-container not found in {f}")
                    
            except Exception as e:
                print(f"Failed to export {f}: {e}")
                
        await browser.close()
            
    print("Export process finished!")

if __name__ == "__main__":
    asyncio.run(export_pngs())
