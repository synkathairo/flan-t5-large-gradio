from transformers import T5Tokenizer, T5ForConditionalGeneration
import gradio as gr

# model_name = "google/flan-t5-small"
# model_name = "google/flan-t5-base"
model_name = "google/flan-t5-large"
# model_name = "google/flan-t5-xl"

default_max_length = 200

print("Using `{}`.".format(model_name))

tokenizer = T5Tokenizer.from_pretrained(model_name)
print("T5Tokenizer loaded from pretrained.")

model = T5ForConditionalGeneration.from_pretrained(model_name, device_map="auto")
print("T5ForConditionalGeneration loaded from pretrained.")


def inference(max_length, input_text, history=[]):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=max_length, bos_token_id=0)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    history.append((input_text, result))
    return history, history


with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown(
            "<h1>Demo of {}</h1><p>See more at Hugging Face: <a href='https://huggingface.co/{}'>{}</a>.</p>".format(
                model_name, model_name, model_name
            )
        )
        max_length = gr.Number(
            value=default_max_length, label="maximum length of response"
        )

    chatbot = gr.Chatbot(label=model_name)
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(
            show_label=False, placeholder="Enter text and press enter"
        ).style(container=False)

    txt.submit(fn=inference, inputs=[max_length, txt, state], outputs=[chatbot, state])

demo.launch()
