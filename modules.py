# importing required libraries 
from PIL import Image
import numpy as np
import time

# encryption method
def encrypt_image(image_path, key):
    # open the image
    img = Image.open(image_path)
    
    # converting the image to a numpy array
    img_array = np.array(img)
    
    # perform the encryption operation
    encrypted_array = img_array.copy()
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(img_array.shape[2]):
                encrypted_array[i, j, k] = np.clip(encrypted_array[i, j, k] + np.uint8(key), 0, 255)
        
    print("Processing...")            
                
    # converting the array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    
    # saving the image with new name
    encrypted_img.save('encrypted_img.png')
    
    #success message 
    print("Image encryption successfull")
  
# decryption method  
def decrypt_image(image_path, key):
    # open the image
    img = Image.open(image_path)
    
    # converting the image to a numpy array
    img_array = np.array(img)
    
    # perform the decryption operation
    encrypted_array = img_array.copy()
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(img_array.shape[2]):
                encrypted_array[i, j, k] = np.clip(encrypted_array[i, j, k] - np.uint8(key), 0, 255)
             
    print("Processing...")

    # converting the array back to an image
    decrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    
    # saving the image with new name
    decrypted_img.save('decrypted_img.png')
    
    #success message 
    print("Image decryption successfull")
