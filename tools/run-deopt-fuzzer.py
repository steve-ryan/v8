#!/usr/bin/env python
#
# Copyright 2017 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


import sys

from testrunner import deopt_fuzzer


if __name__ == "__main__":
  sys.exit(deopt_fuzzer.DeoptFuzzer().execute())