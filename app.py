from flask import Flask, request, render_template, send_file, url_for
import subprocess
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    scan_type = request.form['scan_type']
    app.logger.debug(f"Received URL: {url} for scan type: {scan_type}")

    if scan_type == 'medium':
        script = 'web_scan.py'
        result_template = 'result.html'
    else:  # Assuming 'deep' scan type
        script = 'web_scan2.py'
        result_template = 'result2.html'
    
    try:
        result = subprocess.run(['python3', script, url], capture_output=True, text=True)
        app.logger.debug(f"Subprocess result: {result.stdout}")
        if result.returncode != 0:
            app.logger.error(f"Error: {result.stderr}")
            return render_template(result_template, result=f"Error: {result.stderr}")

        report_path = os.path.join(os.getcwd(), 'SA-Vulnerability-Report')
        return render_template(result_template, result=result.stdout, report_url=url_for('download_report'))
    except Exception as e:
        app.logger.error(f"Exception: {str(e)}")
        return render_template(result_template, result=f"Exception: {str(e)}")

@app.route('/download')
def download_report():
    report_path = os.path.join(os.getcwd(), 'SA-Vulnerability-Report')
    return send_file(report_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
