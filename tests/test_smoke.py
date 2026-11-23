from playwright.sync_api import expect, Page
import os

def test_home_page_title(page: Page):
    page.goto(os.getenv("BASE_URL"))
    expect(page).to_have_title("Practice Software Testing - Toolshop - v5.0")