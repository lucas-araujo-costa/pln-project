import language_tool_python
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def correct_spelling(text):
    tool = language_tool_python.LanguageTool('pt-BR')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("portuguese"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])
