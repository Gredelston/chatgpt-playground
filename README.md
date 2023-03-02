# ChatGPT Playground

Welcome to ChatGPT Playground! This repository provides a platform for
experimenting with OpenAI's cutting-edge natural language processing API,
ChatGPT. I've written some scripts and helpful libraries, and I hope that they
will help you write your own ChatGPT-empowered tools.

I encourage you to join the growing community of developers using OpenAI's
language models to build cutting-edge chatbots, human-like assistants, and much
more. With this playground, you can quickly and easily familiarize yourself with
the possibilities available to you with ChatGPT.

## Getting Started

1.  Install prerequisites:
    1.  `sudo apt get python3.10`
    1.  `python3.10 -m pip install openai`
1.  Clone this repository to your local filesystem.
1.  Generate an OpenAI API key by following the instructions on the [OpenAI
    website](https://openai.com/platform/). This will require you to create an
    OpenAI account and to set up billing.
1.  Create a file in the root of this repository called `secret.txt`. In that
    file, paste your OpenAI API key, and nothing else.
1.  Try running `nira.py` to open an interactive ChatGPT chat session!

## Usage

The `chatgpt-playground` repository contains a few code examples that
demonstrate different use cases of the ChatGPT API. You can modify the examples
to see how the API responds to different input, or develop your own code to test
different concepts.

*   `nira.py`: An interactive session with Nira, my personal assistant. To exit
    the session, just press ENTER with an empty prompt.
*   `what_does_this_file_do.py`: Reads a file from your filesystem, and asks
    ChatGPT what that file does. This is an exploration into an API tool's
    ability to inspect your filesystem, which the web UI cannot do.

## Contributions

I welcome contributions from all developers, whether you're an experienced
software engineer or just getting started. If you have ideas for new example
code, or have found a bug that needs fixing, please don't hesitate to submit a
pull request.

Happy coding!

## Example Images

![Example usage of `nira.py`, showing an interactive chat session.](./images/nira.png)

![Example usage of `what_does_this_file_do.py`, showing ChatGPT describing what a local file does.](./images/what_does_this_file_do.png)
