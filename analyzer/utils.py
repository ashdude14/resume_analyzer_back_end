from transformers import pipeline

def analyze_resume(content):
    summarizer = pipeline("summarization")
    summary = summarizer(content, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
