import agentboard as ab

def fun_chat_history():
    """
        Chat logs between a user and a chatbot
    """
    chat_history = []
    chat_history.append({"role": "user", "content": "Please tell me a joke"})
    chat_history.append({"role": "assistant", "content": "Why don’t skeletons fight each other? Because they don’t have the guts! "})
    chat_history.append({"role": "user", "content": "It's not funny. Try another one."})
    chat_history.append({"role": "assistant", "content": "Why do programmers prefer dark mode? Because light attracts bugs! "})
    chat_history.append({"role": "user", "content": "Alright, this one is good..."})
    return chat_history

def run_chat_visualizer():
    """
        agentboard --logdir=./log
        # agentboard --logdir=./log --logfile=xxx.log --static=./static --port=5000
    """
    messages = fun_chat_history()
    with ab.summary.FileWriter(logdir="./log", static="./static") as writer:
        ab.summary.messages(name="Fun Chat Log", data=messages, agent_name="ChatGPT")

if __name__ == "__main__":
    run_chat_visualizer()
