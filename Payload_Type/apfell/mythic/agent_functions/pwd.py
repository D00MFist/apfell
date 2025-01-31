from mythic_payloadtype_container.MythicCommandBase import *
import sys
from mythic_payloadtype_container.MythicRPC import *


class PwdArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = []

    async def parse_arguments(self):
        pass


class PwdCommand(CommandBase):
    cmd = "pwd"
    needs_admin = False
    help_cmd = "pwd"
    description = "Prints the current working directory for the agent"
    version = 1
    author = "@its_a_feature_"
    attackmapping = ["T1083"]
    argument_class = PwdArguments

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        resp = await MythicRPC().execute("create_artifact", task_id=task.id,
            artifact="fileManager.currentDirectoryPath",
            artifact_type="API Called",
        )
        return task

    async def process_response(self, response: AgentResponse):
        pass
