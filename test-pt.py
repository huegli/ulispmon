from __future__ import unicode_literals
import pygments
from pygments.lexers.lisp import CommonLispLexer
from pygments.styles import get_style_by_name
from pygments.token import Token
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles.pygments import style_from_pygments_cls

print_formatted_text(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))

text = [
        (Token.Keyword, 'print'),
        (Token.Punctuation, '('),
        (Token.Literal.String.Double, '"'),
        (Token.Literal.String.Double, 'hello'),
        (Token.Literal.String.Double, '"'),
        (Token.Punctuation, ')'),
        (Token.Text, '\n'),
        ]

print_formatted_text(PygmentsTokens(text))


style = style_from_pygments_cls(get_style_by_name('native'))
session = PromptSession('Enter Lisp: ', lexer=PygmentsLexer(CommonLispLexer), style=style,
                        include_default_pygments_style=False)
answer = ''

while (answer != '(bye)'):
    answer = session.prompt()
    tokens = list(pygments.lex(answer, lexer=CommonLispLexer()))
    print_formatted_text(PygmentsTokens(tokens), style=style)
