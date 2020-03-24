#!/usr/bin/env python3
# coding=utf-8

import {{cookiecutter.project_slug}}


def test_todo() -> None:
    assert "TODO: Make tests" != {{cookiecutter.project_slug}}.__version__
