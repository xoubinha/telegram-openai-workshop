# telegram-oai-workshop
Demonstration project that creates a Telegram bot that connects to Open AI.

## Repository Overview

This repository contains various demonstration projects related to the workshop titled "Revolucionando Telegram: Creando bots inteligentes con OpenAI". Each project demonstrates a different aspect of creating intelligent Telegram bots using OpenAI models and Python libraries.

Are you tired of reading long messages or listening to endless voice notes on Telegram? Imagine having a bot that could transcribe them quickly with minimal errors and provide you with summaries of the most important points of the conversation. Well, it's possible, and in this talk, we'll show you how from start to finish!

In this session, we will develop a Telegram bot step by step using the latest OpenAI models and Python libraries for Telegram. You don't need to be an AI expert; we will guide you every step of the way, providing practical tips to make the most of these models.

If you want to learn how to take your Telegram bots to the next level, this is the talk for you. Don't miss the opportunity to be part of this exciting evolution in artificial intelligence and messaging! We look forward to seeing you!


## Prerequisites

- Python 3.9
- Telegram Bot API token (can be obtained from the BotFather)
- OpenAI API key (can be obtained from [OpenAI](https://platform.openai.com/))

### Project List

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


### Project Structure

- `telebot_demo.py`: The main Python script containing the bot's logic.
- `openai_demo.py`: The main Python script containing the bot's logic that conversates using OpenAI
- `voice_demo.py`: The main Python script containing the bot's logic that handles voice messages.


## Getting Started
### Installation

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

### Telegram bot

To be able to create the Telegram Bot, you need to obtain a Telegram Bot token, to do so, follow these steps:

1. Download and install the Telegram app on your device if you haven't already.
2. Open the Telegram app and search for the "BotFather" bot. This is the official bot provided by Telegram to create and manage bots.
3. Start a chat with the BotFather by typing `/newbot` and follow the prompts to set up a new bot.
4. Follow the instructions provided by the BotFather to create a new bot. You will be asked to provide a name and a username for your bot.
5. Once you've provided the necessary information, the BotFather will generate a token for your bot. This token is a unique identifier that you'll need to interact with the Telegram Bot API.
6. Copy the generated token and store it securely. This token serves as an authentication mechanism for your bot to communicate with the Telegram API.
7. You can now use the obtained token to interact with the Telegram Bot API and implement your bot's functionality. Add it to you `.env` file.


### Environment variables

In order to configure and run this project, you need to set up the following environment variables. Create a `.env` file in the root directory of your project and add these variables with their corresponding values:

```bash
BOT_TOKEN=<'your-telegram-bot-token'>
OPENAI_API_KEY=<'open-ai-api-key'>
```

#### Explanation of Environment Variables

- **BOT_TOKEN**: The bot token of your bot.
- **OPENAI_API_KEY**: The open AI API key.

Make sure to replace the placeholder values with your actual configuration. It's essential to keep your environment variables secure. Do not share your .env file publicly or commit it to version control. To load these environment variables into your project, `python-dotenv` will be used. Please ensure you have the appropriate values set in your .env file before running the project to avoid any configuration-related issues.

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