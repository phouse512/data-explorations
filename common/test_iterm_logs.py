""" test the iterm_logs utility functions """
import pytest
from unittest.mock import ANY

from common.iterm_logs import CommandData, parse_logs_to_sessions


def test_parse_logs_to_sessions_1():
    """
    test parse log functionality
    """
    lines = [
        "2021-03-19 09:32:23,421-it2-0.1-INFO-new session: 7614DE23-2C12-4C0E-BCBC-FE11151FFB26",
        "2021-03-19 09:32:23,422-it2-0.1-INFO-new session: 0264CAB4-546D-4626-80A0-9CDAE823C9F2",
        "2021-03-19 09:32:23,423-it2-0.1-INFO-new session: 36D97F46-993A-4AC7-99AC-E793434F4FCA",
        "2021-03-19 09:32:23,423-it2-0.1-INFO-new session: 41331E67-186E-4984-8DAD-C1AB2646AC55",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: 96702554-962D-400A-BC28-CC98A6940BA9",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: 23BF42DA-B1A9-4DCF-8CDD-33449830B9D3",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: C97A73C8-C628-4A8F-80F4-BC2705BA7FBC",
        "2021-03-19 09:32:25,483-it2-0.1-INFO-session-7614DE23-2C12-4C0E-BCBC-FE11151FFB26-status: 0",
        "2021-03-19 09:32:25,483-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:32:25,496-it2-0.1-INFO-session-0264CAB4-546D-4626-80A0-9CDAE823C9F2-status: 0",
        "2021-03-19 09:32:25,527-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-status: 0",
        "2021-03-19 09:32:25,573-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 09:32:25,587-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-status: 0",
        "2021-03-19 09:32:25,704-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-status: 0",
    ]
    commands, bad_lines = parse_logs_to_sessions(lines)
    assert len(bad_lines) == 0
    assert len(commands) == 7
    assert commands[0] == CommandData(1616164343.421, "session-init", 0, pytest.approx(2.062, rel=1e-4), True)
    assert commands[-1] == CommandData(1616164343.424, "session-init", 0, pytest.approx(2.28, rel=1e-4), True)
       

def test_parse_logs_to_sessions_2():
    """
    More test cases
    """
    lines = [
        "2021-03-19 09:32:39,083-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: setup tuning",
        "2021-03-19 09:32:39,097-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:32:47,385-it2-0.1-INFO-session-7614DE23-2C12-4C0E-BCBC-FE11151FFB26-command: factory_db_prod",
        "2021-03-19 09:33:18,836-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: python generate-retuning-notebook.py --name philip --start_date 03-10-21 --end_date 03-19-21 -ds 10530",
        "2021-03-19 09:33:21,113-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:33:25,467-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: python generate-retuning-notebook.py --name philip --start_date 03-10-21 --end_date 03-19-21 -ds 10538",
        "2021-03-19 09:33:26,161-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:35:03,407-it2-0.1-INFO-session-0264CAB4-546D-4626-80A0-9CDAE823C9F2-command: amper_juypter ",
        "2021-03-19 10:00:38,399-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:00:38,492-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:00:38,494-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:00:38,502-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:00:38,537-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:00:38,898-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:00:38,902-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:00:38,905-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:00:38,906-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:00:38,911-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:31:04,418-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-16 00:00:00\" \"2021-03-19 10:30:00\"",
        "2021-03-19 10:31:05,574-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 10:31:32,872-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd",
        "2021-03-19 10:31:32,874-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:34,803-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd amper/toad-house/",
        "2021-03-19 10:31:34,849-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:35,950-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ls",
        "2021-03-19 10:31:35,959-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:39,360-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: setup toad-house",
        "2021-03-19 10:31:39,361-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:41,768-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: pycharm .",
        "2021-03-19 10:31:44,325-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:54:29,173-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
    ]
    commands, bad_lines = parse_logs_to_sessions(lines)
    assert len(bad_lines) == 0
    assert len(commands) == 11

    required_commands = [
        CommandData(1616164359.083, "setup tuning", 0, pytest.approx(0.014, rel=1e-4), True),
        CommandData(1616167901.768, "pycharm .", 0, pytest.approx(2.557, rel=1e-4), True),
        CommandData(1616164367.385, "factory_db_prod", -999999, -1, False),
        CommandData(1616164503.407, "amper_juypter", -999999, -1, False),
    ]

    matches = 0
    for command in commands:
        if command in required_commands:
            matches += 1

    assert matches == len(required_commands) 


def test_parse_logs_to_session_3():
    """ More test cases. """

    lines = [
        "2021-03-19 09:32:23,421-it2-0.1-INFO-new session: 7614DE23-2C12-4C0E-BCBC-FE11151FFB26",
        "2021-03-19 09:32:23,422-it2-0.1-INFO-new session: 0264CAB4-546D-4626-80A0-9CDAE823C9F2",
        "2021-03-19 09:32:23,423-it2-0.1-INFO-new session: 36D97F46-993A-4AC7-99AC-E793434F4FCA",
        "2021-03-19 09:32:23,423-it2-0.1-INFO-new session: 41331E67-186E-4984-8DAD-C1AB2646AC55",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: 96702554-962D-400A-BC28-CC98A6940BA9",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: 23BF42DA-B1A9-4DCF-8CDD-33449830B9D3",
        "2021-03-19 09:32:23,424-it2-0.1-INFO-new session: C97A73C8-C628-4A8F-80F4-BC2705BA7FBC",
        "2021-03-19 09:32:25,483-it2-0.1-INFO-session-7614DE23-2C12-4C0E-BCBC-FE11151FFB26-status: 0",
        "2021-03-19 09:32:25,483-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:32:25,496-it2-0.1-INFO-session-0264CAB4-546D-4626-80A0-9CDAE823C9F2-status: 0",
        "2021-03-19 09:32:25,527-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-status: 0",
        "2021-03-19 09:32:25,573-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 09:32:25,587-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-status: 0",
        "2021-03-19 09:32:25,704-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-status: 0",
        "2021-03-19 09:32:39,083-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: setup tuning",
        "2021-03-19 09:32:39,097-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:32:47,385-it2-0.1-INFO-session-7614DE23-2C12-4C0E-BCBC-FE11151FFB26-command: factory_db_prod ",
        "2021-03-19 09:33:18,836-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: python generate-retuning-notebook.py --name philip --start_date 03-10-21 --end_date 03-19-21 -ds 10530",
        "2021-03-19 09:33:21,113-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:33:25,467-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: python generate-retuning-notebook.py --name philip --start_date 03-10-21 --end_date 03-19-21 -ds 10538",
        "2021-03-19 09:33:26,161-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 09:35:03,407-it2-0.1-INFO-session-0264CAB4-546D-4626-80A0-9CDAE823C9F2-command: amper_juypter ",
        "2021-03-19 10:00:38,399-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:00:38,492-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:00:38,494-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:00:38,502-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:00:38,537-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:00:38,898-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:00:38,902-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:00:38,905-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:00:38,906-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:00:38,911-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:31:04,418-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-16 00:00:00\" \"2021-03-19 10:30:00\"",
        "2021-03-19 10:31:05,574-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 10:31:32,872-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd",
        "2021-03-19 10:31:32,874-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:34,803-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd amper/toad-house/",
        "2021-03-19 10:31:34,849-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:35,950-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ls",
        "2021-03-19 10:31:35,959-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:39,360-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: setup toad-house",
        "2021-03-19 10:31:39,361-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:31:41,768-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: pycharm .",
        "2021-03-19 10:31:44,325-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 10:54:29,173-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:29,208-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:29,314-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:29,314-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:54:29,397-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:29,995-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:30,002-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:30,004-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:30,004-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:54:30,005-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:33,501-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:33,531-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:33,532-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:33,556-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:54:33,669-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:35,312-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:35,314-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:35,315-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:35,316-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:54:35,316-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:36,325-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:36,539-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:36,549-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:36,556-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 10:54:36,695-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:39,476-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 10:54:40,077-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 10:54:40,080-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 10:54:40,083-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 10:54:40,085-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 11:00:23,426-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd wip/",
        "2021-03-19 11:00:23,440-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:00:26,641-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:00:29,978-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:00:42,976-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:00:44,966-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:00:45,846-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ls",
        "2021-03-19 11:00:45,867-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:06:01,233-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ls",
        "2021-03-19 11:06:01,254-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:06:03,973-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:06:05,060-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:06:14,015-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:06:15,121-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:18:47,100-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:18:49,798-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:18:57,189-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:18:58,096-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:19:28,656-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: python get-counts.py ",
        "2021-03-19 11:19:30,136-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 11:51:25,461-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-19 00:00:00\" \"2021-03-19 11:40:00\"",
        "2021-03-19 11:51:26,072-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 11:52:06,711-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-18 00:00:00\" \"2021-03-19 00:00:00\"",
        "2021-03-19 11:52:07,040-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 11:52:31,057-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-16 00:00:00\" \"2021-03-18 00:00:00\"",
        "2021-03-19 11:52:31,368-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 11:53:14,086-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-14 00:00:00\" \"2021-03-16 00:00:00\"",
        "2021-03-19 11:53:14,397-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 11:53:49,245-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ee \"2021-03-12 00:00:00\" \"2021-03-14 00:00:00\"",
        "2021-03-19 11:53:49,618-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-status: 0",
        "2021-03-19 14:01:11,906-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:01:11,910-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:01:11,910-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:01:11,993-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:01:12,123-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 14:01:12,395-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 14:01:12,397-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:01:12,399-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:01:12,399-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:01:12,400-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:53:49,934-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:53:49,945-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:53:49,950-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:53:49,966-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:53:50,001-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 14:53:50,163-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:53:50,191-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:53:50,192-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:53:50,217-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:53:50,229-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 14:53:59,789-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: curl https://api.dota-int.com",
        "2021-03-19 14:54:00,649-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 130",
        "2021-03-19 14:54:04,975-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: curl -v  https://api.dota-int.com",
        "2021-03-19 14:54:50,803-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 130",
        "2021-03-19 14:57:51,219-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd ",
        "2021-03-19 14:57:51,222-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 14:57:57,793-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:57:58,053-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 14:57:59,169-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd amper/sheik/nginx.conf ",
        "2021-03-19 14:57:59,173-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 1",
        "2021-03-19 14:58:02,704-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: cd amper/sheik/",
        "2021-03-19 14:58:02,705-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 14:58:04,104-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: vim nginx.conf ",
        "2021-03-19 14:58:10,375-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:58:10,383-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:58:10,389-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:58:10,421-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 14:58:10,590-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 14:58:10,612-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 14:58:10,631-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 14:58:10,646-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:01:39,477-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 15:01:41,290-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:01:42,512-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: curl -v  https://api.dota-int.com",
        "2021-03-19 15:02:42,946-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 15:03:57,538-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: curl -v  https://api.dota-int.com",
        "2021-03-19 15:04:58,002-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-status: 0",
        "2021-03-19 15:22:41,911-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:22:41,914-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 15:22:41,917-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 15:22:41,917-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:42,163-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:42,642-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:42,644-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:42,785-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:22:42,788-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 15:22:42,789-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 15:22:45,794-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:22:46,009-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 15:22:46,010-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 15:22:46,010-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:46,175-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:47,167-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:47,167-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:47,393-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:47,658-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:47,999-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 15:22:47,999-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 15:22:48,000-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:22:48,156-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 15:22:48,156-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 15:22:48,368-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 15:22:48,370-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 15:22:48,371-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 17:14:47,459-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 17:14:47,625-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 17:14:47,725-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 17:14:47,807-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
        "2021-03-19 17:14:47,903-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 17:14:48,267-it2-0.1-INFO-session-C97A73C8-C628-4A8F-80F4-BC2705BA7FBC-command: ",
        "2021-03-19 17:14:48,282-it2-0.1-INFO-session-96702554-962D-400A-BC28-CC98A6940BA9-command: ",
        "2021-03-19 17:14:48,283-it2-0.1-INFO-session-36D97F46-993A-4AC7-99AC-E793434F4FCA-command: ",
        "2021-03-19 17:14:48,283-it2-0.1-INFO-session-41331E67-186E-4984-8DAD-C1AB2646AC55-command: ",
        "2021-03-19 17:14:48,284-it2-0.1-INFO-session-23BF42DA-B1A9-4DCF-8CDD-33449830B9D3-command: ",
    ]
    commands, bad_lines = parse_logs_to_sessions(lines)
    assert len(bad_lines) == 0
    assert len(commands) == 41

    required_commands = [
        CommandData(ANY, "cd wip/", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "python get-counts.py", 0, ANY, True),
        CommandData(ANY, "vim nginx.conf", 0, ANY, True),
        CommandData(ANY, "curl -v  https://api.dota-int.com", 0, ANY, True),
        CommandData(ANY, "curl -v  https://api.dota-int.com", 0, ANY, True),
        CommandData(ANY, "curl https://api.dota-int.com", 130, ANY, True),
        CommandData(ANY, "curl -v  https://api.dota-int.com", 130, ANY, True),
#         CommandData(ANY, "curl -v  https://api.dota-int.com", 0, ANY, True),
        # CommandData(1616167901.768, "pycharm .", 0, pytest.approx(2.557, rel=1e-4), True),
        # CommandData(1616164367.385, "factory_db_prod", -999999, -1, False),
        # CommandData(1616164503.407, "amper_juypter", -999999, -1, False),
    ]

    matches = 0
    for command in commands:
        if command in required_commands:
            matches += 1

    assert matches == len(required_commands) 