# PDF Knowledge Base Assistant with GROQ API

This Streamlit app allows users to interact with a knowledge base created from a PDF document. Users can provide a PDF URL and a GROQ API key to load the knowledge base and ask questions. The app uses PostgreSQL for storage and integrates with the GROQ API for processing.

## Features

- **PDF Knowledge Base**: Load a knowledge base from a PDF URL.
- **GROQ API Integration**: Use the GROQ API for processing and querying.
- **PostgreSQL Storage**: Store assistant data in a PostgreSQL database.
- **Interactive Chat**: Ask questions and get responses from the assistant.

## Prerequisites

Before running the app, ensure you have the following:

1. **Python 3.7+**: The app is built using Python.
2. **PostgreSQL**: A running PostgreSQL database with the necessary credentials.
3. **GROQ API Key**: Obtain a GROQ API key from [GROQ](https://groq.com/).
4. **Environment Variables**: Set up a `.env` file with your GROQ API key and database URL.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pdf-knowledge-base-assistant.git
   cd pdf-knowledge-base-assistant
1. Install the required Python packages:
   pip install -r requirements.txt
2. Create a .env file in the root directory and add your environment variables:
   GROQ_API_KEY=your_groq_api_key
   DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/dbname
Note: Replace your_groq_api_key, username, password, localhost, 5432, and dbname with your actual values.
## Usage
1. Run the Streamlit app:
streamlit run app.py
2. Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501)
3. In the sidebar:

- Enter your GROQ API KEY.
- Provide the PDF URL of the document you want to load into the knowledge base.
- Enter a User ID (default is user).
- Check the Start New Session box if you want to start a new session.

4. Click Load Knowledge Base to initialize the assistant.
5. In the main area, type your question in the input box and press Enter to get a response from the assistant.

# Project Structure
pdf-knowledge-base-assistant/
├── app.py                # Streamlit application code
├── README.md             # Project documentation
├── requirements.txt      # List of dependencies
└── .env                  # Environment variables

## Dependencies
- streamlit: For building the web app.
- phi: For the assistant and knowledge base functionality.
- python-dotenv: For loading environment variables.
- typer: For CLI functionality (used in the original code).

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch and submit a pull request

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Streamlit for the web app framework.
- GROQ for the API integration.
- Phi for the assistant and knowledge base functionality.


### Key Sections:
1. **Features**: Highlights the main functionalities of the app.
2. **Prerequisites**: Lists the requirements for running the app.
3. **Installation**: Provides step-by-step instructions for setting up the app.
4. **Usage**: Explains how to use the app.
5. **Project Structure**: Describes the files in the repository.
6. **Dependencies**: Lists the required Python packages.
7. **Contributing**: Encourages contributions and explains how to contribute.
8. **License**: Specifies the license for the project.
9. **Acknowledgments**: Credits the tools and libraries used.

