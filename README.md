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
    cd CV-Helper
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

### Example Usage

**User Input:**

```
Here is the Job Description: We are looking for a skilled software engineer with 5+ years of experience in Python, a strong background in cloud technologies, and excellent communication skills. The ideal candidate will have experience with agile development methodologies and be a team player.

Here is my CV: John Doe
Software Engineer
Summary
A highly skilled software engineer with experience in developing and maintaining Python applications. Expert in Python, with a good understanding of cloud platforms such as AWS, and possess basic communication skills.

Experience
Software Engineer at Tech Solutions, 2018 – Present.
Developed and maintained several Python applications for cloud and on-premise deployment.

Education
Master of Science in Computer Science, University X, 2018.
Bachelor of Science in Computer Science, University X, 2016.
```

**Expected Bot Output (Example):**

```
I see that you've provided both your CV as a Software Engineer and the job description for the role you're interested in. Based on the information you've shared, here’s an analysis of how well your CV matches the job description:

Score: 5 out of 10.

Your CV demonstrates relevant experience, particularly in Python, but there are several areas for improvement:

1. Experience Requirement: The job description requires over five years of experience in software development, specifically mentioning Python. Your CV explicitly states experience in developing Python applications, which is good. However, it would be beneficial to highlight the exact number of years you have worked with Python, especially if it exceeds five years.

2. Cloud Technologies: While you mention a good understanding of cloud platforms like AWS, the job description emphasizes a strong background in cloud technologies. Provide specific examples of how you've utilized these cloud technologies in past projects to strengthen your application.

3. Communication Skills: The job seeks candidates with excellent communication skills. Your CV notes only basic communication skills. To align closely with the job description, you may want to illustrate experiences where you effectively communicated complex technical concepts to non-technical stakeholders or collaborated closely with team members.

Suggestions for Improvement:

1. Detail Your Experience: Specify the number of years you have worked with Python. For example, instead of saying "experience in developing Python applications," say "over 5 years of experience developing and maintaining Python applications, focusing on scalability and performance optimization."

2. Showcase Cloud Experience: If you have specific projects where you utilized AWS or other cloud technologies, clearly detail them. For instance, "Implemented a cloud-based solution on AWS that improved system reliability and reduced costs by 20%."

3. Enhance Communication Skills Section: Add concrete examples that demonstrate strong communication skills. You might say, "Presented project updates to stakeholders, ensuring clarity in technical discussions, which led to increased project understanding and stakeholder confidence."

By addressing these suggestions, you can create a more compelling CV that aligns better with the job description and enhances your candidacy for the software engineer position. Good luck with your application!
```

## Contributing

Contributions to this project are welcome. Please follow these guidelines:

1.  **Fork:** Fork the repository.
2.  **Branch:** Create a feature branch for your contribution.
3.  **Commit:** Make your changes and commit them using clear, well-formatted messages.
4.  **Pull Request:** Submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
