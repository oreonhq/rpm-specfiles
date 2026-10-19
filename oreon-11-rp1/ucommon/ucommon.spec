%global source0_hash 6ac9f76c2af010f97e916e4bae1cece341dc64ca28e3881ff4ddc3bc334060d7
Name:          ucommon
Version:       7.0.0
Release:        27%{?dist}
Summary:        Portable C++ framework for threads and sockets
License:       LGPL-3.0-or-later
URL:           http://www.gnu.org/software/commoncpp
Source0:        https://ftpmirror.gnu.org/commoncpp/ucommon-%{version}.tar.gz
Patch0:        ucommon_cmakever.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  graphviz-gd
# /oreon:deps
%description
GNU uCommon C++ is a lightweight library to facilitate using C++ design
patterns even for very deeply embedded applications, such as for systems using
uclibc along with POSIX threading support. For this reason, uCommon disables
language features that consume memory or introduce runtime overhead. UCommon
introduces some design patterns from Objective-C, such as reference counted
objects, memory pools, and smart pointers. UCommon introduces some new concepts
for handling of thread locking and synchronization.  Starting with release
5.0, GNU uCommon also bundles GNU Common C++ libraries.

%package bin
Summary:       GNU uCommon system and support applications
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description bin
This is a collection of command line tools that use various aspects of the
ucommon library. Some may be needed to prepare files or for development of
applications.

%package devel
Summary:       Headers for building GNU uCommon applications
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      openssl-devel%{?_isa}
Requires:      pkgconfig
%description devel
This package provides header and support files needed for building
applications that use the uCommon and commoncpp libraries.

%package doc
Summary: Generated class documentation for GNU uCommon
%description doc
Generated class documentation for GNU uCommon library from header files in
HTML format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="-std=c++14 %{optflags}"
%cmake -DBUILD_DOCS=ON
%cmake_build
%cmake_build --target doc
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ucommon-bin -f %{oreon_filedir}/ucommon-bin.list
%files -n ucommon-devel -f %{oreon_filedir}/ucommon-devel.list
%files -n ucommon-doc -f %{oreon_filedir}/ucommon-doc.list

%changelog

%autochangelog
