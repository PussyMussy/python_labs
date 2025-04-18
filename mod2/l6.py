from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/preview/<int:size>/<path:relative_path>')
def preview_file(size, relative_path):
    abs_path = os.path.abspath(relative_path)
    
    if not os.path.isfile(abs_path):
        return Response("Файл не найден.", status=404)

    with open(abs_path, 'r', encoding='utf-8') as file:
        result_text = file.read(size)
    
    result_size = len(result_text)

    response_html = f"""
    <html>
        <body>
            <p><strong>{abs_path}</strong> {result_size}</p>
            <p>{result_text}</p>
        </body>
    </html>
    """
    
    return Response(response_html, content_type='text/html')

if __name__ == '__main__':
    app.run(debug=True)