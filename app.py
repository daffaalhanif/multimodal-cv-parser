import gradio as gr
from parser.multimodal_parser import parse_cv, encode_image
from pdf2image import convert_from_path

def change_pdf(files):
    masuk = []
    
    for file in files:
        filename = file.name.lower()
        
        if filename.endswith(".pdf"):
            file_pdf = convert_from_path(file.name)
        
            for i, halaman in enumerate(file_pdf):
                temp_path = f"sementara_page_{i}.png"
                halaman.save(temp_path, "PNG")
                masuk.append(encode_image(temp_path))
        
        elif filename.endswith((".png", ".jpg", ".jpeg")):
            masuk.append(encode_image(file.name))
            
    hasil = parse_cv(masuk)
    return hasil.model_dump()

with gr.Blocks() as demo:
    gr.Markdown("# CV detetction system")
    gr.Markdown("## deteksi cv dri pdf atau image")
    gr.Markdown("Upload file")
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                file_types=["image", ".pdf"],
                file_count="multiple",
                label="Upload CV"
                )
            ocr_btn = gr.Button("Anaalisis cv")
        with gr.Column():
            output_ocr = gr.JSON()
    
    ocr_btn.click(
        fn=change_pdf,
        inputs=file_input,
        outputs=output_ocr
    )
demo.launch()