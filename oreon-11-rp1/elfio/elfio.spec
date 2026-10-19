%global source0_hash caf49f3bf55a9c99c98ebea4b05c79281875783802e892729eea0415505f68c4
%global debug_package %{nil}
Name:           elfio
Version:        3.12
Release:        1%{?dist}
Summary:        C++ library for reading and generating ELF files
License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz
Patch0:         elfio-includes.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch
%description devel
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DELFIO_BUILD_EXAMPLES=ON
%cmake_build
%install
%cmake_install
rm -r %{buildroot}%{_datadir}/docs
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/examples/elfdump/elfdump %{_bindir}/cmake
%files -f %{oreon_filedir}/main.list
%files -n elfio-devel -f %{oreon_filedir}/elfio-devel.list

%changelog

%autochangelog
