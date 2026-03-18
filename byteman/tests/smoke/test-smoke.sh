#!/bin/bash
#
set -e

##############################################################
#
# Test 1: bmjava
#
##############################################################
test1_dir=$(mktemp -d)
pushd $test1_dir
#####
## The Java program under test (via bmjava)
#####
cat > HelloWait.java <<EOF1
public class HelloWait {

    public static class FooBar {
         public void doSomething(String arg) {
             System.out.println("Hello " + arg);
	 }
    }

    public static void main(String[] args) {
	FooBar fooBar = new FooBar();
        fooBar.doSomething("World!");
    }

}
EOF1
javac -g HelloWait.java
#####
## The byteman rule (used via bmjava)
#####
cat > trace1.btm <<EOF2
RULE trace doSomething entry
CLASS HelloWait\$FooBar
METHOD doSomething(java.lang.String)
AT ENTRY
IF true
DO
traceln("argument was: " + \$1);
\$1 = "bar";
ENDRULE
EOF2

bmjava -p 5555 -h 127.0.0.1 -l trace1.btm HelloWait > out1.log
grep -q "argument was: World!" out1.log
grep -q "Hello bar" out1.log
output=$(tail -n1 out1.log)
if [ ! "${output}_" == "Hello bar_" ]; then
   echo Test FAILED!
   exit 1
fi

echo Test 1 PASSED!

popd
rm -rf $test1_dir


##############################################################
#
# Test 2: bminstall + bmsubmit
#
##############################################################
test2_dir=$(mktemp -d)
pushd $test2_dir
#####
## The Java program under test
#####
cat > HelloWait.java <<EOF3
public class HelloWait {

    public static class FooBar {
         public void doSomething(String arg) {
             System.out.println("Hello " + arg);
	 }
    }

    public static void main(String[] args) {
	FooBar fooBar = new FooBar();
        try {
            while (true) {
		fooBar.doSomething("World!");
                Thread.sleep(300);
            }
        } catch (InterruptedException e) {
            // ignore
        }
    }

}
EOF3
javac -g HelloWait.java
java HelloWait > out2.log 2>&1 &
pid_of_java=$$
echo "Forked java process with pid $pid_of_java"
sleep 2
#####
## The byteman rule(s) (used via bmsubmit)
#####
cat > change_arg.btm <<EOF4
RULE change doSomething arg
CLASS HelloWait\$FooBar
METHOD doSomething(java.lang.String)
AT ENTRY
IF true
DO
\$1 = "THERE!";
ENDRULE
EOF4
cat > throw_excptn.btm <<EOF5
RULE throw exception when leaving doSomething
CLASS HelloWait\$FooBar
METHOD doSomething(java.lang.String)
AT EXIT
IF true
DO
THROW new RuntimeException("Boom!")
ENDRULE
EOF5

# Install the agent
bminstall -p 5555 -h 127.0.0.1 HelloWait
# Install the change arg rule
bmsubmit -p 5555 -h 127.0.0.1 -l change_arg.btm
sleep 2
# Unload the change arg rule
bmsubmit -p 5555 -h 127.0.0.1 -u change_arg.btm
# Install the exception throwing rule
bmsubmit -p 5555 -h 127.0.0.1 -l throw_excptn.btm
sleep 1

# Verify the log
head -n10 out2.log | grep -q "Hello World!"
hello_th_count=$(grep "Hello THERE!" out2.log | wc -l)
if [ $hello_th_count -lt 1 ]; then
    echo "Test 2 FAILED!"
    exit 1
fi
grep -q "Boom!" out2.log
grep -q "RuntimeException" out2.log
echo Test 2 PASSED!

popd
rm -rf $test2_dir
