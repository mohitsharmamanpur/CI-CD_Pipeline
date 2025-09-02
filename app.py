from flask import Flask

app = Flask(__name__)

@app.route('/info')
def home():
    return '''
        <html>
            <head>
                <title>About Me - Mohit Sharma</title>
                <style>
                    body { 
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                        background: linear-gradient(to right, #6a11cb, #2575fc); 
                        margin: 0; 
                        padding: 0; 
                        display: flex; 
                        justify-content: center; 
                        align-items: center; 
                        height: 100vh;
                    }
                    .card {
                        background: white;
                        padding: 40px;
                        border-radius: 20px;
                        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
                        max-width: 600px;
                        text-align: center;
                        transition: transform 0.3s;
                    }
                    .card:hover {
                        transform: scale(1.05);
                    }
                    h1 { color: #2c3e50; margin-bottom: 10px; }
                    h2 { color: #555; font-weight: 400; margin-top: 0; margin-bottom: 20px; }
                    p { font-size: 18px; line-height: 1.8; color: #444; }
                    .highlight { color: #2575fc; font-weight: bold; }
                    .footer { margin-top: 25px; }
                    .btn {
                        text-decoration: none;
                        background: #2575fc;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 8px;
                        font-size: 16px;
                        margin: 5px;
                        display: inline-block;
                        transition: background 0.3s;
                    }
                    .btn:hover { background: #6a11cb; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1> Hi, I'm <span class="highlight">Mohit Sharma</span></h1>
                    <h2>B.Tech Student | DevOps & Cloud Enthusiast</h2>
                    <p><b>College:</b> Swami Keshvanand Institute of Technology, Jaipur</p>
                    <p><b>Interests:</b> DevOps, Cloud Computing, AI, ML</p>
                    <p><b>About Me:</b> I am passionate about technology, automation, and solving real-world problems.</p>
                    <div class="footer">
                        <a href="https://github.com/" class="btn">GitHub</a>
                        <a href="https://linkedin.com/" class="btn">LinkedIn</a>
                        <a href="mailto:yourmail@example.com" class="btn">Contact Me</a>
                    </div>
                </div>
            </body>
        </html>
    '''

if __name__ == '__main__':
    # Unique port number (5006)
    app.run(host='0.0.0.0', port=5006)
