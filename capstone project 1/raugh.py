import pyautogui
im = pyautogui.screenshot()
print(im)
#gathers the pixel data at the given pixel coordinates
pixel_data = im.getpixel((50, 200))
print(pixel_data)
    # checking for the true case of color Match
true_case = pyautogui.pixelMatchesColor(50, 200, pixel_data)
print(true_case)
    #checking for the false case of color match
false_case = pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
print(false_case)