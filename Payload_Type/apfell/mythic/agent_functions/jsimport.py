from mythic_payloadtype_container.MythicCommandBase import *
from mythic_payloadtype_container.MythicRPC import *
import json
import base64


class JsimportArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "file": CommandParameter(
                name="file",
                type=ParameterType.File,
                description="Select a JXA file to upload",
            )
        }

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == "{":
                self.load_args_from_json_string(self.command_line)
            else:
                raise ValueError("Missing JSON arguments")
        else:
            raise ValueError("Missing arguments")
        pass


class JsimportCommand(CommandBase):
    cmd = "jsimport"
    needs_admin = False
    help_cmd = "jsimport"
    description = "import a JXA file into memory. Only one can be imported at a time."
    version = 1
    author = "@its_a_feature_"
    attackmapping = []
    argument_class = JsimportArguments

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        original_file_name = json.loads(task.original_params)["file"]
        file_resp = await MythicRPC().execute("create_file", task_id=task.id,
            file=base64.b64encode(task.args.get_arg("file")).decode(),
            saved_file_name=original_file_name
        )
        if file_resp.status == MythicStatus.Success:
            task.args.add_arg("file", file_resp.response["agent_file_id"])
            task.display_params = f"{original_file_name} into memory"
        else:
            raise Exception("Error from Mythic: " + str(file_resp.error))
        return task

    async def process_response(self, response: AgentResponse):
        pass
