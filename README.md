 LinkedIn AI Content Detector

A high-speed **LinkedIn AI Slop Detector** powered by **Laya** an open-source, non-autoregressive System 1 decision engine—with a **FastAPI** backend and an interactive **Streamlit** dashboard.

Unlike standard LLMs (System 2 thinking) that generate text word-by-word with high latency and token costs, this project performs **discriminative single-forward-pass classification** to flag low-quality AI clichés, heavy emoji spam, and engagement-bait formatting in under **50ms**.



##  Key Features

* **Laya, Non-Autoregressive Decision Engine:** Evaluates text in a single forward pass without token-by-token generation.
* **Calibrated Thresholding:** Tuned binary decision boundaries (`p >= 0.5`) optimized for zero-shot classification on local CUDA GPUs.
* **FastAPI Backend:** Asynchronous Python backend designed for low-latency inference calls.
* **Streamlit UI:** Clean, simple frontend for testing post content and inspecting real-time confidence metrics.

