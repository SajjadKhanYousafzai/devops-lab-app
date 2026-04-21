from flask import Flask
from datetime import datetime

app = Flask(__name__)

START_TIME = datetime.now()
request_count = 0

@app.route('/')
def home():
    global request_count
    request_count += 1
    now = datetime.now()
    uptime = now - START_TIME
    total_seconds = int(uptime.total_seconds())
    h, rem = divmod(total_seconds, 3600)
    m, s = divmod(rem, 60)
    uptime_str = f"{h}h {m}m {s}s" if h else (f"{m}m {s}s" if m else f"{s}s")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>DevOps Lab — Sajjad Ali Shah</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: #f0f2f5;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
    }}
    .card {{
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.08);
      padding: 2rem 2.5rem;
      max-width: 480px;
      width: 100%;
    }}
    .top-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f1f5f9;
    }}
    .brand {{ font-size: 12px; color: #94a3b8; letter-spacing: 0.08em; text-transform: uppercase; }}
    .status-pill {{
      display: flex; align-items: center; gap: 6px;
      background: #dcfce7; color: #166534;
      font-size: 12px; font-weight: 600;
      padding: 4px 12px; border-radius: 20px;
    }}
    .dot {{
      width: 7px; height: 7px; border-radius: 50%;
      background: #16a34a;
      animation: pulse 2s infinite;
    }}
    @keyframes pulse {{ 0%,100%{{opacity:1}} 50%{{opacity:0.3}} }}
    .avatar-row {{ display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; }}
    .avatar {{
      width: 60px; height: 60px; border-radius: 50%;
      background: #eff6ff; border: 2px solid #bfdbfe;
      display: flex; align-items: center; justify-content: center;
      font-size: 20px; font-weight: 600; color: #1d4ed8; flex-shrink: 0;
    }}
    .name-block h1 {{ font-size: 20px; font-weight: 600; color: #1e293b; }}
    .name-block p {{ font-size: 13px; color: #64748b; margin-top: 3px; }}
    .info-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 1.25rem; }}
    .info-card {{ background: #f8fafc; border-radius: 10px; padding: 12px 14px; }}
    .info-card .label {{ font-size: 11px; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 4px; }}
    .info-card .value {{ font-size: 14px; font-weight: 600; color: #1e293b; }}
    .clock-row {{
      display: flex; align-items: center; gap: 12px;
      background: #f8fafc; border-radius: 10px;
      padding: 12px 16px; margin-bottom: 1.25rem;
    }}
    .clock-icon {{ width: 18px; height: 18px; color: #94a3b8; flex-shrink: 0; }}
    .clock-label {{ font-size: 11px; color: #94a3b8; }}
    .clock-time {{ font-size: 14px; font-weight: 600; color: #1e293b; margin-top: 2px; }}
    .metrics {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
    .metric {{ text-align: center; padding: 10px 6px; background: #f8fafc; border-radius: 10px; }}
    .metric .m-val {{ font-size: 18px; font-weight: 700; color: #1e293b; }}
    .metric .m-lbl {{ font-size: 11px; color: #94a3b8; margin-top: 2px; }}
    .green {{ color: #16a34a; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="top-bar">
      <span class="brand">DevOps Lab</span>
      <span class="status-pill"><span class="dot"></span>Online</span>
    </div>

    <div class="avatar-row">
      <div class="avatar">SA</div>
      <div class="name-block">
        <h1>Sajjad Ali Shah</h1>
        <p>BSE Student &mdash; DevOps Engineer</p>
      </div>
    </div>

    <div class="info-grid">
      <div class="info-card">
        <div class="label">Registration</div>
        <div class="value">FA22-BSE-046</div>
      </div>
      <div class="info-card">
        <div class="label">Port</div>
        <div class="value">5000</div>
      </div>
      <div class="info-card">
        <div class="label">Environment</div>
        <div class="value">Production</div>
      </div>
      <div class="info-card">
        <div class="label">Framework</div>
        <div class="value">Flask 3.x</div>
      </div>
    </div>

    <div class="clock-row">
      <svg class="clock-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
      </svg>
      <div>
        <div class="clock-label">Session started</div>
        <div class="clock-time">{START_TIME.strftime('%b %d, %Y &mdash; %H:%M:%S')}</div>
      </div>
      <div style="margin-left:auto; text-align:right;">
        <div class="clock-label">Server time</div>
        <div class="clock-time" id="live-clock">{now.strftime('%H:%M:%S')}</div>
      </div>
    </div>

    <div class="metrics">
      <div class="metric">
        <div class="m-val green" id="uptime-display">{uptime_str}</div>
        <div class="m-lbl">Uptime</div>
      </div>
      <div class="metric">
        <div class="m-val">{request_count}</div>
        <div class="m-lbl">Requests</div>
      </div>
      <div class="metric">
        <div class="m-val green">OK</div>
        <div class="m-lbl">Health</div>
      </div>
    </div>
  </div>

  <script>
    const serverStart = new Date("{START_TIME.strftime('%Y-%m-%dT%H:%M:%S')}");
    function tick() {{
      const now = new Date();
      document.getElementById('live-clock').textContent = now.toTimeString().slice(0,8);
      const s = Math.floor((now - serverStart) / 1000);
      const h = Math.floor(s/3600), m = Math.floor((s%3600)/60), sec = s%60;
      document.getElementById('uptime-display').textContent =
        h ? h+"h "+m+"m "+sec+"s" : m ? m+"m "+sec+"s" : sec+"s";
    }}
    setInterval(tick, 1000);
  </script>
</body>
</html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)