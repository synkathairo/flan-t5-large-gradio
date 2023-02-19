# flan-t5-large-gradio
A [gradio](https://gradio.app/) frontend for [Google's Flan-T5 Large](https://huggingface.co/google/flan-t5-large) language model, can also be adjusted for other sizes.

The gradio frontend runs in the browser, and displays a chat-like interface for interacting with the language model.

## To run:

Install the dependencies: gradio, transformers, sentencepiece

Recommended to install: safetensors

Optionally also install: accelerate

Run with: `python flan-t5-large-gradio.py`

Optionally run with: `accelerate launch flan-t5-large-gradio.py`
(this may or may not speed up your execution)

## To use other size models

Modify lines 4-6, comment/uncomment to select a different model. Note that each model has different requirements for storage/RAM, the code as presently configured assumes sufficient RAM to load the entire model.

Additional info on loading large models is on the [Hugging Face website](https://huggingface.co/blog/accelerate-large-models), see [also](https://huggingface.co/docs/accelerate/v0.11.0/en/big_modeling)

