# YouTube Assistant
## Overview
The YouTube Assistant is a powerful tool designed to help you extract valuable insights from YouTube videos. By leveraging advanced NLP models, it processes video transcripts and allows you to query them effectively. This tool integrates several libraries and APIs to provide detailed and contextually accurate responses based on video content.

## Features
- **YouTube Video Loading:** Fetch and process video transcripts from YouTube.
- **Text Splitting:** Break down transcripts into manageable chunks for efficient querying.
- **Embedding Generation:** Create vector embeddings from transcripts using Google Generative AI.
- **Similarity Search:** Search for relevant content within the video transcript based on your queries.
- **Question Answering:** Generate detailed responses to questions about the video content.

## Setup
### 1. Clone the Repository

```bash
git clone https://github.com/mshaadk/Youtube-Assistant-LangChain.git
cd Youtube-Assistant-LangChain
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Usage
### 1. Run the Application

```bash
streamlit run main.py
```

### 2. Interact with the Application

- Open your browser and navigate to `http://localhost:8501`.
- Paste the YouTube video URL in the sidebar and enter your query.
- Click "Submit" to get responses based on the video transcript.

## Code Explanation
`create_db_from_youtube_video_url(video_url)`
- Input: YouTube video URL.
- Process:
  - Load the transcript of the video.
  - Split the transcript into chunks for processing.
  - Generate embeddings for each chunk.
  - Create a FAISS vector store from the chunks and embeddings.
- Output: FAISS vector store for querying.
  
`get_response_from_query(db, query)`
- Input: FAISS vector store and query.
- Process:
  - Perform similarity search to find relevant chunks.
  - Combine the content of these chunks.
  - Use OpenAI's GPT model to generate a detailed response based on the query and combined content.
- Output: Response to the query and the relevant documents used.

## Contributing
Feel free to fork the repository and submit pull requests. If you encounter any issues or have suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
