#!/bin/sh

# Generate colossus source tarball in current directory
# The desired rev should be used as a parameter.
# If a rev isn't provided, the current rev of HEAD is determined and
# is used instead.
# $REV[0] is the date of the commit for the build
# $REV[1] is the revision of the commit for the build
# If a rev is provided, you can also provide a branch. As time goes on
# I expect that the Colossus project will be doing more stable branches.
# Don't supply "trunk" as a branch, leave it unspecified instead.

# Location of SVN repository
if test -z "$2"
then
BRANCH=trunk/Colossus
BNAME=
else
BRANCH=branches/releases/Colossus-$2
BNAME=$2
fi
COLOSSUS=https://colossus.svn.sourceforge.net/svnroot/colossus/${BRANCH}

# First check if revision specified
if test -z "$1"
then
REV=(`svn info --xml --incremental $COLOSSUS | xsltproc colossus-rev.xsl -`)
else
REV=(`svn info -r $1 --xml --incremental $COLOSSUS | xsltproc colossus-rev.xsl -`)
fi

# Remove pre-existing source with the same rev
rm -rf colossus-${BNAME}-${REV[0]}-${REV[1]}.tar.gz colossus-${BNAME}-${REV[0]}-${REV[1]}

# Fetch source
svn export -q -r ${REV[1]} $COLOSSUS colossus-${BNAME}-${REV[0]}-${REV[1]}

# Remove included jar files
find colossus-${BNAME}-${REV[0]}-${REV[1]} -name '*.jar' | xargs rm -f

# Remove htdocs is just a copy of the project home page. This is also
# one less set of images to worry about.
rm -rf colossus-${BNAME}-${REV[0]}-${REV[1]}/htdocs

# This can be used to remove all of the unused images in the icons directory.
# It is not needed for now.
# find colossus-${BNAME}-${REV[0]}-${REV[1]}/core/src/main/resource/icons/ -type f \! -name ColossusIcon.png | xargs rm -f

# Build .tar.gz archive
tar czf colossus-${BNAME}-${REV[0]}-${REV[1]}.tar.gz colossus-${BNAME}-${REV[0]}-${REV[1]}

# Remove unarchived source
rm -rf colossus-${BNAME}-${REV[0]}-${REV[1]}
