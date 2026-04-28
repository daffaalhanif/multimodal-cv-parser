import gradio as gr

from utils.file_handler import load_file
from parser.multimodal_parser import parse_cv
from parser.validator import validate


def process_cv(files):
    """Proses file CV yang diupload dan return hasil parsing sebagai JSON.

    Args:
        files: List file yang diupload dari Gradio.

    Returns:
        Dict hasil parsing CV yang sudah tervalidasi.
    
    Raises:
        json.JSONDecodeError: Jika model mengembalikan JSON yang tidak valid.
        ValueError: Jika output tidak sesuai schema CVOutput.
    """
    masuk = []

    for file in files:
        images = load_file(file.name)
        masuk.extend(images)

    raw_dict = parse_cv(masuk)
    hasil = validate(raw_dict)
    return hasil.model_dump()


with gr.Blocks() as demo:
    gr.Markdown("# CV Detection System")
    gr.Markdown("## Deteksi CV dari PDF atau Image")
    gr.Markdown("Upload file CV kamu di bawah ini")

    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                file_types=["image", ".pdf"],
                file_count="multiple",
                label="Upload CV"
            )
            ocr_btn = gr.Button("Analisis CV")
        with gr.Column():
            output_ocr = gr.JSON()

    ocr_btn.click(
        fn=process_cv,
        inputs=file_input,
        outputs=output_ocr
    )

demo.launch()