import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body {
  margin: 0;
  overflow: hidden;
  background: linear-gradient(#87CEEB, #ffffff);
}

/* Plane */
.plane {
  position: absolute;
  top: 30%;
  left: -300px;
  font-size: 60px;
  animation: fly 4s ease forwards;
}

/* Rope */
.rope {
  width: 2px;
  height: 80px;
  background: black;
  margin: auto;
}

/* Gift */
.gift {
  font-size: 50px;
  cursor: pointer;
  animation: bounce 2s infinite;
}

/* Fly animation */
@keyframes fly {
  0% { left: -300px; }
  100% { left: 40%; }
}

/* Bounce */
@keyframes bounce {
  0%,100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* Message */
.message {
  display: none;
  position: absolute;
  top: 70%;
  width: 100%;
  text-align: center;
  font-size: 30px;
  color: #ff3399;
  font-weight: bold;
}

</style>
</head>

<body>

<div class="plane">
  ✈️
  <div class="rope"></div>
  <div class="gift" onclick="showMessage()">🎁</div>
</div>

<div class="message" id="msg">
  🎉 Happy Birthday Komal 🎉 💖
</div>

<script>
function showMessage() {
  document.getElementById("msg").style.display = "block";
}
</script>

</body>
</html>
""", height=600)
