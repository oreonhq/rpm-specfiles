%global source0_hash 5556deb5081fb246ee92afae73efd943c889cef0cafea92b0b82422d6a18f289
Name:           tinyxml2
Version:        11.0.0
%global so_version 11
Release:        1%{?dist}
Summary:        Simple, small and efficient C++ XML parser
License:        Zlib
SourceLicense:  %{license} AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://github.com/leethomason/tinyxml2
Source0:        https://github.com/leethomason/tinyxml2/archive/refs/tags/11.0.0.tar.gz#/tinyxml2-11.0.0.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be easily
integrated into other programs. It uses a Document Object Model (DOM), meaning
the XML data is parsed into a C++ objects that can be browsed and manipulated,
and then written to disk or another output stream.

TinyXML-2 doesn’t parse or use DTDs (Document Type Definitions) nor XSLs
(eXtensible Stylesheet Language).

TinyXML-2 uses a similar API to TinyXML-1, But the implementation of the parser
was completely re-written to make it more appropriate for use in a game. It
uses less memory, is faster, and uses far fewer memory allocations.

%package devel
Summary:        Development files for tinyxml2
Requires:       tinyxml2%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
This package contains the libraries and header files that are needed
for writing applications with the tinyxml2 library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Demonstrate that bundled JS/CSS sources from pre-rendered HTML documentation
# do not contribute to the binary RPMs:
rm -rv docs/

%conf
%cmake \
    -Dtinyxml2_BUILD_TESTING:BOOL=ON \
    -Dtinyxml2_INSTALL_PKGCONFIG:BOOL=ON

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n tinyxml2-devel -f %{oreon_filedir}/tinyxml2-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11.0.0-1
- Prepare for Oreon 11 (RP1)
