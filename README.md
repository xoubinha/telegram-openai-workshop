# telegram-oai-workshop
Demonstration project that creates a Telegram bot that connects to Open AI.

## Repository Overview

This repository contains various demonstration projects related to the workshop titled "Revolucionando Telegram: Creando bots inteligentes con OpenAI". Each project demonstrates a different aspect of creating intelligent Telegram bots using OpenAI models and Python libraries. The information about the workshop is the following:

- **Talk Title:** Revolucionando Telegram: Creando bots inteligentes con OpenAI
- **Date and Time:** 30/12/23, 16:30–17:15 (Europe/London)
- **Location:** Santiago de Compostela, Spain
- **Language:** Español
- **Description:**

Are you tired of reading long messages or listening to endless voice notes on Telegram? Imagine having a bot that could transcribe them quickly with minimal errors and provide you with summaries of the most important points of the conversation. Well, it's possible, and in this talk, we'll show you how from start to finish!

In this session, we will develop a Telegram bot step by step using the latest OpenAI models and Python libraries for Telegram. You don't need to be an AI expert; we will guide you every step of the way, providing practical tips to make the most of these models.

If you want to learn how to take your Telegram bots to the next level, this is the talk for you. Don't miss the opportunity to be part of this exciting evolution in artificial intelligence and messaging! We look forward to seeing you!


## Prerequisites

- Python 3.9
- Telegram Bot API token (can be obtained from the [BotFather](https://telegram.me/BotFather))
- OpenAI API key (can be obtained from [OpenAI](https://platform.openai.com/))

## Project List

1. **Basic Telegram Bot (Telebot Demo)** - This demo serves as an introductory guide to building a basic Telegram bot. It lays the foundation for understanding how to create more advanced bots that leverage OpenAI models.  You will learn how to set up a bot, handle user interactions, and respond to messages using pyTelegramBotAPI Python library.

    **Telebot demo features**
    - Helps to show the basic elements of a Telegram bot build with Python.

2. **OpenAI demo** - This demo serves to see how we can build an intelligent model making use of OpenAI's GPT models and Langchain.

    **OpenAI demo features**
    - Open AI interaction.
    - Convenient and user-friendly Telegram bot interface.

3. **Voice demo** - This demo serves to see how we can interact both with OpenAI GPT models and Whisper.

    **Voice demo features**
    - Transcribe audio files (up to 25MB) received through Telegram in source language.
    - Support for various audio formats (m4a, mp3, mp4, mpeg, mpga, wav, webm).
    - Accurate transcription results using the Whisper open-source model.
    - Interaction with OpenAI.
    - Convenient and user-friendly Telegram bot interface.

## Project Structure

- `telebot_demo.py`: The main Python script containing the bot's logic.
- `openai_demo.py`: The main Python script containing the bot's logic that conversates using OpenAI
- `voice_demo.py`: The main Python script containing the bot's logic that handles voice messages.

## Getting Started

### Check and update Python version

Ensuring you have the correct Python version is crucial for compatibility.

1. **Open Terminal or Command Prompt**:
   - Windows: Press `Win + R`, type `cmd`, and hit Enter.
   - macOS/Linux: Open the Terminal app.

2. **Check Python Version**: 
   - Type `python --version` or `python3 --version` and press Enter.
   - This command will display your installed Python version (e.g., Python 3.9).

If your Python version is less than 3.9, you must update it. The update process can vary significantly between operating systems, visit the [Python Downloads Page](https://www.python.org/downloads/) for official release information.

### Installation

> To set up our environment, we will be using Conda. If you haven't installed Conda already, we suggest doing so as it simplifies package management and deployment. Conda can be installed as part of the Anaconda or Miniconda distribution. For installation instructions, please refer to the [official Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

To activate an Anaconda environment in your project, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the root directory of your project.
3. Create the Anaconda environment by running the following command:

```bash
conda env create -f environment.yml
```

4. Once the environment is created, activate it using the following command:

```bash
conda activate <environment-name>
```

By following these steps, you'll be able to activate your Anaconda environment and ensure that all the necessary packages are available for your project.

### Setting up environment variables

Before obtaining your API keys, it's important to set up a way to securely store and manage these keys. In this project, we use environment variables to handle sensitive information like API keys. You will need to create a `.env` file in the root directory of your project to store your tokens and keys. Add the following variables to this file:

```bash
BOT_TOKEN=<'your-telegram-bot-token'>
OPENAI_API_KEY=<'your-open-ai-api-key'>
```

> You can refer to the `.env.template` file in the project as a guide for creating your `.env` file.

#### Explanation

- **BOT_TOKEN**: The bot token of your bot.
- **OPENAI_API_KEY**: The open AI API key.

Ensure to replace `<your-telegram-bot-token>` and `<your-open-ai-api-key>` with the actual values you will obtain following the instructions in the next sections.

It's crucial to keep these environment variables secure. Do not share your `.env` file publicly or commit it to version control. We will use `python-dotenv` to load these environment variables into your project.

### Obtaining a Telegram Bot API Token

To start building your own Telegram bot, the first step is to obtain an API token, which is a unique identifier for your bot. This token allows your bot to communicate with the Telegram API. Here’s a step-by-step guide:

1. **Access BotFather**: Open the [Telegram app](https://web.telegram.org), log in and search for the [BotFather](https://telegram.me/BotFather), which is the official bot for creating other bots on Telegram.

2. **Start a conversation**: Once you find the BotFather, start a conversation with it by clicking the “Start” button.

3. **Create a new bot**: Type `/newbot` and send it as a message to the BotFather. This command initiates the process of creating a new bot.

4. **Set a name for your bot**: You need to set a unique username for your bot. This username must end in bot (e.g., mytestbot or example_bot).

Once the username is approved, the BotFather will provide you with your bot's API token. This token is a long string of letters and numbers. Keep it secure and do not share it with others, you will need this token when you are setting up your bot in your code.

### Obtaining an OpenAI API Key

Since you're looking to integrate OpenAI's capabilities into your application, you'll need an API key. This key serves as a unique identifier and token for authentication, allowing you to make requests to OpenAI's API. Here is how you can obtain it:

1. **Visit OpenAI**: Go to [OpenAI Platform](https://platform.openai.com/).

2. **Sign up or log in**: Create an account if you don't have one, or log in if you do.

3. **Navigate to the API section**: Once logged in, find the section related to API keys, typically in the dashboard or under a tab like “API” or “Developer”.

4. **Create a new API Key**: Look for an option to create a new API key, often labeled “Create new secret key”.

Once you submit the key name, the platform will generate a new API key. Copy it and keep it secure.

### Test locally

To test any of the demos locally, follow these steps:

1. Open a terminal or command prompt and navigate to the `src` folder.
2. In the terminal, execute the following command to start the bot:

```bash
python -m demos.<your-demo-bot-file>
```

This file is responsible for running the bot. 
3. Once the bot is running, open the Telegram app on your device. 
4. Search for your bot by its username or the name you provided during the bot creation process. 
5. Open a chat with the bot and interact with it!

### Deployment
Coming soon!

## Contributors
- [Sara](https://twitter.com/sara_sanluis)
- [Christian](https://twitter.com/ccarballolozano)

If you'd like to contribute to this repository by adding more demo projects or improving existing ones, feel free to fork the repository, make your changes, and submit a pull request. We welcome contributions from the community!

- Fork the repository.
- Create a new branch.
- Make your changes.
- Test your changes.
- Commit your changes and push them to your fork.
- Submit a pull request explaining your changes.

## Disclaimer

This project is provided as-is with no warranty or guarantee of its performance or results. Use at your own risk.

## Relevant Links
- https://core.telegram.org/bots
- https://pypi.org/project/pyTelegramBotAPI/
- https://github.com/eternnoir/pyTelegramBotAPI/tree/master
- https://api.python.langchain.com/en/latest/api_reference.html
