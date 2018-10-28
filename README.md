# d-503
NLP and image classification project

Task: build a predictive and generative language model for captions on reddit posts from /r/adviceanimals.

Simplification: cluster underlying image posts into circa 10 categories of images, throwing out the other images. Use an OCR to pull the caption T = (image title, top text, bottom text). I = one-hot encoding of image category. X = additional metadata (time of posting, poster ID, ...). y = upvotes achieved on that post.

Phase 1: Explain y best as possible using only X and I, arriving at predictions \overline{y} = f(X, I). Since the distribution of y is likely to approximate a logarithmic normal, we will probably need to log transform. We will also be using residuals later as weights (and responses) which we require to be non-negative, so we end up with residuals of the form \frac{y}{f(X, I)}.

Phase 2: Predictive phase. We use T together with I to additionally explain the residual response, arriving at a function \theta : (T, I) \mapsto \overline{y}. This will be used as the final evaluation metric in phase 4 below.

Phase 3: Generative phase. We use I together with knowledge of T so far to cotninue to generate T. In order to produce "successful examples", we will weight examples by the "residuals" from phase 1. Some care must be taken over the order in which the constituents of T are generated. We arrive at a function \psi : I \mapsto T.

Phase 4: Evaluation phase. We perform a final evaluation of the generative language model, using the predictive model from phase 2, by composing \psi with \theta and inverting the transformation in phase 1 to arrive at a prediction of the number of upvotes our generated text would receive had it been posited.

Notes on data policy: each task will train, validate, and test on different datasets to minimise the possibility of overfitting and model selection bias.
