%global source2_hash e272b0c7f128468f7c46bf8e6bbd480675b6469f22cedb4aa12fb3ee06d32f83

%global source1_hash 0077954716ab488b2dbb301b3d411697b83a3c489ffc4e1eb3bb676d53718cf7

%global source0_hash b6bd32964cbe451be2838822c9d200b7c7e76a2a5947c03feb71dc6bd72988bd

Summary:       The NetBSD make(1) tool
Name:          bmake
Version:       20260912
Release:       %autorelease
License:       BSD-3-Clause AND BSD-4-Clause-UC AND BSD-2-Clause
URL:           https://ftp.netbsd.org/pub/NetBSD/misc/sjg/
Source0:       %{url}/bmake-%{version}.tar.gz
Source1:       %{url}/bmake-%{version}.tar.gz.asc
Source2:       https://www.crufty.net/ftp/pub/sjg/Crufty.pub.asc

Requires:      mk-files

#Patch1:       

BuildRequires: gcc
BuildRequires: sed
BuildRequires: util-linux
# Required by tests
BuildRequires: tcsh ksh
%if 0%{?fedora}
# source verification
BuildRequires: gnupg2
%endif

%description
bmake, the NetBSD make tool, is a program designed to simplify the
maintenance of other programs.  The input of bmake is a list of specifications
indicating the files upon which the targets (programs and other files) depend.
bmake then detects which targets are out of date based on their dependencies
and triggers the necessary commands to bring them up to date when that happens.

bmake is similar to GNU make, even though the syntax for the advanced features
supported in Makefiles is very different.

%package -n mk-files
Summary:   Support files for bmake, the NetBSD make(1) tool
BuildArch: noarch

%description -n mk-files
The mk-files package provides some bmake macros derived from the NetBSD
bsd.*.mk macros.  These macros allow the creation of simple Makefiles to
build all kinds of targets, including, for example, C/C++ programs and/or
shared libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -n %{name} -p1
sed -i.python -e '1 s|^#!/usr/bin/env python|#!/usr/bin/python3|' mk/meta2deps.py

%build
%configure --with-default-sys-path=%{_datadir}/mk
sh ./make-bootstrap.sh

%install
./bmake -m mk install DESTDIR="%{buildroot}" INSTALL='install -p' STRIP_FLAG=''
chmod a-x %{buildroot}%{_datadir}/mk/mkopt.sh

%files
%doc ChangeLog README
%license LICENSE
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*

%files -n mk-files
%license LICENSE
%doc mk/README
%{_datadir}/mk

%changelog
%autochangelog
