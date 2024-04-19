# Beautiful Soup is a Python library that helps extract data from HTML and XML files. It makes web scraping easier by providing tools to navigate and search for tags, attributes, and text within HTML files.

# 1. Install Beautiful Soup 

# 2. Import the necessary libraries:

# 3. Retrieve the HTML content from a website:


url = 'https://example.com'
response = requests.get(url)
html_content = response.text

# 4. Create a BeautifulSoup object to parse the HTML content:

soup = BeautifulSoup(html_content, 'html.parser')

# 5. Navigate through the HTML content to find the data you want:

# Find all <a> tags with class 'title'

titles = soup.find_all('a', class_='title')

# Print the text content of each title

for title in titles:
    print(title.text)


# This is a basic example of how to use Beautiful Soup for web scraping. You can explore more functionalities of the library, such as navigating through the HTML structure, finding specific tags or attributes, and extracting data based on specific criteria.
