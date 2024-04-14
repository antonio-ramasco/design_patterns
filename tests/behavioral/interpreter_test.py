from behavioral.interpreter import Context, TerminalExpression, NonTerminalExpression
def test_interpreter_client():
    context=Context("SUM")
    terminal_one = TerminalExpression(1)
    assert terminal_one.interpret(context)==1
    terminal_two = TerminalExpression(2)
    assert terminal_two.interpret(context)==2
    tree_add=NonTerminalExpression([terminal_one, terminal_two])
    assert tree_add.interpret(context) == 3

    expression_tree=NonTerminalExpression([TerminalExpression(1),
                                           NonTerminalExpression(
                                              [TerminalExpression(4),
                                               TerminalExpression(6)])
                                           ])
    assert expression_tree.interpret(context)==1+4+6
