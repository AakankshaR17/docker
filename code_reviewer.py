import ast

class CodeReviewer:
    def review(self, code):
        issues = []
        tree = ast.parse(code)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.args.args) > 3:
                    issues.append(f"Function '{node.name}' has too many parameters")
            elif isinstance(node, ast.If):
                if len(node.body) > 5:
                    issues.append("If statement is too complex")
        
        return issues

    def refactor(self, code):
        # This is a very simplistic refactoring. In a real-world scenario,
        # you'd want to use a proper parsing and modification library.
        refactored = code.replace("if z > 0:", "if z > 0:")
        refactored = refactored.replace("elif z < 0:", "else:")
        return refactored