Completions = {
    'hi': 'hi! how',
    ' how': ' are',
    'are': ' you',
    'hi! how': ' are',
    ' you': '<stop>',
    '<stop>': '<stop>',
    ' are': ' you',
    'a': 'b',
    'b': 'c',
    'c': 'd',
    'd': 'e',
    'e': 'f',
    'f': 'g',
    'g': 'h',
    'h': 'i',
    'i': 'j',
    'j': 'k',
    'k': 'l',
    'l': 'm',
    'm': 'n',
    'n': 'o',
    'o': 'p',
    'p': 'q',
    'q': 'r',
    'r': 's',
    's': 't',
    't': 'u',
    'u': 'v',
    'v': 'w',
    'w': 'x',
    'x': 'y',
    'y': 'z',
    'z': 'this is',
    'this': 'a',
    'a': 'test',
    'test': 'for',
    'for': 'coherent',
    'coherent': 'text',
    'text': 'generation',
    'generation': 'using',
    'using': 'a ',
    'a ': 'dictionary',
    'dictionary': 'in',
    'in': 'Python',
    'Python': 'programming',
    'programming': 'language',
    'language': 'using',
    'using': 'using a',
    'using a': 'Seq2Seq',
    'Seq2Seq': '(Sequence-to-Sequence)',
    '(Sequence-to-Sequence)': 'large',
    'large': 'large language',
    'large language': 'large language model',
    'large language model': '(LLM).',
    '(LLM).': '<stop>',
    "what is sonoai?": "SonoAI?",
    'SonoAI?': 'SonoAI? You mean',
    'SonoAI? You mean': 'the people who created me?',
    'the people who created me?': "This is what the CEO says: 'We are SonoAI (SonoAI LLC). At our AI start-up, we are dedicated to creating artificial intelligence that is both intelligent and ethical. We believe that with the rapid advancements in technology, it is crucial to ensure that AI is developed in a responsible manner, one that aligns with human values and promotes social good. Our mission is to create AI that can learn, reason, and interact with humans in a way that is indistinguishable from another human being. To achieve this, we develop algorithms and models that are transparent, explainable, and fair. We also prioritize the development of AI that is capable of understanding and responding to emotions, empathy, and creativity, which are essential qualities for building truly human-like AI. However, we recognize that there are potential risks associated with the development of AI, such as job displacement, privacy invasion, and even the potential for AI to be misused. Therefore, we are committed to addressing these concerns through open communication, transparency, and collaboration with stakeholders. Ultimately, our goal is to create AI that benefits society as a whole and enhances the lives of individuals.'",
    "This is what the CEO says: 'We are SonoAI (SonoAI LLC). At our AI start-up, we are dedicated to creating artificial intelligence that is both intelligent and ethical. We believe that with the rapid advancements in technology, it is crucial to ensure that AI is developed in a responsible manner, one that aligns with human values and promotes social good. Our mission is to create AI that can learn, reason, and interact with humans in a way that is indistinguishable from another human being. To achieve this, we develop algorithms and models that are transparent, explainable, and fair. We also prioritize the development of AI that is capable of understanding and responding to emotions, empathy, and creativity, which are essential qualities for building truly human-like AI. However, we recognize that there are potential risks associated with the development of AI, such as job displacement, privacy invasion, and even the potential for AI to be misused. Therefore, we are committed to addressing these concerns through open communication, transparency, and collaboration with stakeholders. Ultimately, our goal is to create AI that benefits society as a whole and enhances the lives of individuals.'": '<stop>'
    }

i = input('Prompt: ')
il = i.lower()
p = Completions[il]  # Initialize p here
p1 = Completions[p]  # Initialize p1 here
while p1.lower() != '<stop>':
    print(p, end=' ')
    print(p1)
    p = Completions[p]
    p1 = Completions[p]
