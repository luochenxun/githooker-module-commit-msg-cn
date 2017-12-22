#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess
import os
import pickle
import base64
import re


''' ---------- Hook method ---------- '''
pCommitMessage = ''  # git commit message
# the git-project's name(for https://https://github.com/xx/usefulTool.git is usefulTool)
pProjectName = ''
pProjectPath = ''    # the git-project's path


def hook():
    """
    Write your main hook logic here, and you can use the prepared global member as 'pCommitMessage'、'pProjectName' and so on.

    call _pass() if you want to pass the git action, and _failed() if you want to failed the action.
    """
    global pCommitMessage
    regStr = "^\[.*\]"
    if re.match(regStr,pCommitMessage) is None:
        print("提交格式必须为: '[模块名/Bug号] 提交内容描述'");
        _failed()
    _pass()
    # ... process the pCommitMessage and so on.
    # if success:
    #     _pass()
    # else:
    #     _failed()


''' ---------- Private methods ---------- '''

# init some global variables of git environment


def _initGitInfo():
    global pCommitMessage, pProjectName, pProjectPath
    pCommitMessage = os.popen('git log -1 --pretty=format:"%s"').read()
    pProjectName = os.popen(
        "git remote -v | sed -n \'1 s|\(.*\)/\(.*\).git\(.*\)|\\2|g p\'").read().replace("\n", "")
    pProjectPath = os.popen("pwd").read().replace("\n", "")


def _pass():
    os._exit(0)


def _failed():
    os._exit(1)


def _loadArgs(args_str):
    """ use to pass param through scripts """
    return pickle.loads(base64.decodestring(args_str))


def main():
    _initGitInfo()
    hook()


if __name__ == "__main__":
    main()
