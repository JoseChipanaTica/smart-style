# Smart-Style

## Overview
This project enables users to generate outfits based on their own clothing or uploaded items, along with a description and specified gender.

When a clothing item is uploaded, the application extracts its image embedding and description. The image description is then converted into embeddings. Both the image embeddings and description embeddings are compared with preloaded outfit database embeddings to identify similar outfits.

Finally, the clothing description and the similar outfits are sent to the LLM to create new outfit suggestions. Using Stability, an image is generated for each new outfit.

## Project Structure
```
root
├── backend      # FastAPI backend
└── frontend     # Next.js frontend
```

## Backend
The backend is implemented using **FastAPI** and provides the following key functionalities:

### Endpoints
1. **Image Upload Endpoint**
   - Accepts an image file via HTTP POST.
   - Processes the image to generate embeddings.
   - Stores the image and its embeddings in Supabase.

2. **Outfit Recommendation Endpoint**
   - Accepts a reference to a clothing item.
   - Generate similar outfits based on embeddings.
   - Generate one image for each generated outfit.

### Setup
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Set up environment variables:
   - Ensure the following variables are configured:
     - `SUPABASE_URL`
     - `SUPABASE_KEY`
     - Other configurations as needed.
4. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Frontend
The frontend is developed using **Next.js** to provide a seamless user experience for uploading images and viewing recommendations.

### Features
- **Responsive Design**: Works across devices for an optimal user experience.
- **Upload Interface**: Allows users to upload clothing images.
- **Recommendation Display**: Shows a list of similar outfits with their details.

### Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
4. Open the application in your browser at `http://localhost:3000`.

## Technologies Used
### Backend
- **FastAPI**: For API development.
- **Supabase**: To store images and embeddings.
- **ML Libraries**: Used for generating embeddings (e.g., PyTorch, TensorFlow).

### Frontend
- **Next.js**: For building the user interface.
- **TailwindCSS** (optional): For styling components.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Set up the backend and frontend as described above.
3. Ensure both the backend and frontend are running:
   - Backend: `http://localhost:8000`
   - Frontend: `http://localhost:3000`
4. Interact with the application through the frontend interface.

## Future Improvements
- Integrate a database for advanced analytics and tracking.
- Add user authentication for a personalized experience.
- Extend the recommendation engine with multi-modal embeddings (e.g., text and image).

---
Feel free to contribute or provide suggestions for improvement!

