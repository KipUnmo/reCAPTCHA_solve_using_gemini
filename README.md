# reCAPTCHA solver

This reCAPTCHA solver is meant to be used in larger project that for example utilize the [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/) library to control bots. The logic procided in this script will be able to solve image based reCAPTCHA's.

## Disclaimer
When utilizing this code in any way, you are taking full responsibility for your actions and any consequences (e.g. account bans, user agreement violations, etc), and in no circumstances can I be held accountable for anything.

## Requirements
To execute this code the following libraries need to be installed.

[Pillow](https://pillow.readthedocs.io/en/stable/) for image manipulation.
```bash
pip install Pillow
```
[Google generative AI](https://github.com/GoogleCloudPlatform/generative-ai) to communicate with Gemini AI.
```bash
pip install google-generativeai
```

## Usage
In the file ```credentials.ini``` replace ```YOUR_GOOGLE_API_KEY_HERE``` with your actual Google api key. Note: this is not yet supported worldwide.

After this run ```main.py```

## Test cases
To test the script, change the output folder to any desired location, as example.
```python
output_folder = "output_images"
```
Change the image path to the path of the whole reCAPTCHA image.
```python
path_to_img = "testCaptcha04.jpg"
```
Specify the object that needs to be checked if present.
```python
word_to_contain = "a crosswalk"
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)