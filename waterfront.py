import gradio as gr

from modules import shared, scripts


def create_ui():
    import modules.ui
    with gr.Group():
        with gr.Accordion("Large Scale Generation", open = False):
            with gr.Row():
                enabled = gr.Checkbox(label='Enable Large Scale Generation', value=False)
            with gr.Row():
                sampling_step_min =  gr.Textbox(label="Sampling Step Min", placeholder="Sampling Step Min", value="1")
                sampling_step_max = gr.Textbox(label="Sampling Step Max", placeholder="Sampling Step Max", value="150")
                sampling_step_gap = gr.Textbox(label="Sampling Step Gap", placeholder="Sampling Step Gap", value="1")
            with gr.Row():
                hr_step_min =  gr.Textbox(label="Hires Step Min", placeholder="Hires Step Min", value="1")
                hr_step_max = gr.Textbox(label="Hires Step Max", placeholder="Hires Step Max", value="150")
                hr_step_gap = gr.Textbox(label="Hires Step Gap", placeholder="Hires Step Gap", value="1")
            with gr.Row():
                CFG_step_min =  gr.Textbox(label="CFG Step Min", placeholder="CFG Step Min", value="1")
                CFG_step_max = gr.Textbox(label="CFG Step Max", placeholder="CFG Step Max", value="30")
                CFG_step_gap = gr.Textbox(label="CFG Step Gap", placeholder="CFG Step Gap", value="1")
    return enabled, sampling_step_min, sampling_step_max, sampling_step_gap, hr_step_min, hr_step_max, hr_step_gap, CFG_step_min, CFG_step_max, CFG_step_gap

