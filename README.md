# flan-t5-large-gradio
A gradio frontend for [Google's Flan-T5 Large](https://huggingface.co/google/flan-t5-large) language model, can also be adjusted for other sizes.

## To run:

Install the dependencies: gradio, transformers, sentencepiece
Optionally also install: accelerate

Run with: `python flan-t5-large-gradio.py`
Optionally run with: `accelerate launch flan-t5-large-gradio.py`

## To use other size models

Modify lines 4-6, comment/uncomment to select a different model. Note that each model has different requirements for storage/RAM, the code as presently configured assumes sufficient RAM to load the entire model.
