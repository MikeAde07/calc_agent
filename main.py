
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI #used to connect to openai and have our LLM running
from langchain.tools import tool #use this to register a tool that our A.i agent can use
from langgraph.prebuilt import create_react_agent #prebuilt agent
from dotenv import load_dotenv


#looks in directory for current .env file and loads in the variables so we can use them later on in our program
load_dotenv()

def main() :
    #initialize LLM that acts like the brain
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    #allow user and agent to continue interacting
    while True :
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")
        #chunks are parts of a response coming from our agent
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"] :
                for message in chunk["agent"]["messages"] :
                    print(message.content, end="")
        #prints empty line
        print()   

if __name__ == "__main__" :
    main()
                

