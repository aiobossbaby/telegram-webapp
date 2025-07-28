<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ဖော်မြုလာစိုင်း</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap');
    body {
      margin: 0;
      font-family: 'Playfair Display', serif;
      background: linear-gradient(135deg, #111, #222);
      color: gold;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      overflow: hidden;
      text-align: center;
    }
    .card {
      background: rgba(255, 215, 0, 0.05);
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
      backdrop-filter: blur(10px);
      border: 2px solid gold;
      max-width: 700px;
      animation: fadeIn 2s ease;
    }
    h1 {
      font-size: 2.5em;
      margin-bottom: 10px;
    }
    p {
      font-size: 1.2em;
      color: #fff9;
      margin: 10px 0;
      line-height: 1.6;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }
    canvas {
      position: fixed;
      top: 0;
      left: 0;
      z-index: -1;
    }
  </style>
</head>
<body>
<canvas id="confetti"></canvas>
<div class="card">
  <h3>၂၉ရက်နေ့မှစ၍</h3>
  <p><strong>တစ်ပတ်အတွက်</strong></p>
  <p>နှစ်ရက်မကျော်ငွေပေါ် - သုံည<br>
     သုံးရက်မကျော်ငွေပေါ် - သုံး</p>
  <p>တစ်ပတ်စာမွေး - သုံးဘရိတ် (၅၈၊၃၀၊၄၉)<br>
     မွေး -၂၇၄၉ ခွေပူး<br>
     ၂၄၀ ကိုမကပ်ထွက်မယ်။<br>
     (၂၁၊၂၉၊၄၃၊၄၅၊၃၀၊၉၀)</p>
</div>
<script>
  const canvas = document.getElementById('confetti');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  const confetti = [];
  for (let i = 0; i < 100; i++) {
    confetti.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 4 + 1,
      d: Math.random() * 40 + 10
    });
  }
  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'gold';
    confetti.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2, true);
      ctx.fill();
    });
    update();
  }
  function update() {
    confetti.forEach(p => {
      p.y += Math.cos(p.d) + 1 + p.r / 2;
      p.x += Math.sin(p.d) * 2;
      if (p.y > canvas.height) {
        p.x = Math.random() * canvas.width;
        p.y = -10;
      }
    });
  }
  setInterval(draw, 33);
</script>
</body>
</html>