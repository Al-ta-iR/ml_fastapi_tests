[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions


# ML FastAPI Application for Sentiment Analysis

This is a simple FastAPI application that uses a pre-trained model from the Hugging Face library to perform sentiment analysis on text input.

## Requirements

- Python 3.6 or higher
- FastAPI
- Transformers (Hugging Face library)

## Installation

1. Clone the repository:

git clone https://github.com/tokarevsas31/ml_fastapi_tests.git


2. Navigate to the project directory:

cd ml_fastapi_tests


3. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate


4. Install the required packages:

pip install -r requirements.txt


## Running the Application

To run the application, execute the following command:

uvicorn main:app --reload


The application will be available at `http://localhost:8000`.

## API Endpoints

- `GET /`: Returns a simple "Hello World" message.
- `POST /predict/`: Performs sentiment analysis on the provided text. Send a JSON payload with the following structure:

```json
{
  "text": "Your text for sentiment analysis"
}

The response will contain the predicted sentiment label (e.g., "POSITIVE", "NEGATIVE", or "NEUTRAL").
Project Structure

    main.py: Contains the FastAPI application and the sentiment analysis endpoint.
    test_main.py: Contains unit tests for the application.
    requirements.txt: Lists the required Python packages for the project.
    .git/: Git repository metadata.
    venv/: Virtual environment for isolating project dependencies (optional).
