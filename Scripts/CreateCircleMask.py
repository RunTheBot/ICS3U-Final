# from PIL import Image, ImageDraw
# import os

# def create_circle_mask(radius, step):
#     # Define the image size (720p), but create the image at a smaller size for the pixel art effect
#     width, height = 160, 90

#     # Calculate the center of the image
#     center = (width // 2, height // 2)

#     # Loop until the radius is greater than 0
#     while radius >= 0:
#         # Create a new image with a black background and an alpha channel
#         img = Image.new('RGBA', (width, height), 'black')

#         # Create a draw object
#         draw = ImageDraw.Draw(img)

#         # Draw the circle mask with a transparent color
#         draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=(0, 0, 0, 0))

#         # Scale the image up to create the pixel art effect
#         img = img.resize((1280,720), Image.NEAREST)

#         # Save the image
#         img.save(f'circle_mask_{radius}.png')

#         # Decrease the radius for the next circle
#         radius -= step


# def test_draw_one_frame():
#     # Call the function to draw one frame
#     create_circle_mask(91, 91)

# create_circle_mask(91, 1)