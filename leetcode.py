from playwright.sync_api import sync_playwright


class LeetCodeClient:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.cookies = {}

    def connect(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.connect_over_cdp(
            "http://127.0.0.1:9222"
        )

        self.context = self.browser.contexts[0]

        for cookie in self.context.cookies():
            self.cookies[cookie["name"]] = cookie["value"]

    def get_cookie_header(self):
        needed = [
            "LEETCODE_SESSION",
            "csrftoken",
        ]

        parts = []

        for name in needed:
            if name in self.cookies:
                parts.append(f"{name}={self.cookies[name]}")

        return "; ".join(parts)

    def csrf(self):
        return self.cookies["csrftoken"]

    def close(self):
        self.browser.close()
        self.playwright.stop()