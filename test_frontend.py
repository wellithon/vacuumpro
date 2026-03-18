from playwright.sync_api import sync_playwright
import os

def run(page):
    cwd = os.getcwd()

    # Check index for Ezequiel button
    page.goto(f"file://{cwd}/index.html")
    page.wait_for_timeout(1000)
    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_timeout(500)
    page.screenshot(path="/home/jules/verification/index_ezequiel.png")

    # Check produtos for the 6 aligned cards
    page.goto(f"file://{cwd}/produtos.html")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/produtos_cards.png")

    # Check cidades for the new accordions
    page.goto(f"file://{cwd}/cidades.html")
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/cidades_accordion.png")

    # Click first accordion
    page.locator('summary', has_text="Paraná").click()
    page.wait_for_timeout(1000)
    page.screenshot(path="/home/jules/verification/cidades_open.png")

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/video", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(record_video_dir="/home/jules/verification/video")
        page = context.new_page()
        try:
            run(page)
        finally:
            context.close()
            browser.close()
