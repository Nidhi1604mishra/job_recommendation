import gradio as gr 
from recommendor import recommend_jobs
from file_reader import extract_text_from_file
from history_server import save_user_history, get_user_history



def process_resume_file(file):
    text = extract_text_from_file(file)
    recommendations = recommend_jobs(text)
    save_user_history(text, recommendations)
    return gr.update(value=recommendations, visible=True)
    
def handle_show_history():
    return gr.update(value=get_user_history(), visible=True)

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 💼 Smart Job Recommendation System")
    gr.Markdown("Upload your resume and get job recommendations based on your skills 🚀")

    with gr.Row():
        file_input = gr.File(label="Upload Resume (PDF or DOCX)", file_types=[".pdf", ".docx"])
    
    with gr.Row():
        submit_btn = gr.Button("🔍 Get Recommendations")
    
    match_output = gr.Textbox(
        label="🎯 Top Job Matches",
        lines=10,
        visible=False
    )
    
    gr.Markdown("---")

    with gr.Row():
        history_btn = gr.Button("📜 Show Past Resume Uploads")
    
    with gr.Accordion("🕓 Your Resume Upload History", open=False):
        history_output = gr.Textbox(
            label="Previous Recommendations",
            lines=15,
            visible=False
        )

    # Button click actions
    submit_btn.click(fn=process_resume_file, inputs=[file_input], outputs=[match_output])
    history_btn.click(fn=handle_show_history, inputs=[], outputs=[history_output])

demo.launch()

# iface = gr.Interface(
#     fn=process_resume_file,
#     inputs = gr.File(label="Upload your resume (PDF or DOCX)", file_types=[".pdf", ".docx"]),
#     outputs = gr.Textbox(label="Top Job matches"),
#     title = "Smart Job recommendation System",
#     description = "Upload your resume and get the best matching job roles based on skills",
# )

# iface.launch()