import wikipedia

while True:
    # Prompt the user for a page title or search phrase
    user_input = input("Enter a page title or search phrase (blank to exit): ").strip()

    # Exit the loop if the user enters blank input
    if not user_input:
        break

    try:
        # Use the Wikipedia API to get a page based on user input
        page = wikipedia.page(user_input, auto_suggest=False)

        # Handle disambiguation pages
        if "disambiguation" in page.summary.lower():
            print(f"Disambiguation page: {page.title}")
            continue

        # Check if the page title differs from user input due to autosuggest
        if page.title.lower() != user_input.lower():
            print(f"Suggested page: {page.title}")
            continue

        # Print the title, summary, and URL of the page
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}\n")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation page: {e.options}")
    except wikipedia.exceptions.HTTPTimeoutError:
        print("Error: Unable to connect to Wikipedia. Please try again later.")
    except wikipedia.exceptions.WikipediaException as e:
        print(f"Error: {e}")
