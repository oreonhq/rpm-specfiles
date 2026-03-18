#!/bin/bash -

set -e
set -x

po4a --help

# Write a test POD (Perl doc) file to the local directory.
cat >test.pod <<EOF
=head1 NAME

hello - hello world

=head1 DESCRIPTION

This is the hello world documentation

=head1 SEE ALSO

L<goodbye(1)>
EOF

cp test.pod local.pod

# Try to compile it into a POT file using po4a-gettextize:
po4a-gettextize -f pod -M utf-8 -L utf-8 \
                --package-name hello \
                --package-version 1.0 \
                --msgid-bugs-address noone@example.com \
                --copyright-holder "Red Hat Inc." \
                -p output.pot -m test.pod -l local.pod

cat output.pot

# Check for some expected strings in the output.
grep 'msgid "DESCRIPTION"' output.pot

grep 'msgid "This is the hello world documentation"' output.pot

# Clean up.
rm output.pot test.pod local.pod
