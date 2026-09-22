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



