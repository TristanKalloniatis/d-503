def joke_structure_str(joke):
    ### This function takes a joke string, and returns a string with end of sentence & joke delimiters.
    
    joke_parse1 = re.sub('\.{2,}','\u03B1', joke) # symbolise multible fullstops (...)
    joke_parse2 = re.sub('\?{2,}','\u03B2', joke_parse1) # symbolise multible question marks (???)
    joke_parse3 = re.sub('\!{2,}','\u03B3', joke_parse2) # symbolise multible exclamation marks (!!!)

    joke_parse4 = re.sub('\.','.\u03B4', joke_parse3) # symbolise fullstops (.)
    joke_parse5 = re.sub('\?','?\u03B4', joke_parse4) # symbolise question marks (?)
    joke_parse6 = re.sub('\!','!\u03B4', joke_parse5) # symbolise exclamation marks (!)
    
    joke_parse7 = re.sub('\u03B1','...\u03B4', joke_parse6) # symbolise fullstops (.)
    joke_parse8 = re.sub('\u03B2', '???\u03B4', joke_parse7) # symbolise question marks (?)
    joke_parse9 = re.sub('u03B3','!!!\u03B4', joke_parse8) # symbolise exclamation marks (!)
    
    joke_parse10 = joke_parse9+'\u03A9'
    
    joke_restructure = re.sub('\u03B4\u03A9', '\u03A9', joke_parse10) # symbolise end of joke  
    
    return(joke_restructure)
