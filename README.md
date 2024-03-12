README.md
Chatbot App with Streamlit
This is a simple chatbot application built using Streamlit. It leverages various libraries to enhance its functionality.

Setup
Clone this repository to your local machine.

bash
Copy code
git clone <repository_url>
Navigate to the project directory.

bash
Copy code
cd <project_directory>
Install pipenv if you haven't already.

bash
Copy code
pip install pipenv
Create a virtual environment and install the required dependencies.

bash
Copy code
pipenv install -r requirements.txt
Running the App
Once the setup is complete, you can run the Streamlit app using the following command:

bash
Copy code
pipenv run streamlit run main.py
This will start the Streamlit server and open the app in your default web browser.

Requirements
Make sure you have the following packages installed in your environment:

langchain==0.0.154
PyPDF2==3.0.1
python-dotenv==1.0.0
streamlit==1.18.1
faiss-cpu==1.7.4
streamlit-extras
These packages can be installed using pipenv as mentioned in the setup section.

Usage
Upon running the Streamlit app, you will be presented with a chat interface.
Interact with the chatbot by typing your queries and pressing Enter.
The chatbot will respond accordingly based on its configured logic.
Additional Notes
Feel free to customize the chatbot's functionality by modifying the main.py file.
Explore further features and extensions provided by Streamlit to enhance the user experience.
For any issues or suggestions, please open an issue in the repository or contact the project maintainers.
Enjoy chatting with the bot! 🤖🚀
