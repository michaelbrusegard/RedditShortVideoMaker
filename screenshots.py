import os
from playwright.sync_api import ViewportSize, sync_playwright

def take_screenshots(url: str, username, password) -> bytes:
    
    with sync_playwright() as playwright:
        print('Opening Browser...')
        # Start a headless Chromium browser context
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            color_scheme='dark',
            locale='en-GB',
            viewport=ViewportSize(width=540, height=960),
            device_scale_factor=2
            )
        page = context.new_page()

        print('Logging in to Reddit...')
        # Navigate to the login page
        page.goto('https://www.reddit.com/login')
        page.wait_for_load_state()
    
        # Fill in the username field
        username_field_selector = 'input#loginUsername'
        username_field = page.wait_for_selector(username_field_selector)
        username_field.fill(username)

        # Fill in the password field
        password_field_selector = 'input#loginPassword'
        password_field = page.wait_for_selector(password_field_selector)
        password_field.fill(password)

        # Click the 'Log In' button
        login_button_selector = 'button.AnimatedForm__submitButton'
        login_button = page.wait_for_selector(login_button_selector)
        login_button.click()

        page.wait_for_timeout(5000)
        page.wait_for_load_state()

        # Navigate to the post
        page.goto(url)

        # Click the button to reject non-essential cookies
        button_selector = 'button:has-text("Reject non-essential")'
        page.click(button_selector)

        # Click the button to dismiss NSFW warnings
        button_selector = 'button.gCpM4Pkvf_Xth42z4uIrQ'
        button = page.query_selector(button_selector)
        if button:
            button.click()

        page.wait_for_load_state()
    
        post_content_selector = '[data-test-id="post-content"]'
        post_screenshots = []

        print('Taking screenshot of title...')

        # Wait for the title element to be available
        title_selector = f'{post_content_selector} > div:nth-child(3)'
        title_handle = page.wait_for_selector(title_selector)
        
        # Get the bounding box of the element
        title_bbox = title_handle.bounding_box()

        # Add some extra space around the element
        padding_height = 32
        padding_width = 8
        title_bbox['x'] -= padding_width
        title_bbox['y'] -= padding_height
        title_bbox['width'] += padding_width * 2
        title_bbox['height'] += padding_height + padding_width

        # Take a screenshot of the expanded area
        title_screenshot = page.screenshot(clip=title_bbox, type='png')
        post_screenshots.append(title_screenshot)

        print('Taking screenshots of content...')
        # Wait for the content element to be available
        content_selector = f'{post_content_selector} > div:nth-child(4) > div:first-child'
        content_handle = page.query_selector(content_selector)
        content_text = content_handle.query_selector_all('p')

        # loop through each child element and do something with it
        for i, paragraph in enumerate(content_text):
            paragraph.scroll_into_view_if_needed()
            paragraph_bbox = paragraph.bounding_box()
            padding = 8     

            if i == 0:
                paragraph_bbox['y'] -= padding + 2
                paragraph_bbox['height'] += padding * 2

            else:
                paragraph_bbox['height'] += padding

            paragraph_bbox['x'] -= padding
            paragraph_bbox['width'] += padding * 2
            post_screenshots.append(page.screenshot(clip=paragraph_bbox, type='png'))
            

        # Close the browser context
        browser.close()

         # Create the assets directory if it doesn't exist
        if not os.path.exists('assets'):
            os.makedirs('assets')
        
        # Create an empty list to store the filenames
        filenames = []
        
        # Iterate through each screenshot and save it to a file
        for i, screenshot in enumerate(post_screenshots):
            # Set the file name and path
            file_name = f'screenshot_{i}.png'
            file_path = os.path.join('assets', file_name)

            # Write the binary content to a png file
            with open(file_path, 'wb') as out:
                out.write(screenshot)

            # Add the file path to the list
            filenames.append(file_name)
        
    return filenames