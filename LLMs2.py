import streamlit as st

# Configure the page layout to be simple and clean
st.set_page_config(page_title="LLM Learning Plan", layout="centered")

# Main Title
st.title("Large Language Models Learning Plan")
st.markdown("A sequential guide to learning and building AI applications.")
st.divider()

# Topic 1
st.header("1. Python and Environment Setup")
st.subheader("The Prerequisites")
st.markdown("- [Python Tutorial for Beginners (Programming with Mosh)](https://www.youtube.com/watch?v=_uQrJ0TkZlc)")

# Topic 2
st.header("2. AI/LLMs Overview")
st.subheader("Understanding AI and LLMs")
st.markdown("- [AI vs Machine Learning vs Deep Learning (IBM Technology)](https://www.youtube.com/watch?v=4RixMPF4xis)")
st.markdown("- [Intro to Large Language Models (Andrej Karpathy)](https://www.youtube.com/watch?v=zjkBMFhNj_g)")
st.markdown("- [What is a GPT? Visually Explained (3Blue1Brown)](https://www.youtube.com/watch?v=wjZofJX0v4M)")

# Foundation Section
st.header("Foundation: Math & Machine Learning Fundamentals")

st.subheader("Linear Algebra & Calculus")
st.markdown("- [Essence of Linear Algebra - Playlist (3Blue1Brown)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)")
st.markdown("- [Cosine Similarity, Clearly Explained (StatQuest)](https://www.youtube.com/watch?v=e9U0QAFbfLI)")
st.markdown("- [Gradient Descent, Step-by-Step (StatQuest)](https://www.youtube.com/watch?v=sDv4f4s2SB8)")

st.subheader("Machine Learning Concepts")
st.markdown("- [But what is a neural network? (3Blue1Brown)](https://www.youtube.com/watch?v=aircAruvnKk)")

st.subheader("Official Text Documentation")
st.markdown("- [Machine Learning Crash Course (Google)](https://developers.google.com/machine-learning/crash-course)")
st.markdown("- [Machine Learning Glossary (Google)](https://developers.google.com/machine-learning/glossary)")
st.markdown("- [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)")
st.markdown("- [Dive into Deep Learning Book (D2L)](https://d2l.ai/)")
st.markdown("- [NLP Course - Transformers (Hugging Face)](https://huggingface.co/learn/nlp-course)")

# Topic 3
st.header("3. LLM Brains and Text Processing")
st.subheader("Tokens and Context Windows")
st.markdown("- [The OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)")
st.markdown("- [What are Tokens?](https://www.youtube.com/watch?v=nKSk_TiR8YA)")
st.markdown("- [What is a Context Window? (IBM Technology)](https://www.youtube.com/watch?v=-QVoIxEpFkM&pp=ygUqV2hhdCBpcyBhIENvbnRleHQgV2luZG93PyAoSUJNIFRlY2hub2xvZ3kp )")

st.subheader("Embeddings")
st.markdown("- [Word Embedding and Word2Vec Clearly Explained (StatQuest)](https://www.youtube.com/watch?v=viZrOnJclY0)")

# Topic 4
st.header("4. Prompt Engineering")
st.subheader("Techniques and Best Practices")
st.markdown("- [ChatGPT Prompt Engineering for Developers (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)")
st.markdown("- [Prompt Engineering Techniques (freeCodeCamp)](https://www.youtube.com/watch?v=_ZvnD73m40o&pp=ygUscHJvbXB0IGVuZ2luZWVyaW5nIGZ1bGwgY291cnNlIGZvciBiZWdpbm5lcnM%3D)")

# Topic 5
st.header("5. APIs & Local Models")
st.subheader("API and JSON Basics")
st.markdown("- [APIs for Beginners (freeCodeCamp)](https://www.youtube.com/watch?v=GZvSYJDk-us)")
st.markdown("- [Working with JSON Data in Python (Corey Schafer)](https://www.youtube.com/watch?v=9N6a-VLBa2I)")

st.subheader("Making Requests to Models")
st.markdown("- [OpenAI API Tutorial in Python ](https://youtube.com/playlist?list=PLpdmBGJ6ELUIYHjmzYTuePlNRf7yeCACz&si=k-uinRBgv3gYXBlE)")
st.markdown("- [Hugging Face Inference API Tutorial ](https://www.youtube.com/watch?v=85FVwWPg63Q)")

st.subheader("Running Local Models (Free)")
st.markdown("- [Run LLMs locally with Ollama](https://www.youtube.com/watch?v=fBSV5Kw_rR4&pp=ygUoUnVuIExMTXMgbG9jYWxseSB3aXRoIE9sbGFtYSAoTGFuZ0NoYWluKQ%3D%3D)")

# Topic 6
st.header("6. Building Core Applications & UIs")
st.subheader("Terminal Chatbot")
st.markdown("- [How To Create A Chatbot With Python and OpenAI (Indently)](https://www.youtube.com/watch?v=qkzhSZAwD6A&pp=ygU5SG93IFRvIENyZWF0ZSBBIENoYXRib3QgV2l0aCBQeXRob24gYW5kIE9wZW5BSSAoSW5kZW50bHkp)")

st.subheader("Web Interfaces")
st.markdown("- [Streamlit Python Tutorial for Beginners (Data Professor)](https://www.youtube.com/watch?v=Yk-unX4KnV4)")
st.markdown("- [Build an AI Chatbot UI in Streamlit](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)")

# Topic 7
st.header("7. AI Frameworks (LangChain & LlamaIndex)")
st.subheader("Chaining Prompts and Managing Memory")
st.markdown("- [LangChain Crash Course ](https://www.youtube.com/watch?v=lG7Uxts9SXs)")
st.markdown("- [LangChain Memory Tutorial ](https://www.youtube.com/watch?v=sYlMD2OFEgc&pp=ygUaTGFuZ0NoYWluIE1lbW9yeSBUdXRvcmlhbCA%3D)")

# Topic 8
st.header("8. Retrieval-Augmented Generation (RAG)")
st.subheader("Data Processing: Loading and Chunking")
st.markdown("- [The 5 Levels Of Text Splitting For Retrieval (Greg Kamradt)](https://www.youtube.com/watch?v=8OJC21T2SL4)")

st.subheader("Vector Databases")
st.markdown("- [What is a Vector Database? (IBM Technology)](https://www.youtube.com/watch?v=gl1r1XV0SLw&pp=ygUMdmVjdG9yREIgaWJt)")
st.markdown("- [Vector Databases Course (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/)")

st.subheader("Building the RAG Pipeline")
st.markdown("- [RAG Course Playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmva0dRLWEHLznSHKbFD_RJfX)")
st.markdown("- [Chat with Multiple PDFs LangChain Tutorial (Alejandro AO)](https://www.youtube.com/watch?v=dXxQ0LR-3Hg)")

# Topic 9
st.header("9. Advanced Paradigms: AI Agents")
st.subheader("Autonomous Systems & Tool Use")
st.markdown("- [What are AI Agents? (Harrison Chase - LangChain)](https://www.youtube.com/watch?v=F8NKVhkZZWI)")
st.markdown("- [Introduction to LangGraph](https://www.youtube.com/watch?v=CnXdddeZ4tQ&t=461s&pp=ygUoSW50cm9kdWN0aW9uIHRvIExhbmdHcmFwaCAoTGFuZ0NoYWluIEFJKQ%3D%3D)")

# Topic 10
st.header("10. Evaluation & Fine-Tuning")
st.subheader("Evaluating RAG Apps")
st.markdown("- [Evaluating RAG Pipelines with Ragas](https://www.youtube.com/watch?v=SjwTae-dLrw&pp=ygUjRXZhbHVhdGluZyBSQUcgUGlwZWxpbmVzIHdpdGggUmFnYXM%3D  )")

st.subheader("Fine-Tuning Concepts")
st.markdown("- [Fine-Tuning LLMs (freeCodeCamp)](https://www.youtube.com/watch?v=H-oCV5brtU4&t=437s&pp=ygUnIEZpbmUtVHVuaW5nIGFuZCBDdXN0b20gTW9kZWxzIGZvciBMTE1z0gcJCQQLAYcqIYzv)")
st.markdown("- [Fine-Tuning a GPT-2 Model (Hugging Face)](https://youtube.com/playlist?list=PLc2rvfiptPSTGfTp0nhC71ksTY1p5ooCW&si=DD1Ih_z-yFPRKGr2)")

# Topic 11
st.header("11. Deployment")
st.subheader("Hosting the Application")
st.markdown("- [Deploy Streamlit App for Free (Data Professor)](https://www.youtube.com/watch?v=HKoOBiAaHGg)")

st.divider()
st.markdown("End of Learning Plan.")