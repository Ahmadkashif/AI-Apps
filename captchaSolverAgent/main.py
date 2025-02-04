from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent1 = Agent(
        task=f"""
        THIS IS A STANDALONE AND INPEDEPENT PROMPT. IT DOES NOT NEED ANY PAST CONTEXT.
        
        The following is a link where you have to solve a puzzle. 
        https://2captcha.com/demo/rotatecaptcha/
        
        Think aand process step by step.
        
        make sure to only follow these steps:
        Step1: Write a short summary on what you see at the webpage.
        Step2: Identify what are the key elements that you need to focus on.
        Step3: Write a step by step guide on how to solve the puzzle.
        Step4: DO NOT TAKE ANY ACTION, RATHER RETURN THE A STRING THAT IS THE SUMMARY
        """,
        llm=llm,
    )
    result = await agent1.run()
    
    agent2 = Agent(
        task=f"""
        THIS IS A STANDALONE AND INPEDEPENT PROMPT. IT DOES NOT NEED ANY PAST CONTEXT.
        
        The following is a link where you have to solve a puzzle. 
        https://2captcha.com/demo/rotatecaptcha/
        
        Use this guide to identify the correct orientation of the image.
        Identification Step1: Identify the image object, for eaxmple, what is it? an animal? a building? a person?. Whatever it is, identify the object.
        Identification Step2: Identify the orientation of the object. for example: Is it standing up? is it laying down? is it upside down?
        Identification Step3: In most cases the image would be rotated by some degrees on an axle and be presented to you. In this step you need to identify by approximately how many degrees is the image rotated. We will call it finalRotation. For example, if it is an animal upside down, then it is rotated by approximately 180 degrees.
        Identification Step4: Identify the correct orientation of the object. for example: If the object is a person, then the person should be standing up.
        
        Think step by step.
        
        Find the rotation per click value:
        Rotation Step1: Rotate the image right and check how many degrees did the image rotate from the original value. We will call it as rotationPerClick.
        Rotation Step2: divide the finalRotation value by rotationPerClick, and you will get the number of clicks you need to rotate the image. Return this value.
        """,
        llm=llm,
    )
    actions = await agent2.run()
    
    print(result)

asyncio.run(main())