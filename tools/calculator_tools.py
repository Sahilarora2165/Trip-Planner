from langchain.tools import tool # Tool converts normal python func into AI tools


class CalculatorTools():

    # '@' - Decorator that tells python how a function works. Here it works as an AI tool.
    @tool("Make a Calculation")
    def calculate(operation):
        # this triple quotes is called Docstring. Which is used to tell what a function does. And AI agent read this to
        # know what is this function about.
        """
        Useful to perform any mathematical calculations ,
        like sum , minus , multiplication , division etc.
        The input to this tool should be a mathematical expression,
        a couple examples are `200*7` or `500/2*10`
        """
        try:
            return eval(operation) # eval - converts maths expression as string into real calculations.
        except SyntaxError:
            return "Error : Invalid Error in Syntax Expression"
