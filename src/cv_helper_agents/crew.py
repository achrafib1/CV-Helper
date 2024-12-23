from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class CVHelper:
    """CrewaiConversationalChatbot crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["assistant"],
            verbose=False,
        )

    @task
    def assistant_task(self) -> Task:
        return Task(config=self.tasks_config["assistant_task"], agent=self.assistant())

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiConversationalChatbot crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            memory=True,
            verbose=False,
        )