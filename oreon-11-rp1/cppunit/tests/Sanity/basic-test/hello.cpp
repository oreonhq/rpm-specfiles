#include <iostream>

#include <cppunit/TestRunner.h>
#include <cppunit/TestResult.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/BriefTestProgressListener.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/CompilerOutputter.h>
#include <cppunit/XmlOutputter.h>

using namespace std;

class Math
{
public:
  int Addition (int x, int y);
};

int
Math::Addition (int x, int y)
{
  return (x + y);
}

class Test:public
  CPPUNIT_NS::TestCase
{
  CPPUNIT_TEST_SUITE (Test);
  CPPUNIT_TEST (testAddition);
  CPPUNIT_TEST_SUITE_END ();

public:
  void
  setUp (void);
  void
  tearDown (void);

protected:
  void
  testAddition (void);

private:
  Math *
    mTestObj;
};

void
Test::testAddition (void)
{
  CPPUNIT_ASSERT (5 == mTestObj->Addition (2, 3));
}

void
Test::setUp (void)
{
  mTestObj = new Math ();
}

void
Test::tearDown (void)
{
  delete mTestObj;
}

CPPUNIT_TEST_SUITE_REGISTRATION (Test);

int
main (int ac, char **av)
{
  CPPUNIT_NS::TestResult controller;

  CPPUNIT_NS::TestResultCollector result;
  controller.addListener (&result);

  CPPUNIT_NS::BriefTestProgressListener progress;
  controller.addListener (&progress);

  CPPUNIT_NS::TestRunner runner;
  runner.
    addTest (CPPUNIT_NS::TestFactoryRegistry::getRegistry ().makeTest ());
  runner.run (controller);

  CPPUNIT_NS::CompilerOutputter compileroutputter (&result, std::cerr);
  compileroutputter.write ();

  ofstream xmlFileOut ("output.xml");
  CPPUNIT_NS::XmlOutputter xmlOut (&result, xmlFileOut);
  xmlOut.write ();

  return result.wasSuccessful ()? 0 : 1;
}
