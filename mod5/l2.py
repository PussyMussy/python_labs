from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, NumberRange
import subprocess
import shlex

app = Flask(__name__)

class Form(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    timeout = FloatField('Timeout', validators=[DataRequired(), NumberRange(min=0.1, max=30)])

@app.route('/execute', methods=['POST'])
def execute_code():
    form = Form(request.form)
    if not form.validate():
        return jsonify({'error': 'Invalid input'}), 400

    code = form.code.data
    timeout = form.timeout.data

    if 'shell=True' in code:
        return jsonify({'error': 'Unsafe code detected'}), 400

    cmd = f'python -c "{code}"'
    
    try:
        result = subprocess.run(shlex.split(cmd), timeout=timeout, capture_output=True, text=True)
        return jsonify({'output': result.stdout.strip(), 'error': result.stderr.strip()}), 200
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Execution timed out'}), 408
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)