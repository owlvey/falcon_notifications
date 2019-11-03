#!/usr/bin/env bash

coverage run -m unittest discover -s tests/unittest

coverage report -m --omit="*/test*"

coverage html --omit="*/test*" -d reports/unittest_coverage_report

