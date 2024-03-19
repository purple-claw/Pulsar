import json

def print_tool_info(tool_data, output_file):
    try:
        tool_name = tool_data.get("Tool_name")
        description = tool_data.get("Description")
        dependencies = tool_data.get("Dependencies")
        commands = tool_data.get("Commands", [])
        usage = tool_data.get("Usage", [])
        extra_info = tool_data.get("Extra-Info")
        
        # Write tool information to file
        output_file.write("Tool Name: {}\n".format(tool_name))
        output_file.write("Description: {}\n".format(description))
        output_file.write("Dependencies: {}\n".format(dependencies))
        
        # Write commands to file
        if commands:
            output_file.write("Commands:\n")
            for command_info in commands:
                output_file.write("\tFlag: {}\n".format(command_info.get("flag")))
                output_file.write("\tDescription: {}\n".format(command_info.get("description")))
                output_file.write("\n")
        
        # Write usage to file
        if usage:
            output_file.write("Usage:\n")
            for usage_info in usage:
                output_file.write("\tCommand: {}\n".format(usage_info.get("command")))
                output_file.write("\tDescription: {}\n".format(usage_info.get("description")))
                output_file.write("\n")
        
        # Write extra information to file or process it as needed
        if extra_info:
            output_file.write("Extra Information: {}\n".format(extra_info))
        output_file.write("\n")
    except Exception as e:
        print("Error occurred while processing tool information:", e)

def main():
    try:
        # Load JSON data from file
        with open("/home/dev/Desktop/Pulsar/dataset.json", "r") as f:
            data = json.load(f)
        
        # Write tool information to a text file
        with open("/home/dev/Desktop/Pulsar/dataset.txt", "w") as output_file:
            # Process each tool's information
            for tool_data in data:
                print_tool_info(tool_data, output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
