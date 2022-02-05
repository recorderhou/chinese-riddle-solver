# chinese-riddle-solver
![](teaser.jpg)

We built a hybrid model combining embedding model for glyph and pre-trained model ERNIE.
For riddles with single character, we use the glyph based model directly. For riddles longer than one character, we use ERNIE to select the right answer among the given 5 choices.
