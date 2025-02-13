import requests
import html2text

class URLProcessor:
    """Handles URL fetching and converting to Markdown."""

    def __init__(self):
        """Initializes the URLProcessor."""
        pass

    def fetch_page_content(self, url):
        """
        Fetches the content of a given URL.

        Args:
            url (str): The URL to fetch content from.

        Returns:
            str: The HTML content of the page, or None if an error occurs.
        """
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            )
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content from URL '{url}': {e}")
            return None

    def convert_to_markdown(self, url, html_content):
        """
        Converts HTML content to Markdown format.

        Args:
            url (str): The URL being processed.
            html_content (str): The HTML content fetched from the URL.

        Returns:
            str: The formatted Markdown content.
        """
        converter = html2text.HTML2Text()
        converter.ignore_links = False
        markdown_content = converter.handle(html_content)

        # Add a reference header
        return f"# Processed Content from URL: {{'REFERENCE': '{url}'}}\n\n{markdown_content}"
