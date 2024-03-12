# Chatbot Streamlit App

This repository contains a Streamlit web application for running a chatbot. The chatbot is powered by the `langchain` library and offers various functionalities.

## Installation

To set up the environment and install the required dependencies, follow these steps:

1. Make sure you have Python 3.9 and Pipenv installed on your system.

2. Clone this repository to your local machine.

3. Navigate to the project directory in your terminal.

4. Run the following command to create a Pipenv environment and install the required dependencies:

    ```
    pipenv install
    ```

    This will create a virtual environment and install all the necessary packages listed in the `requirements.txt` file.

## Running the App

Once you have installed the dependencies, you can run the Streamlit app using the following command:

    
    pipenv run streamlit run main.py



This will start the Streamlit server, and you can access the app through your web browser at the provided URL.

## Dependencies

The app relies on the following Python libraries:

- `langchain==0.0.154`: Library for language processing tasks.
- `PyPDF2==3.0.1`: Library for PDF manipulation.
- `python-dotenv==1.0.0`: Library for managing environment variables.
- `streamlit==1.18.1`: Library for building interactive web apps.
- `faiss-cpu==1.7.4`: Library for efficient similarity search.
- `streamlit-extras`: Additional Streamlit components and utilities.

  you can install the required dependencies by run this command
```
  pipenv install -r requirements.txt
```


  

## Usage

Once the app is running, you can interact with the chatbot through the provided interface. Explore the various features and functionalities offered by the chatbot.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



    
    

