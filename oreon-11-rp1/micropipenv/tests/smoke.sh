#!/bin/bash
set -ex

username="test_$$"
id "$username" && userdel -rf "$username"

useradd "$username"
su -l -c "echo simple-manylinux-demo > requirements.txt" "$username"
su -l -c "micropipenv install -- --user" "$username"
su -l -c "python3 -c 'from dummyextension.extension import hello; assert hello() == \"Hello from Python extension!\"'" "$username"

userdel -rf "$username"
