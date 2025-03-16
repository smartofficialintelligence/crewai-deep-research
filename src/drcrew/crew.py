from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
import os
from dotenv import load_dotenv
import litellm
from pydantic import BaseModel, Field
# Apply a monkey patch to remove the 'stop' parameter which breaks perplexity_llm
original_completion = litellm.completion

def patched_completion(*args, **kwargs):
    if 'stop' in kwargs:
		
        print("Removing 'stop' parameter from LiteLLM call...")
        kwargs.pop('stop')
    return original_completion(*args, **kwargs)

litellm.completion = patched_completion

@CrewBase
class Drcrew():
	"""Drcrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
	@agent
	def manager(self) -> Agent:
		return Agent(
			config=self.agents_config['manager'],
			verbose=True
		)

	@agent
	def perplexity_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['perplexity_researcher'],
			verbose=True
		)

	@agent
	def chatgpt_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['chatgpt_researcher'],
			verbose=True
		)

	@agent
	def claude_sonnet_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['claude_sonnet_researcher'],
			verbose=True
		)

	@agent
	def xai_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['xai_researcher'],
			verbose=True
		)

	@agent
	def deepseek_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['deepseek_researcher'],
			verbose=True
		)

	@task
	def perplexity_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['perplexity_research_task'],
		)

	@task
	def chatgpt_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['chatgpt_research_task'],
		)


	@task
	def claude_sonnet_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['claude_sonnet_research_task'],
		)

	@task
	def xai_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['xai_research_task'],
		)

	@task
	def deepseek_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['deepseek_research_task'],
		)

	@task
	def manager_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['manager_report_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Drcrew crew"""
		return Crew(
			manager_agent=self.manager(), 
			 agents=[
            	self.perplexity_researcher(),
            	self.chatgpt_researcher(),
				self.claude_sonnet_researcher(),
				self.xai_researcher(),
				self.deepseek_researcher()
        	],
			# tools=[delegate_tool],
			tasks=self.tasks,
			process=Process.hierarchical,
			planning=True,
			async_execution=True,
			verbose=True,
		)
