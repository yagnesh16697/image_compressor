# FastAPI Image Compression API

This FastAPI application provides a simple API for compressing images. It supports various image formats, including PNG, JPG, and JPEG. The compressed images are saved in a designated folder with new filenames.

## Installation

1. Install the required dependencies using the following command:

   ```bash
   pip install fastapi uvicorn Pillow
   ```

2. Clone the repository or download the `main.py` file.

3. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

## Usage

### API Endpoint

- **Endpoint**: `/compress`
- **Method**: `POST`
- **Parameters**:
  - `upload_file`: Image file to be compressed (PNG, JPG, JPEG supported).
  - `quality` (optional): Compression quality (default: 85).

### Example Usage

1. Open the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.
2. Navigate to the `/compress` endpoint.
3. Upload an image file.
4. Optionally, specify the compression quality.
5. Execute the request.

The compressed image will be displayed, and the compressed image file will be saved in the `compressed_images` folder.

## Folder Structure

- `uploads`: Folder for storing uploaded images.
- `compressed_images`: Folder for storing compressed images.

## Customization

- You can customize the folder names by modifying the `UPLOAD_FOLDER` and `COMPRESSED_FOLDER` constants in the `main.py` file.

## Error Handling

- The API handles errors gracefully and returns appropriate HTTP status codes and error details.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [Pillow](https://pillow.readthedocs.io/)

## License

This FastAPI Image Compression API is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README further based on your specific requirements and preferences. Additionally, consider providing information on how to deploy the application in a production environment, security considerations, and any other relevant details.
