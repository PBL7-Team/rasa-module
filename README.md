# Rasa Chatbot Project

This repository contains a Rasa chatbot project for building conversational AI.

## Requirements

- Python 3.9.13
- Rasa 3.0.3
- Other dependencies (see `requirements.txt`)

## Installation

1. Install Python 3.9.13:

   ```bash
   # Using pyenv
   pyenv install 3.9.13
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   # On macOS/Linux
   source venv/bin/activate

   # On Windows
   .\venv\Scripts\activate
   ```

4. Install Rasa and other dependencies:

   ```bash
   pip install rasa==3.0.3
   pip install -r requirements.txt
   ```

## Usage

1. Train the Rasa model:

   ```bash
   rasa train
   ```

2. Test the trained model:

   ```bash
   rasa test
   ```

3. Run the Rasa server:

   ```bash
   rasa run
   ```

4. Interact with the chatbot via Rasa shell:

   ```bash
   rasa shell
   ```

5. Integrate the chatbot with your application using Rasa REST API.

For more information on how to use Rasa, refer to the [official documentation](https://rasa.com/docs/rasa).
