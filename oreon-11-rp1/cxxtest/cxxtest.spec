%global source0_hash 1c154fef91c65dbf1cd4519af7ade70a61d85a923b6e0c0b007dc7f4895cf7d8
Name:           cxxtest
Version:        4.4
Release:        1%{?dist}
Summary:        A JUnit-like testing framework for C++
License:        LGPL-3.0-only
URL:            https://cxxtest.com
Source0:        https://github.com/CxxTest/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-shebang.patch
Patch1:         %{name}-include-anchors.patch
Patch2:         %{name}-tracker-typo.patch
Patch3:         %{name}-is-equals.patch
Patch4:         %{name}-escapes.patch
Patch5:         %{name}-classifiers.patch
BuildArch:      noarch
Requires:       python3-ply
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cxxtest = %{version}-%{release}
# /oreon:deps
%description
CxxTest is a unit testing framework for C++ that is similar in spirit to
JUnit, CppUnit, and xUnit. CxxTest is easy to use because it does not require
precompiling a CxxTest testing library, it employs no advanced features of
C++ (e.g. RTTI) and it supports a very flexible form of test discovery.

%package doc
Summary:        Documentation on how to use CxxTest
Requires:       %{name} = %{version}-%{release}
%description doc
This package contains the documentation on how to use CxxTest.
It also provides code examples.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

rm -f doc/images/icons/README
# remove Windows-related stuff
rm -rf sample/msvc/
rm -f sample/Makefile.bcc32
# remove Python 2 sources
rm -rf python/cxxtest/

find . -name ".cvsignore" -delete
sed -i "s|^PY = python$|PY = %{python3}|" doc/Makefile

%build

cd python
%pyproject_wheel
cd ..
cat <<EOF >%{name}.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}/%{name}
Name: %{name}
Description: A JUnit-like testing framework for C++
Version: %{version}
Cflags: -I\${includedir}
EOF
cd doc
cat <<EOF >create_manpage.py
import sys
sys.path.insert(0, '../python/python3')
import cxxtest
cxxtest.create_manpage()
EOF
%{python3} create_manpage.py
a2x -f manpage cxxtestgen.1.txt
make pdf html
%install
mkdir -p %{buildroot}%{_includedir}/cxxtest
install -D -p -m 644 cxxtest/* %{buildroot}%{_includedir}/cxxtest
install -D -p -m 644 %{name}.pc %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
cd python
%pyproject_install
cd ..
install -D -p -m 644 doc/cxxtestgen.1 %{buildroot}%{_mandir}/man1/cxxtestgen.1
%oreon_autofiles cxxtest-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n cxxtest-doc -f %{oreon_filedir}/cxxtest-doc.list

%changelog

%autochangelog
