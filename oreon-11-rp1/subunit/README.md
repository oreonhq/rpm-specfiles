# subunit

[Subunit](https://launchpad.net/subunit) is a streaming protocol for test
results.  The protocol is a binary encoding that is easily generated and
parsed.  By design all the components of the protocol conceptually fit into
the xUnit `TestCase -> TestResult` interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell.  Bindings are easy to write
for other languages.

A number of useful things can be done easily with subunit:
- Test aggregation: Tests run separately can be combined and then
  reported/displayed together.  For instance, tests from different languages
  can be shown as a seamless whole.
- Test archiving: A test run may be recorded and replayed later.
- Test isolation: Tests that may crash or otherwise interact badly with each
  other can be run separately and then aggregated, rather than interfering with
  each other.
- Grid testing: subunit can act as the necessary serialization and
  deserialization to get test runs on distributed machines to be reported in
  real time.
