class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create empty stack
        res = []

        # Itterate over each token, remove negative sign and append if number is a digit
        for token in tokens:
            if token.lstrip('-').isdigit():
                res.append(int(token))
            
            # If not a number, pop the last two digits in the res and preform operand function on numbers
            else:
                b = res.pop()
                a = res.pop()
            
            if token == '+':
                res.append(a + b)
            elif token == '-':
                res.append(a - b)
            elif token == '*':
                res.append(a * b)
            elif token == '/':
                res.append(int(a / b))
        
        return res[0]