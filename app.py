import code_to_review
from code_reviewer import CodeReviewer

def main():
    print("Welcome to the Code Review and Refactoring Tool!")
    
    # Get the code to review
    code = code_to_review.bad_function.__code__.co_code
    
    # Create a CodeReviewer instance
    reviewer = CodeReviewer()
    
    # Perform code review
    issues = reviewer.review(code)
    
    # Print review results
    print("\nCode Review Results:")
    for issue in issues:
        print(f"- {issue}")
    
    # Perform refactoring
    refactored_code = reviewer.refactor(code)
    
    print("\nRefactored Code:")
    print(refactored_code)

if __name__ == "__main__":
    main()