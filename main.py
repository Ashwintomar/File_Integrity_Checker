import gradio as gr
import os
from file_manager import load_file_hashes, save_file_hashes, get_file_size, create_hash_result
from hash_utils import HASH_FUNCTIONS
from verify_file import verify_file_integrity

def upload_file(files) -> str:
    file_hashes = load_file_hashes()
    results = []

    for file in files:
        file_name = os.path.basename(file.name)
        file_path = file.name
        if not os.path.exists(file_path):
            results.append(f"Error: '{file_name}' not found.")
            continue
        
        # Calculate all hashes
        current_hashes = {
            name: func(file_path) 
            for name, func in HASH_FUNCTIONS.items()
        }
        
        current_hashes["size"] = get_file_size(file_path)
        file_hashes[file_name] = current_hashes
        
        # Format results
        hash_results = [
            create_hash_result(current_hashes, algorithm)
            for algorithm in HASH_FUNCTIONS.keys()
        ]
        results.append(f"File: {file_name}\n" + "\n".join(hash_results))

    save_file_hashes(file_hashes)
    return "\n\n".join(results)

def list_files() -> str:
    file_hashes = load_file_hashes()
    if not file_hashes:
        return "No files in the system."

    result = []
    for file, data in file_hashes.items():
        file_info = [f"File: {file} ({data['size']} bytes)"]
        for algorithm in HASH_FUNCTIONS.keys():
            if algorithm in data:
                file_info.append(f"{algorithm.upper()}: {data[algorithm]}")
        result.append("\n".join(file_info))
    
    return "\n\n".join(result)

# Rest of the Gradio interface remains the same
with gr.Blocks() as app:
    gr.Markdown("# Enhanced File Integrity System")
    
    with gr.Tab("Upload Files"):
        file_input = gr.File(file_count="multiple", label="Upload Files")
        upload_button = gr.Button("Upload and Calculate Hashes")
        upload_output = gr.Textbox(label="Upload Results", max_lines=20)
        upload_button.click(upload_file, inputs=file_input, outputs=upload_output)
    
    with gr.Tab("Verify File"):
        verify_input = gr.File(label="Select File to Verify")
        verify_button = gr.Button("Verify File Integrity")
        verify_output = gr.Textbox(label="Verification Result")
        verify_button.click(verify_file_integrity, inputs=verify_input, outputs=verify_output)
    
    with gr.Tab("List Files"):
        list_button = gr.Button("List All Files")
        list_output = gr.Textbox(label="Files in System", max_lines=20)
        list_button.click(list_files, outputs=list_output)

if __name__ == "__main__":
    app.launch(share=True)