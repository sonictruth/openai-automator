# macOS OpenAI Automator 🤖

- A script for Mac Automator that allows you to perform spell checks or other text-related tasks within any application on Mac OS. 
- Availible prompts:
    - apellcheck: English spellchecker
    - coding: Code generation
    - genz: Translate english to GenZ
    - enfr: Translate English to French.


## Install:

- Ensure that you have Python 3 installed.
- Check out this project using Git in your home directory.
- Rename .env.example to .env and add your OpenAI API key.
- Add OpenAI.workflow to Automator.
- Recommended service Keyboard Shortcut: Shift + Ctrl + Z
- The project contains three prompts. The default prompt is spellcheck 
- To use other prompts, start the selected text with the name of the prompt.
  Example: select the text following text: 
  _[genz] Hello world, how are you ?_
  and press the shortcut keys. 
  The text will be replaced by _Heyyy world, wassup? How ya vibin'? 😎🌍🤙_

<img src="workflow.png" width="200">
