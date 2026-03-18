#!/bin/bash -x

# Copyright (c) 2015 Red Hat, Inc. This copyrighted material
# is made available to anyone wishing to use, modify, copy, or
# redistribute it subject to the terms and conditions of the GNU General
# Public License v.2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Author: Vladimir Benes <vbenes@redhat.com>

PKG=dbus-glib
PKG_DIR=$2
if [ -z "$PKG_DIR" ]; then
  PKG_DIR=$1
fi

RPMBUILD=$(rpm --eval '%{_topdir}')
LOG="/tmp/$TEST.log"
PKG_SRPM=$(rpm -q --qf '%{SOURCERPM}\n' $PKG | head -n1)
PKG_PATH=$(rpm -q --qf '%{NAME}/%{VERSION}/%{RELEASE}\n' $PKG | head -n1)
PKG_BUILD_PATH=$(rpm -q --qf "$PKG_DIR-%{VERSION}\n" $PKG | head -n1)

echo "Downloading SRPM"
wget https://kojipkgs.fedoraproject.org/packages/$PKG_PATH/src/$PKG_SRPM
rm -rf $RPMBUILD
rpm -ivf $PKG_SRPM
echo "Building dependencies"
dnf builddep -y $PKG_SRPM
echo "Rebuilding the package"
rpmbuild -bc $RPMBUILD/SPECS/$PKG.spec

echo "Running make check"
#make check -C $RPMBUILD/BUILD/$PKG_BUILD_PATH/ &>$LOG
cd $RPMBUILD/BUILD/$PKG*
make check | tee -a $LOG
#make check -C $RPMBUILD/BUILD/$PKG_BUILD_PATH/ 
rc=$?
RESULT=FAIL

if [ $rc -eq 0 ]; then
  RESULT="PASS"
fi

if which rhts-report-result &> /dev/null; then
   rhts-report-result $TEST $RESULT $LOG
fi

exit $rc
echo "Result is: $RESULT"
rm $LOG

