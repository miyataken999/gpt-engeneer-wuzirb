import pytest
from appsdcript0001 import extract_text_from_youtube, correct_text, generate_sequence_diagram, generate_user_documentation

def test_extract_text_from_youtube():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    text = extract_text_from_youtube(video_url)
    assert isinstance(text, YouTubeText)

def test_correct_text():
    text = "Hello, world!"
    corrected_text = correct_text(text)
    assert corrected_text == "Hello world"

def test_generate_sequence_diagram():
    text = "Hello, world!"
    sequence_diagram = generate_sequence_diagram(text)
    assert sequence_diagram.startswith("@startuml")

def test_generate_user_documentation():
    text = "Hello, world!"
    user_documentation = generate_user_documentation(text)
    assert user_documentation.startswith("# YouTube Text Extractor and Corrector")