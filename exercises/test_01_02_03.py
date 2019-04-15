def test():
    import spacy.tokens
    import spacy.lang.es
    assert isinstance(nlp, spacy.lang.es.Spanish), "The nlp object should be an instance of the Spanish class."
    assert isinstance(doc, spacy.tokens.Doc), "Did you process the text with the nlp object to create a doc?"
    assert "print(doc.text)" in ___solution___, "Did you print the doc.text?"

    ___msg___.good("Perfecto! Let's move on to documents, spans and tokens.")
