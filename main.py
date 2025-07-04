from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import asyncio
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "EOIR scraper is running."}

@app.get("/eoir")
async def get_eoir_info(a_number: str = Query(..., alias="a_number")):
    result = await scrape_eoir(a_number)
    return JSONResponse(content=result)

async def scrape_eoir(a_number):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://portal.eoir.justice.gov/InfoSystem/Form")
        await page.fill("#aNumber", a_number)
        await page.click("button[type='submit']")
        await page.wait_for_timeout(4000)
        content = await page.content()
        await browser.close()
        return {"status": "OK", "raw_html": content}
