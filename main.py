from configparser import ConfigParser
import google.generativeai as genai
import PIL.Image
import os

img_contains_word_list = []

config = ConfigParser()
config.read("credentials.ini")
api_key = config["API_KEY"]["google_api_key"]

genai.configure(api_key=api_key)

model_gemini_pro_vision = genai.GenerativeModel("gemini-pro-vision")

def split_image(image_path, output_folder):
    original_image = PIL.Image.open(image_path)
    small_width, small_height = 100, 100

    count = 0
    for i in range(3):
        for j in range(3):
            left = j * small_width
            upper = i * small_height
            right = left + small_width
            lower = upper + small_height

            small_image = original_image.crop((left, upper, right, lower))
            small_image.save(f"{output_folder}/small_image_{count}.png")

            count += 1

def test_multiple_images(total_image_path):
    img = PIL.Image.open(total_image_path)
    prompt = "One or Multiple. Is this one image or multiple?"
    response = model_gemini_pro_vision.generate_content((prompt, img))
    lower_response_text = response.text.lower()

    if "one" in lower_response_text or "single" in lower_response_text:
        return False
    else:
        return True
    
def test_image_contains(image_path, contains_word):
    small_img = PIL.Image.open(image_path)
    prompt = f"Yes or No. Does this image contain {contains_word}"
    response = model_gemini_pro_vision.generate_content((prompt, small_img))
    lower_response_text = response.text.lower()

    #print(lower_response_text)

    if "yes" in lower_response_text:
        return True
    elif "no" in lower_response_text:
        return False
    else:
        return None

def main(path_to_img, output_folder, word_to_contain):
    if test_multiple_images(path_to_img):
        split_image(path_to_img, output_folder)

        for image in os.listdir(output_folder):
            img_path = os.path.join(output_folder, image)

            return_val = test_image_contains(img_path, word_to_contain)
            img_contains_word_list.append(return_val)

        print(img_contains_word_list)
    else:
        print("Request new reCAPTCHA images") #Your logic to request new reCAPTCHA images

if __name__ == "__main__":
    path_to_img = "testCaptcha04.jpg"
    output_folder = "output_images"
    word_to_contain = "a crosswalk"

    main(path_to_img, output_folder, word_to_contain)