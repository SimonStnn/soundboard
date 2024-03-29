# Soundboard

This Python-based soundboard project allows you to play audio through your microphone, creating a customizable and interactive soundboard experience. Easily trigger your favorite sounds or effects in real-time during virtual meetings, live streams, or casual conversations.

## Table of contents

- [Soundboard](#soundboard)
  - [Table of contents](#table-of-contents)
  - [🚀 Get started](#-get-started)
    - [Downloading the program](#downloading-the-program)
      - [Download from release](#download-from-release)
      - [Clone the project](#clone-the-project)
    - [Config](#config)
      - [Manually](#manually)
      - [Automatically](#automatically)
    - [Installing a virtual cable](#installing-a-virtual-cable)
  - [Add audio](#add-audio)

## 🚀 Get started

### Downloading the program

To download the soundboard you can either [download from the latest release](#download-from-release) or [clone the project](#clone-the-project). For most users [downloading from the latest release](#download-from-release) is recommended.

#### Download from release

To get started download the [`soundboard.zip`](https://github.com/SimonStnn/soundboard/releases/latest/download/soundboard.zip) file from the latest release. After downloading, unzip the file and run `soundboard.exe`.

#### Clone the project

Clone the project.

```bash
git clone https://github.com/SimonStnn/soundboard.git
cd soundboard
```

Set up venv (optional)

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install requirements

```bash
pip install -r requirements.txt
```

Build the exe

```bash
pyinstaller --distpath . --name soundboard --icon .\images\icon.ico --windowed --onefile .\src\main.py
```

### Config

You can customize the soundboard to your liking in the config. If you want to keep the default, you can ignore this section and skip to [Installing a virtual cable](#installing-a-virtual-cable).

#### Manually

To manually make the config, rename `config.yaml.template` to `config.yaml` and you're good to go! You can change the values in the config to your liking.

#### Automatically

A copy of the `config.yaml.template` will be made the first time you run the program. Once the `config.yaml` file is made you can make changes and customize the soundboard.

### Installing a virtual cable

To play the audio trough the microphone you'll need a virtual cable. You can do this at [VB-audio](https://vb-audio.com/Cable/) or with any other virtual cable software.

> Follow the instructions on the website to setup your virtual cable.

## Add audio

You can add your own audio files to the `audio` folder. After adding them you may need to restart the program so they are loaded correctly.

---

> Thank you for using my soundboard. 😄
