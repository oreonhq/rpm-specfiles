%global source0_hash 5ec89082d54f1a29d23fed54de70acab4375036d57828ff0fc7a88b81833d40f

Name: liblcf
Summary: Library to handle RPG Maker 2000/2003 game data

# liblcf itself is MIT, but it uses some example code
# from the BSD-licensed "inih" library, as well as
# some header-only C++ libraries, which are subject
# to the Boost License.
#
# BSD-licensed:
# - src/lcf/inireader.cpp
# - src/lcf/inireader.h
#
# Boost:
# - src/lcf/third_party/span.h
License: MIT AND BSD-2-Clause AND BSL-1.0

Version: 0.8.1
Release: 4%{?dist}

URL: https://github.com/EasyRPG/liblcf
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: expat-devel
BuildRequires: inih-devel
BuildRequires: libicu-devel

%description
%{name} is a library to handle RPG Maker 2000/2003 game data.
It can read and write LCF and XML files.

%{name} is part of the EasyRPG Project.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?isa} = %{version}-%{release}

Requires: inih-devel

%description devel
This package contains files required to develop applications using %{name}.

%package tools
Summary: Programs for handling RPG Maker 2000/2003 game data

%description tools
This package contains helper tools for working with
RPG Maker 2000/2003 data files:
- lcf2xml: converts RM2k data files to XML (and vice-versa)
- lcfstrings: extracts all strings from an RM2k data file

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains documentation (in HTML format) for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake \
	-DLIBLCF_UPDATE_MIMEDB=OFF \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build
%cmake_build --target liblcf_doc

%install
%cmake_install

%check
%cmake_build --target check

%files
%license COPYING
%{_libdir}/%{name}.so.*
%{_datadir}/mime/packages/%{name}*.xml

%files devel
%{_includedir}/lcf/
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/lcf2xml
%{_bindir}/lcfstrings

%files doc
%license COPYING
%doc doc/*

%changelog
%autochangelog
