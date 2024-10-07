from inltk.inltk import tokenize

# Define your stop words in Gujarati
STOP_WORDS_GUJARATI = [
    "લેતા", "શા", "ઉભા", "હો", "હોઈ", "મા", "મૂકી", "નહી", "બધું", "હા", "મી", "એન", 
    "તું", "નો", "છો", "જી", "લેવા", "આર", "છીએ", "નં", "એવો", "હોવા", "તેથી", "નું", 
    "છ", "એવા", "એની", "થતાં", "જેવી", "બંને", "હશે", "માં", "ની", "હતાં", "તેવી", 
    "થયો", "એવી", "થી", "થયું", "ત્યાં", "બની", "ગયો", "છતાં", "આપી", "રહે", "તેઓ", 
    "પાસે", "તેમ", "ને", "તેને", "હું", "બાદ", "શકે", "જો", "અંગે", "રહી", "એમ", 
    "તેના", "કરે", "થઇ", "સુધી", "જાય", "રૂા", "કોઈ", "ના", "હવે", "તેની", "સામે", 
    "આવે", "બે", "થઈ", "ન", "જે", "આવી", "તા", "પર", "હોય", "હતું", "એ", "કરી", 
    "તે", "હતી", "માટે", "તો", "જ", "પણ", "કે", "આ", "અને", "છે"
]

def remove_stop_words(tokens, stop_words):
    return [token for token in tokens if token[1:] not in stop_words]  # Remove '▁' prefix before checking

def preprocess_text(text1, text2):
    # Tokenize both texts
    string1_tokens = tokenize(text1, 'gu')
    string2_tokens = tokenize(text2, 'gu')

    # Filter tokens and remove stop words, ignoring leading underscore
    filtered_string1_tokens = [
        token for token in string1_tokens if token.lstrip('_') not in STOP_WORDS_GUJARATI and token not in STOP_WORDS_GUJARATI
    ]
    filtered_string2_tokens = [
        token for token in string2_tokens if token.lstrip('_') not in STOP_WORDS_GUJARATI and token not in STOP_WORDS_GUJARATI
    ]

    # Convert tokens back to strings without '▁' prefix
    filtered_string1 = ' '.join([token[1:] if token.startswith('▁') else token for token in filtered_string1_tokens])
    filtered_string2 = ' '.join([token[1:] if token.startswith('▁') else token for token in filtered_string2_tokens])

    return filtered_string1, filtered_string2
