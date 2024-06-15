# from PIL import Image, ImageDraw 
import os

def create_circle_mask(radius, step):
    # Define the image size (720p), but create the image at a smaller size for the pixel art effect
    width, height = 320, 320

    # Calculate the center of the image
    center = (width // 2, height // 2)

    # Loop until the radius is greater than 0
    while radius >= 0:
        # Create a new image with a black background and an alpha channel
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

        # Create a draw object
        draw = ImageDraw.Draw(img)

        # Draw the circle mask with a transparent color
        draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=(255, 255, 255, 255))

        # Scale the image up to create the pixel art effect
        img = img.resize((2560, 2560), Image.NEAREST)

        # Save the image
        img.save(f'light_{radius}.png')

        # Decrease the radius for the next circle
        radius -= step



def test_draw_one_frame():
    # Call the function to draw one frame
    create_circle_mask(91, 91)


create_circle_mask(182, 1)
# create_white_circle(0, 1)