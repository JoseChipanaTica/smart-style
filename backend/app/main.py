from typing import Optional

from app.core.pipelines.clothing import ClothingPipeline
from app.core.pipelines.outfit import OutfitStylePipeline
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/outfit")
async def upload_image_with_text(
    file: UploadFile = File(...), description: str = Form(...)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

    file_content = await file.read()

    ext = file.filename.split(".")[-1]

    OutfitStylePipeline().run(file_content, ext)

    return JSONResponse(
        content={
            "filename": file.filename,
            "content_type": file.content_type,
            "description": description,
        }
    )


@app.post("/clothing")
async def clothing(
    file: UploadFile = File(...), gender: str = Form(...), description: str = Form(None)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

    file_content = await file.read()

    print(gender)
    response = ClothingPipeline().run(file_content, description, gender)

    return JSONResponse(content=response)
