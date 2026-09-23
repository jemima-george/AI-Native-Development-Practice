# GitHub Copilot Notes:

## Copilot Fundamentals:
- GitHub Copilot is an AI-powered developer assistant
- It uses the context of your code and comments to help generate code, explain existing logic, refactor implementations, fix bugs and write tests
- It helps developers code faster
- An extension is available for Visual Studio Code (VS Code), Visual Studio, Neovim, and the JetBrains suite of integrated development environments (IDEs).

## Effective Prompting:
Best practices for prompting with GitHub Copilot - 
- Provide context 
- be predictable
 
Prompting a single file -
- Describe what the file does for the AI to understand 
- Comment what function does and what it should return
- Provide context by specify to open file, comments to describe functions/modules, well wrriten function names or parameter names, inline comment to guide or change result

Prompting a database model design -
- using SQLAlchemy python package
- Describe the type of database model for what application in the start for context 
- Copilot suggests imports, sql alchemy imports and database code
- Can use latest documentation for database design in sql alchemy and copy paste the quick start which will be used by the copilot and adjust it
- Paste in documentation for more context and hint

Add features to an existing code base/app -
- Can use copilot to add new features to an existing app in VS code
- Can open files already built for coplit to review to get more context and built it similar to how it was built already
- Describe new feature as a comment in new file
- Comments to guide the copilot during the development

## Code explanation:
Explain code - 
- Ask Copilot to explain what code is doing using /explain command
- Helps to understand existing code
- Can use explaination for code documentation
- Useful to understand existing code when new people join and collaborate with an existing project to develop new features 
- Can ask copilot to document code using /doc command which will provide summary of code in comments

## Code generation:
- Comment what the code should accomplish and specify paramerters needed to generate code 
- Press tab to accept generated code
- Can tune/change comment if the generated code is not what is needed
- Copilot is trained on public repositories
- Provide code suggesstions
- Can ask copilot to optimize code using /optimize command
- Can create an an Article class, DBContext class, repository interface, repository class, service interface, service class

## Debugging:
- Can ask copilot to optimize code using /optimize command
- Can ask to convert code to add another feature. eg: Converting methods to Async methods
- Provides imports to use in the code
- More code optimization by add additional services or features
- Can ask copilot to fix code errors using /fix command

## Testing:
- Can ask copilot to test code using /test command on selected method
- save time on testing code
- copilot understands exceptions and exception tasks which is useful for testing

## Code review:
- use the official GitHub documentation on GitHub Copilot Code Review
- can review code and provide feedback
- identify issues and suggest fixes
- can customize Copilot code review by adding custom instructions to your repository which can either be repository wide or path specific
- Use .github/copilot-instructions.md for repository-wide review guidance that should apply across the entire codebase
- Use .github/instructions/ ** / *.instructions.md files for path-specific instructions 
- can set up Copilot to automatically review all pull requests
- can manually verify its suggestions

Code review in the GitHub website: 
1. create a pull request or navigate to an existing pull request
2. Under "Reviewers" in the right sidebar, next to Copilot, click Request
3. Copilot will review the code and labels each comment with a severity level of High, Medium, Low
4. It provides a comment review - not a request changes review. Click Fix with copilot to fix errors found in the review

Code review in the Visual Studio Code: 
1. select the code you want to review
2. Right-click the selected code and choose Generate Code > Review
3. VS Code creates review comments in the Comments panel and also shows them inline in the editor
4. If you have uncommitted changes, you can request a review in Visual Studio Code by clicking the Source Control button in the Activity Bar, hover over CHANGES and click the  Copilot Code Review - Uncommitted Changes button. Copilot will review your changes and comments will be shown inline in the files and the Problems tab.

