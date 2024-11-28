# Chat Visualizer of AI Agent Multi-Turn Dialogue

In this tutorial, I will introduce how to use the chat visualizer feature of agentboard ([Github](https://ai-hub-admin.github.io/agentboard/),[Docs](http://www.deepnlp.org/blog/agentBoard-ai-agent-visualization-toolkit-agent-loop-workflow)) to help visualize huge amount 
of chat logs. agentboard is a python package to help visualize agent_loop, RAG, Chat messages, and multi-modal datas. It provides useful web GUI 
to quickly protytype the Chat logs, and you can take screen shots of the demos, put them in your tech report, arxiv papers, or even continue the Chat of some open ended funny dialogues.


### Example 1: Simple Demo of using the AgentBoard to log the messages.

**ab.summary.messages**

A typical chat history between AI agents and users are in the format of a list of jsons. [{"role": "user", "content": "message 1"}, {"role": "assistant", "content": "message 2"}, ...]

```

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


```

**Run the Demo**


```
    python run_chat_visualizer.py

```

You will find the logs will be saved to local "log" folder

Then you can run the agentboard and see the visualized chat history in a Chatbot.



```
agentboard --logdir=./log
```

![Chat Visualizer Using Deepnlp Agentboard](https://github.com/llmpro70b/Chat-Visualizer/blob/main/agentboard_chat_visualizer?raw=true)


Alternatively, you can also use the online Chat Visualizer Tool for quick prototypes ([DeepNLP Chat Visualizer](http://www.deepnlp.org/workspace/dialogue_visualization))
It provides more UI choices, such as the ones like ChatGPT, Whatsapp, Wechat, etc. 




## Agents Related Pipeline Workflow and Document
### AI Services Reviews and Ratings <br>
##### AI Agent
[AI Agent User Reviews](http://www.deepnlp.org/store/ai-agent) <br>
[Microsoft AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-microsoft-ai-agent) <br>
[Claude AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-claude-ai-agent) <br>
[OpenAI AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-openai-ai-agent) <br>
[AgentGPT AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-agentgpt) <br>
[Saleforce AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-salesforce-ai-agent) <br>
[Google AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-google-ai-agent) <br>
[Google AI Agents Space](http://www.deepnlp.org/store/ai-agent/ai-agent/pub-google-ai-agent/google-ai-agents-space-review) <br>
##### Chatbot
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[ChatGPT User Reviews](http://www.deepnlp.org/store/pub/pub-chatgpt-openai) <br>
[Gemini User Reviews](http://www.deepnlp.org/store/pub/pub-gemini-google) <br>
[Perplexity User Reviews](http://www.deepnlp.org/store/pub/pub-perplexity) <br>
[Claude User Reviews](http://www.deepnlp.org/store/pub/pub-claude-anthropic) <br>
[Qwen AI Reviews](http://www.deepnlp.org/store/pub/pub-qwen-alibaba) <br>
[Doubao Reviews](http://www.deepnlp.org/store/pub/pub-doubao-douyin) <br>
[ChatGPT Strawberry](http://www.deepnlp.org/store/pub/pub-chatgpt-strawberry) <br>
[Zhipu AI Reviews](http://www.deepnlp.org/store/pub/pub-zhipu-ai) <br>
##### AI Image Generation
[Midjourney User Reviews](http://www.deepnlp.org/store/pub/pub-midjourney) <br>
[Stable Diffusion User Reviews](http://www.deepnlp.org/store/pub/pub-stable-diffusion) <br>
[Runway User Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[GPT-5 Forecast](http://www.deepnlp.org/store/pub/pub-gpt-5) <br>
[Flux AI Reviews](http://www.deepnlp.org/store/pub/pub-flux-1-black-forest-lab) <br>
[Canva User Reviews](http://www.deepnlp.org/store/pub/pub-canva) <br>
##### AI Video Generation
[Luma AI](http://www.deepnlp.org/store/pub/pub-luma-ai) <br>
[Pika AI Reviews](http://www.deepnlp.org/store/pub/pub-pika) <br>
[Runway AI Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[Kling AI Reviews](http://www.deepnlp.org/store/pub/pub-kling-kwai) <br>
[Dreamina AI Reviews](http://www.deepnlp.org/store/pub/pub-dreamina-douyin) <br>
##### AI Education
[Coursera Reviews](http://www.deepnlp.org/store/pub/pub-coursera) <br>
[Udacity Reviews](http://www.deepnlp.org/store/pub/pub-udacity) <br>
[Grammarly Reviews](http://www.deepnlp.org/store/pub/pub-grammarly) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
[Unitree Robotics Reviews](http://www.deepnlp.org/store/pub/pub-unitree-robotics) <br>
[Waymo User Reviews](http://www.deepnlp.org/store/pub/pub-waymo-google) <br>
[ANYbotics Reviews](http://www.deepnlp.org/store/pub/pub-anybotics) <br>
[Boston Dynamics](http://www.deepnlp.org/store/pub/pub-boston-dynamic) <br>
##### AI Tools
[DeepNLP AI Tools](http://www.deepnlp.org/store/pub/pub-deepnlp-ai) <br>
##### AI Widgets
[Apple Glasses](http://www.deepnlp.org/store/pub/pub-apple-glasses) <br>
[Meta Glasses](http://www.deepnlp.org/store/pub/pub-meta-glasses) <br>
[Apple AR VR Headset](http://www.deepnlp.org/store/pub/pub-apple-ar-vr-headset) <br>
[Google Glass](http://www.deepnlp.org/store/pub/pub-google-glass) <br>
[Meta VR Headset](http://www.deepnlp.org/store/pub/pub-meta-vr-headset) <br>
[Google AR VR Headsets](http://www.deepnlp.org/store/pub/pub-google-ar-vr-headset) <br>
##### Social
[Character AI](http://www.deepnlp.org/store/pub/pub-character-ai) <br>
##### Self-Driving
[BYD Seal](http://www.deepnlp.org/store/pub/pub-byd-seal) <br>
[Tesla Model 3](http://www.deepnlp.org/store/pub/pub-tesla-model-3) <br>
[BMW i4](http://www.deepnlp.org/store/pub/pub-bmw-i4) <br>
[Baidu Apollo Reviews](http://www.deepnlp.org/store/pub/pub-baidu-apollo) <br>
[Hyundai IONIQ 6](http://www.deepnlp.org/store/pub/pub-hyundai-ioniq-6) <br>


### Related Blogs <br>
[AgentBoard AI Agent Visualization Toolkit](http://www.deepnlp.org/blog/agentboard-ai-agent-visualization-toolkit-agent-loop-workflow) <br>
[DeepNLP AI Agents Designing Guidelines](http://www.deepnlp.org/blog?category=agent) <br>
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>
[AI Boyfriend User Reviews](http://www.deepnlp.org/store/chatbot-assistant/ai-boyfriend) <br>
[AI Girlfriend User Reviews](http://www.deepnlp.org/store/chatbot-assistant/ai-girlfriend) <br>

