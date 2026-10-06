import asyncio
from playwright.sync_api import sync_playwright

def test_navbar():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Test 1280px desktop
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto("http://localhost:8080/index.html")
        page.wait_for_timeout(1000)
        page.locator(".site-header").screenshot(path="scratch/header_desktop_1280px.png")
        print("Captured desktop 1280px")

        # Test 768px tablet
        page = browser.new_page(viewport={"width": 768, "height": 1024})
        page.goto("http://localhost:8080/index.html")
        page.wait_for_timeout(1000)
        page.locator(".site-header").screenshot(path="scratch/header_tablet_768px.png")
        print("Captured tablet 768px")

        # Test 430px mobile (iPhone 14 Pro Max)
        page = browser.new_page(viewport={"width": 430, "height": 932})
        page.goto("http://localhost:8080/index.html")
        page.wait_for_timeout(1000)
        page.locator(".site-header").screenshot(path="scratch/header_mobile_430px.png")
        print("Captured mobile 430px")

        # Test 390px mobile (iPhone 14)
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto("http://localhost:8080/index.html")
        page.wait_for_timeout(1000)
        page.locator(".site-header").screenshot(path="scratch/header_mobile_390px.png")
        print("Captured mobile 390px")

        # Test 360px mobile (Android standard)
        page = browser.new_page(viewport={"width": 360, "height": 800})
        page.goto("http://localhost:8080/index.html")
        page.wait_for_timeout(1000)
        page.locator(".site-header").screenshot(path="scratch/header_mobile_360px.png")
        print("Captured mobile 360px")

        browser.close()

if __name__ == "__main__":
    test_navbar()
