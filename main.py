from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
from io import BytesIO
import os

app = FastAPI()

COMPRESSED_FOLDER = "compressed_images"

# Ensure that the upload and compressed folders exist
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

def compress_image(image_bytes, quality=85):
    image = Image.open(BytesIO(image_bytes))
    
    # Convert RGBA to RGB if the image has an alpha channel
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    
    output_buffer = BytesIO()
    
    # Determine image format based on the file extension
    format = image.format if image.format else 'JPEG'
    
    image.save(output_buffer, format=format, quality=quality)
    compressed_image = output_buffer.getvalue()
    return compressed_image

@app.post("/compress")
async def compress(upload_file: UploadFile = File(...), quality: int = 85):
    try:
        contents = await upload_file.read()
        compressed_image = compress_image(contents, quality)

        # Save the compressed image to the compressed folder with a new filename
        compressed_filename = f"{COMPRESSED_FOLDER}/{upload_file.filename.split('.')[0]}_compressed.{upload_file.filename.split('.')[-1].lower()}"
        with open(compressed_filename, "wb") as compressed_file:
            compressed_file.write(compressed_image)

        return StreamingResponse(BytesIO(compressed_image), media_type=f"image/{upload_file.filename.split('.')[-1].lower()}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
