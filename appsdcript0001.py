import youtube_dl
import re
from dataclasses import dataclass
from plantuml import PlantUML
from markdown import Markdown

@dataclass
class YouTubeText:
    text: str

def extract_text_from_youtube(video_url: str) -> YouTubeText:
    """
    Extract text from YouTube video
    """
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        text = info_dict['description']
        return YouTubeText(text)

def correct_text(text: str) -> str:
    """
    Perform correction processing on the extracted text
    """
    # Simple correction processing (e.g., remove punctuation)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def generate_sequence_diagram(text: str) -> str:
    """
    Generate a sequence diagram using PlantUML
    """
    puml = PlantUML()
    puml.startuml()
    puml.participant("YouTube")
    puml.participant("Text Extractor")
    puml.participant("Correction Processor")
    puml.sequence_diagram(text)
    puml.enduml()
    return puml.get_svg_string()

def generate_user_documentation(text: str) -> str:
    """
    Generate user documentation using Markdown
    """
    md = Markdown()
    md.add_header("YouTube Text Extractor and Corrector")
    md.add_paragraph("This script extracts text from YouTube videos and performs correction processing.")
    md.add_code_block(text)
    return md.get_markdown_string()

def main():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    text = extract_text_from_youtube(video_url)
    corrected_text = correct_text(text.text)
    sequence_diagram = generate_sequence_diagram(corrected_text)
    user_documentation = generate_user_documentation(corrected_text)
    print(sequence_diagram)
    print(user_documentation)

if __name__ == "__main__":
    main()