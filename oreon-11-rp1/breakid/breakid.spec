%global source0_hash 42f56d70cdf9cc8bbdb8246761a43e2cd6ea33fb98faa4b1754e6c6f74686885
Name:           breakid
Version:        3.1.3
Release:        1%{?dist}
Summary:        Symmetry detecting and breaking library
License:        MIT
URL:            https://github.com/meelgroup/breakid
VCS:            git:%{url}.git
Source0:        https://github.com/meelgroup/%{name}/archive/release/%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-compiler-flags.patch
Patch:          %{name}-unbundle-bliss.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  bliss-devel
BuildRequires:  cmake
BuildRequires:  cmake(argparse)
BuildRequires:  gcc-c++
BuildRequires:  help2man
# /oreon:deps
%description
BreakID is a symmetry detecting and breaking library for SAT solvers.  It is
based on Jo Devriendt's BreakID code.  It has been re-licensed by the original
author to be MIT.  All modifications by Mate Soos.

%package        devel
Summary:        Development files for breakid
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bliss-devel%{?_isa}
%description    devel
Header files and library links for developing applications that use breakid.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-release-%{version} -p1

%conf
# Make sure the bundled bliss cannot be used
rm -fr src/bliss

# Unbundle argparse
rm src/argparse.hpp
ln -s %{_includedir}/argparse/argparse.hpp src/argparse.hpp

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build

%cmake -DBREAKID_INSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/breakid
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
cd %{_vpath_builddir}
help2man -N --version-string=%{version} ./breakid \
  -n 'Symmetry detection and breaking' \
  -o %{buildroot}%{_mandir}/man1/breakid.1
cd -
%oreon_autofiles breakid-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n breakid-devel -f %{oreon_filedir}/breakid-devel.list

%changelog

%autochangelog
