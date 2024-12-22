# CV-Helper

This project provides a chatbot that helps users assess how well their CV matches a given job description. The chatbot provides a score and actionable suggestions to help users improve their CVs.

!['image_app'](static/images/cvhelper_exmaple.png)

## Features

- **CV Analysis:** Analyzes a user's CV against a job description.
- **Scoring:** Provides a score out of 10, reflecting the CV's alignment with the job description.
- **Actionable Suggestions:** Gives 2-3 specific suggestions for improving the CV.
- **Conversational Interface:** Supports a natural, conversational interaction with the user.
- **Memory:** The chatbot remembers previous interactions and uses them to keep the conversation fluid and contextual.
- **Easy-to-use Streamlit Interface:** The chatbot is deployed using Streamlit, making it easy to use through your browser.

## Getting Started

### Prerequisites

- **Python 3.11+**
- **uv** - An extremely fast Python package manager written in Rust.
- **Git** - For version control.
- **A valid OpenAI API key:** You will need an API key to run the LLM, which should be defined in a `.env` file.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/achrafib1/CV-Helper
    cd CV-Helper # Replace 'your-repository' with 'CV-Helper'
    ```

2.  **Set up a virtual environment:** We recommend using virtual environments for your projects. Choose one of the following methods:

    - **Using Python's built-in `venv` (Cross-Platform):**

      ```bash
      python -m venv .venv
      ```

    - **Using `uv` (Cross-Platform):**
      ```bash
      uv venv
      ```

3.  **Activate the virtual environment and install dependencies:**

    - **Linux/macOS:**

      ```bash
      source .venv/bin/activate
      uv pip install -r requirements.txt
      ```

    - **Windows:**

      ```bash
      .venv\Scripts\activate
      uv pip install -r requirements.txt
      ```

    - **Verify installation:**
      ```bash
      uv pip check
      ```
    - **Ensure that the `requirements.txt` file exists at the root of your project and contains the list of all required dependencies.**

4.  **Set up a `.env` file:**

    - Create a `.env` file in the project root directory.
    - Add the model name you'd like to use like so:

      ```
      MODEL=gpt-4o-mini
      ```

    - Add your OpenAI API key to the file like so:
      ```
      OPENAI_API_KEY=sk-your-openai-api-key
      ```
      - Replace `sk-your-openai-api-key` with the API Key for your OpenAI account.

### Running the Application

1.  **Run the main app:**
    ```bash
    streamlit run app.py
    ```
    This will start the Streamlit application in your default web browser. You can interact with the chatbot from the interface.

## Contributing

Contributions to this project are welcome. Please follow these guidelines:

1.  **Fork:** Fork the repository.
2.  **Branch:** Create a feature branch for your contribution.
3.  **Commit:** Make your changes and commit them using clear, well-formatted messages.
4.  **Pull Request:** Submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
