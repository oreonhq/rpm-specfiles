%global source0_hash 87daefacd7958b4a69f88c6856dbd1634261963c414079d0c371f589cd66a2e3

Summary: A front end for testing other programs
Name: dejagnu
Version: 1.6.3
Release: 15%{?dist}
Epoch: 1
# Note: baseboards/riscv-sim.exp is GPL 2.0 or later
# GFDL-1.3-or-later: Everything in doc/
License: GPL-3.0-or-later AND GFDL-1.3-or-later
Source:        https://ftp.gnu.org/gnu/dejagnu/dejagnu-%{version}.tar.gz
URL: http://www.gnu.org/software/dejagnu/
Requires: expect
BuildArch: noarch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: expect texinfo
BuildRequires: make

Patch0: rhbz460153.patch

%description
DejaGnu is an Expect/Tcl based framework for testing other programs.
DejaGnu has several purposes: to make it easy to write tests for any
program; to allow you to write tests which will be portable to any
host or target where a program must be tested; and to standardize the
output format of all tests (making it easier to integrate the testing
into software development).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1

%build
%configure -v

%check
echo ============TESTING===============
TMP=`mktemp`
export SCREENDIR=`mktemp -d`
# Skip selected tests.  Failed testcases reported upstream:
# https://lists.gnu.org/archive/html/dejagnu/2021-09/msg00001.html
(make check RUNTESTFLAGS="--ignore pr48155.exp stats.exp"; echo $?) >> $TMP
RESULT=`tail -n 1 $TMP`
cat $TMP
rm -f $TMP
rm -rf $SCREENDIR
echo ============END TESTING===========
exit $RESULT

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
chmod a-x $RPM_BUILD_ROOT/%{_datadir}/dejagnu/runtest.exp
make DESTDIR=$RPM_BUILD_ROOT install-man
install -D -m 644 doc/dejagnu.info $RPM_BUILD_ROOT/%{_infodir}/%{name}.info

%files
%doc COPYING NEWS README AUTHORS ChangeLog doc/dejagnu.texi
%{_bindir}/runtest
%{_bindir}/dejagnu
%{_datadir}/dejagnu
%{_includedir}/dejagnu.h
%{_mandir}/*/*
%{_infodir}/dejagnu*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.3-15
- Prepare for Oreon 11 (RP1)
