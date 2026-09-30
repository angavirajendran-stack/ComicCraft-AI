from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="ComicCraftAI")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ComicCraftAI - AI Comic Generator</title>
    <link rel="icon" href="data:;base64,iVBORw0KGgo=">
    <style>
    body{font-family:Arial,sans-serif;background:#0f0f0f;color:white;padding:20px;margin:0}
    .container{max-width:800px;margin:40px auto;background:#1e1e1e;padding:30px;border-radius:15px;box-shadow:0 10px 30px rgba(0,0,0,0.5)}
    h1{color:#ff6b00;text-align:center;font-size:32px}
    p.subtitle{text-align:center;color:#aaa;margin-bottom:20px}
    .badges{text-align:center;margin-bottom:15px}
    .badge{display:inline-block;background:#2a2a2a;border:1px solid #444;padding:6px 14px;border-radius:20px;margin:5px;font-size:13px}
    textarea{width:100%;height:120px;padding:15px;border-radius:10px;background:#2a2a2a;color:white;border:1px solid #444;font-size:16px;box-sizing:border-box}
    button{width:100%;padding:15px;background:linear-gradient(90deg,#ff6b00,#ff8533);color:white;border:none;border-radius:10px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:15px}
    button:hover{opacity:0.9}
    .panel{margin-top:20px;background:#2a2a2a;padding:15px;border-radius:10px;border-left:4px solid #ff6b00}
    .footer{text-align:center;margin-top:30px;color:#666;font-size:12px}
    </style>
    </head>
    <body>
    <div class="container">
    <h1>🎨 ComicCraftAI</h1>
    <p class="subtitle">Transform Stories into Comics with Generative AI</p>
    <div class="badges">
    <span class="badge">🎨 AI Art</span>
    <span class="badge">📖 Auto Story</span>
    <span class="badge">📄 PDF Export</span>
    </div>
    <textarea id="story" placeholder="Enter your story... Eg: A cat superhero saves city from alien dogs..."></textarea>
    <button onclick="generate()">GENERATE COMIC ✨</button>
    <div id="result"></div>
    <p class="footer">Built with FastAPI + Gemini AI | Ready for GitHub</p>
    </div>
    <script>
    function generate(){
      let s=document.getElementById('story').value;
      if(!s){alert('Please enter a story');return;}
      document.getElementById('result').innerHTML=`<div class='panel'><h3>🔥 Comic Generating...</h3><p style='margin-top:10px'><b>Your Story:</b> ${s}</p><p style='margin-top:10px;color:#ff6b00'>AI panels are being created... (Add Gemini API Key for full image generation)</p></div>`;
    }
    </script>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ComicCraftAI is running!"}