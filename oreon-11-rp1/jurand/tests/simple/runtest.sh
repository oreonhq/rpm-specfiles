#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartSetup
    rlAssertRpm jurand
  rlPhaseEnd

  rlPhaseStartTest
    rlAssertGrep "^import com.Foo;$" test_template.java
    rlAssertGrep "^import biz.Bar;$" test_template.java
    rlAssertGrep "^@Foo$" test_template.java
    rlAssertGrep "^class test{}$" test_template.java

    rlRun "cp test_template.java test.java"
    rlRun -s "jurand -i test.java -n Foo"
    rlAssertNotGrep "^import com.Foo;$" test.java
    rlAssertGrep "^import biz.Bar;$" test.java
    rlAssertGrep "^@Foo$" test.java
    rlAssertGrep "^class test{}$" test.java

    rlRun "cp test_template.java test.java"
    rlRun -s "jurand -i -a test.java -n Foo"
    rlAssertNotGrep "^import com.Foo;$" test.java
    rlAssertGrep "^import biz.Bar;$" test.java
    rlAssertNotGrep "^@Foo$" test.java
    rlAssertGrep "^class test{}$" test.java
  rlPhaseEnd

  rlPhaseStartCleanup
    rlRun "rm -f test.java"
  rlPhaseEnd
rlJournalEnd
rlJournalPrintText
