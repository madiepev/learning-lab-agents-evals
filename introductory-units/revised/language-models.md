## Describe how language models turn prompts into completions

Large language models, or LLMs, are built to turn input text into a likely next response. They do that by learning patterns in language, not by memorizing fixed answers. That makes them useful for tasks such as summarizing text, drafting responses, and completing partial sentences.

A simple way to think about an LLM is as a prediction engine for language. You give it a prompt, and it predicts the most likely continuation based on the patterns it learned during training.

## Break text into tokens

Before a model can learn those patterns, it breaks text into tokens. A token can be a word, a subword, punctuation, or another common text fragment.

That matters because models do not work directly with raw sentences. They work with token IDs, which give each piece of text a consistent numeric form the model can process.

For example, a sentence such as "I heard a dog bark" becomes a sequence of tokens. The same token can appear in more than one place, and the model uses that repeated structure to learn how language behaves.

## Turn tokens into embeddings

After tokenization, the model turns each token into a vector, often called an embedding. The embedding captures how the token relates to other tokens in similar contexts.

That is where the model starts to understand meaning in a useful way. Tokens that often appear in similar language patterns end up with embeddings that point in similar directions.

A transformer model uses attention to build those embeddings. Attention helps the model decide which nearby tokens matter most for the current token, so it can assign a representation that reflects context instead of just the token itself.

| Step | What happens |
| --- | --- |
| Token | Text is broken into pieces the model can process. |
| Embedding | Each token becomes a vector that reflects context. |
| Attention | The model weighs nearby tokens to sharpen that context. |

This is the point where the model stops treating text as a loose string of words and starts treating it as a structured input it can compare, weight, and predict from.

For example, if you ask for "a short summary of a customer email," the tokens in your prompt tell the model that you want a concise transformation of an existing message. The attention step then weighs the most important tokens in the email so the embedding for each token reflects the parts that matter most for summarization.

## Predict the next token

Once the model has embeddings, it can use them to predict the next token in a sequence. During training, the model sees full text and learns to guess what should come next while ignoring later tokens it has not reached yet.

When you use the model, that same process drives completion. The model looks at the tokens already in the prompt, predicts the next likely token, adds it to the sequence, and repeats the process until it reaches a stopping point.

That is why prompt quality matters. A clearer prompt gives the model better context, which usually leads to a better completion.

Now you can connect the pieces: text becomes tokens, tokens become embeddings, and embeddings help the model predict the next best token in the sequence.
