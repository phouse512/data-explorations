""" iterm logging analysis utilities """
from collections import namedtuple
from datetime import datetime
import os
from typing import Dict, List, Tuple, Union

CommandData = namedtuple("CommandData", ["timestamp", "command", "exit_status", "duration", "clean"])
RowData = namedtuple("RowData", ["timestamp", "type", "data", "session"])


def load_logs(directory: str) -> List[str]:
    """
    given a directory, loads a list of all log lines in string format, unparsed
    """
    lines = []
    files = os.listdir(directory)
    for f_name in files:
        with open("{}/{}".format(directory, f_name)) as f:
            file_lines = f.readlines()
            lines.extend(file_lines)
    
    return lines


def parse_logs_to_sessions(log_lines: List[str]) -> Tuple[List[CommandData], List[str]]:
    """
    Takes log lines and parses them from the format into a list of CommandData object. 
    Joins lines on session uuids to compute exit status, duration ,etc. If a command/status
    line can not be found to complete the pair, clean will be set to False.
    2021-09-24 15:07:48,108-it2-0.1-INFO-session-337D4B97-2985-481E-B5F9-72C900B939AD-status: 0
    """
    # parse row data first
    bad_rows = []
    row_data = []  # type: List[RowData]
    for row in log_lines:
        dash_split = row.split("-")     
        
        try:
            time_str = "{}-{}-{}".format(dash_split[0], dash_split[1], dash_split[2])
            epoch_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S,%f").timestamp()

            # handle the special new session case
            if "new session" in dash_split[6]:
                session_str = row.split(" ")[3]
                row_data.append(RowData(epoch_time, "command", "session-init", session_str))
                continue

            status_data = "-".join(dash_split[12:])
            status_split = status_data.split(":")

            status_type = status_split[0]
            status_output = ":".join(status_split[1:]).strip()

            session = "{}-{}-{}-{}-{}".format(
                dash_split[7],
                dash_split[8],
                dash_split[9],
                dash_split[10],
                dash_split[11],
            )
        except Exception as e:
            print(row)
            print("Received error: ", e)
            bad_rows.append(row)
            continue 

        row_data.append(RowData(
            epoch_time,
            status_type,
            status_output,
            session,
        ))
    
    # create an map of session -> a list of RowData objects
    session_map = {}  # type: Dict[str, List[RowData]]
    for row in row_data: 
        if row.session in session_map:
            session_map[row.session].append(row)
        else:
            session_map[row.session] = [row]
    
    commands = []  # type: List[CommandData]
    # time to pair up command / status rows 
    for key in session_map:
        rows = session_map[key]
        sorted_rows = sorted(rows, key=lambda x: x.timestamp)
        last_command = None  # type: Union[None, RowData]

        for _, sorted_row in enumerate(sorted_rows):
            # handle edge case with no data entered for a command "user hits enter with no data"
            if sorted_row.type == "command" and not sorted_row.data:
                print("no command data, not processing.")
                continue

            if last_command is None and sorted_row.type == "status":
                print("status but no command, skipping")
                continue
            
            if last_command is None and sorted_row.type == "command":
                last_command = sorted_row
                continue
            
            if last_command is not None and sorted_row.type == "status":
                commands.append(CommandData(
                    last_command.timestamp,
                    last_command.data,
                    int(sorted_row.data),
                    sorted_row.timestamp - last_command.timestamp,
                    True,
                ))
                last_command = None
                continue

            if last_command is not None and sorted_row.type == "command":
                print("command found with open command, skipping previous command")
                last_command = sorted_row
                continue

        # handle case if there is a last command but no end time. mark as dirty w/ no duration
        if last_command != None:
            print("command found with no end, adding dirty block")
            commands.append(CommandData(
                last_command.timestamp,
                last_command.data,
                -999999,
                -1,
                False,
            ))
            
    return commands, bad_rows

