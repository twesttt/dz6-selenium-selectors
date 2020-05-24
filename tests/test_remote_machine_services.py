#!/usr/bin/env python


def test_connect_ssh(connect_ssh):
    stdin, stdout, stderr = connect_ssh.exec_command("ls -l")
    data = stdout.read() + stderr.read()
    print(data.decode("utf-8"))


