# whai1
Why Would You Use AI For This? - Conspiracy Theory Generator

## Prep
I developed and testing on Python 3.13.5. I didn't test with other versions so try to aim for something close to that to avoid surprises.

Install the dependencies (in a virtual env or not)

```sh
pip install -r requirements.txt
```

Add your generative AI provider config and API key to **config.yaml**.

## Run

At a command line within the source directory:

```sh
python main.py
```

Alternatively if your shell supports shebang scripts:

```sh
chmod +x main.py
./main.py
```

There's no input commands. It's just an interactive command line program. You can force-quit the program or use the post-generation prompt to exit.

## Notes

The program only supports the **gemini** provider currently. I've left the door open to add others as I learn about their APIs.

You may adjust the "tone" of the conspiracy theories using the "MAGIC_WORDS" array at the top of **main.py**. Try not to get too dark with it.
