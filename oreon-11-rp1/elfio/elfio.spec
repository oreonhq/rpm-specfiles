%global source0_hash caf49f3bf55a9c99c98ebea4b05c79281875783802e892729eea0415505f68c4

%global debug_package %{nil}

Name:           elfio
Version:        3.12
Release:        %autorelease
Summary:        C++ library for reading and generating ELF files

# This is the proper SPDX license
License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz
# Add missing includes - fixes FTBFS rhbz 2340118
# https://github.com/serge1/ELFIO/pull/148
Patch0:         elfio-includes.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

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

%autosetup -p1

%build
%cmake -DELFIO_BUILD_EXAMPLES=ON
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/docs

%check
# Sanity check
%{_vpath_builddir}/examples/elfdump/elfdump %{_bindir}/cmake

%files devel
%license LICENSE.txt
%doc doc/elfio.pdf README.md
%{_includedir}/elfio/
%{_datadir}/elfio/

%changelog
%autochangelog
