# FastAPI Image Compression API

This FastAPI application provides a simple API for compressing images. It supports various image formats, including PNG, JPG, and JPEG. The compressed images are saved in a designated('/compressed_images') folder with new filenames.

## Installation

1. Create compressed_images folder in same directory
2. Run this command to run API server.

```
docker compose up -d
```

### Example Usage

1. Open the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.
2. Navigate to the `/compress` endpoint.
3. Upload an image file.
4. Optionally, specify the compression quality.
5. Execute the request.

The compressed image will be displayed, and the compressed image file will be saved in the `compressed_images` folder.

## Folder Structure

- `compressed_images`: Folder for storing compressed images.
