import streamlit as st
import random
import datetime

# confetti effect
from streamlit.components.v1 import html

# Define your javascript
my_js = """
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/confetti@3.0.3/tsparticles.confetti.bundle.min.js"></script>
<script>
const defaults = {
  spread: 360,
  ticks: 100,
  gravity: 0,
  decay: 0.94,
  startVelocity: 30,
};

function shoot() {
  confetti({
    ...defaults,
    particleCount: 30,
    scalar: 1.2,
    shapes: ["circle", "square"],
    colors: ["#a864fd", "#29cdff", "#78ff44", "#ff718d", "#fdff6a"],
  });

  confetti({
    ...defaults,
    particleCount: 20,
    scalar: 2,
    shapes: ["emoji"],
    shapeOptions: {
      emoji: {
        value: ["🦄", "🌈"],
      },
    },
  });
}

setTimeout(shoot, 0);
setTimeout(shoot, 100);
setTimeout(shoot, 200);
</script>
"""

# Wrapt the javascript as html code
my_html = f"{my_js}"

# --------------------------

st.title("로또 생성기 :sparkles")


def start_lotto():
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()
    return lotto


button = st.button("로또를 생성해 주세요!")

if button:
    # Execute your app
    # st.title("Javascript example")
    html(my_html)
    for i in range(0, 5):
        st.subheader(f"{i+1}. 행운의 번호: :green[{start_lotto()}]")
