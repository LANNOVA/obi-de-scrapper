# Obi-DE-scrapper

## Description

This Python script scrapes product information from the OBI website based on the user's input for the item name. It retrieves data such as product name, price, product link, average rating, description, EAN, thumbnail image URL, and manufacturer (if available) using web scraping and API requests.

## Prerequisites

Before running the script, you need to make sure you have the following dependencies installed:

- Python (version 3.x)
- Requests library (\`pip install requests\`)
- BeautifulSoup library (\`pip install beautifulsoup4\`)

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

   ``` shell
   python scrapper.py
   ```

4. The script will prompt you to enter the item name you want to search for on the OBI website. Enter the item name and press Enter.

5. The script will scrape the OBI website, retrieve information about the products that match your search, and display the data in the terminal.

##  Script Overview

- The script begins by importing the required libraries: \`requests\`, \`BeautifulSoup\`, \`json\`, and \`re\`.

- It sets the user-agent and language headers for web requests.

- The user is prompted to enter the item name they want to search for on the OBI website.

- The script constructs the URL for the OBI search based on the user's input.

- It sends an HTTP GET request to the OBI website and uses BeautifulSoup to parse the HTML content of the page.

- The script extracts product information, including name, price, product link, and more, and prints it to the terminal.

- It also makes API requests to retrieve additional product information, such as average rating, description, EAN, thumbnail image URL, and manufacturer.

- The retrieved data is displayed in the terminal.

## Note

- This script is for educational purposes and should be used responsibly and in accordance with the terms of service of the OBI website.

- Web scraping may be subject to legal restrictions, so ensure that you have the necessary permissions and rights to scrape data from external websites.

- The script may require adjustments if the structure of the OBI website changes in the future.

- Be aware that web scraping can place a load on websites, so consider implementing rate limiting and error handling if you plan to use this script extensively.

## Donations

BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
