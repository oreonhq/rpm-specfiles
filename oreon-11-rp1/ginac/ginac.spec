%global source0_hash 6cac1973a5325de0b9bcb8e392988ae95fbc37aa66c0f1f1d3b8e64c08cec1b9
%global so_ver 13
Name:             ginac
Version:          1.8.10
Release:        1%{?dist}
Summary:        C++ library for symbolic calculations
License:          GPL-2.0-or-later
URL:              https://www.ginac.de/
Source0:        https://www.ginac.de/%{name}-%{version}.tar.bz2
Patch:            cmake-minimum-version.diff
Obsoletes:        GiNaC < 1.3.2-999
Provides:         GiNaC = %{version}-%{release}
Provides:         GiNaC%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  cln-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  tex(dvips)
BuildRequires:  tex(latex)
BuildRequires:  tex(latex-base)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  transfig
# /oreon:deps
%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

%package          devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         cln-devel%{?_isa}
Obsoletes:        GiNaC-devel < 1.3.2-999
Provides:         GiNaC-devel = %{version}-%{release}
Provides:         GiNaC-devel%{?_isa} = %{version}-%{release}
%description      devel
This package contains libraries and header files for
developing applications that use %{name}.

%package          utils
Summary:          GiNaC-related utilities
Requires:         %{name}%{?_isa} = %{version}-%{release}
Obsoletes:        GiNaC-utils < 1.3.2
Provides:         GiNaC-utils = %{version}-%{release}
%description      utils
This package includes ginsh ("GiNaC interactive shell") which provides a
simple and easy-to-use CAS-like interface to GiNaC for non-programmers, and
the tool "viewgar" which displays the contents of GiNaC archives.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Destroy the RPATH.
sed -i 's| @GINACLIB_RPATH@||' ginac.pc.{in,cmake}

%build

%cmake -DCMAKE_INSTALL_RPATH="" -DLIBEXECDIR=%{_libexecdir}
%cmake_build
%cmake_build --target ginac_html
%install
%cmake_install
rm -frv %{buildroot}%{_infodir}/dir
find %{buildroot} -name '*.la' -delete -print
for f in $(find %{buildroot} -name "*.py") ; do
  sed -i.orig "s:^#\!/usr/bin/env\s\+python:#!%{__python3}:" $f
  touch -r $f.orig $f
  rm $f.orig
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export CTEST_OUTPUT_ON_FAILURE=1
%cmake_build --target check
%files -f %{oreon_filedir}/main.list
%files -n ginac-devel -f %{oreon_filedir}/ginac-devel.list
%files -n ginac-utils -f %{oreon_filedir}/ginac-utils.list

%changelog

%autochangelog
