%global source0_hash 95f24de663321a86d2cdef28e085f23d7604086e7bd4218782353b2e65d943bc
%global giturl  https://github.com/scipopt/zimpl
Name:           zimpl
Version:        3.7.1
Release:        1%{?dist}
Summary:        Zuse Institut Mathematical Programming Language
License:        LGPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:            https://zimpl.zib.de/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-shared.patch
Patch:          %{name}-cddlib-set-clash.patch
Patch:          %{name}-zlib-ng.patch
Patch:          %{name}-test-bsearch.patch
ExcludeArch:    %{ix86}
Requires:       libzimpl%{?_isa} = %{version}-%{release}
%global _desc %{expand:Zimpl is a little language to translate the mathematical model of a problem
into a linear or nonlinear (mixed-) integer mathematical program expressed in
.lp or .mps file format which can be read and (hopefully) solved by a LP or
MIP solver.}
# oreon:deps
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib-ng)
# /oreon:deps
%description
%_desc

This package contains a command-line tool to access ZIMPL functionality.

%package -n     libzimpl
License:        LGPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
Summary:        Zuse Institut Mathematical Programming Language
%description -n libzimpl
%_desc

This package contains a library interface to ZIMPL functionality.

%package -n     libzimpl-devel
License:        LGPL-3.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
Summary:        Headers and library links for libzimpl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libzimpl%{?_isa} = %{version}-%{release}
%description -n libzimpl-devel
This package contains headers and library links for developing applications
that use libzimpl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Avoid warnings about obsolete invocations of grep
sed -i 's/fgrep/grep -F/' check/check.sh

%build

export CFLAGS='%{build_cflags} -DFREEMEM -DNO_MSHELL'
export CXXFLAGS='%{build_cxxflags} -DFREEMEM -DNO_MSHELL'
%cmake
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/zimpl.man %{buildroot}%{_mandir}/man1/zimpl.1
rm -fr %{buildroot}%{_datadir}/licenses
%ifnarch %{power64}
%oreon_autofiles libzimpl usr/*/lib*.so.*
%oreon_autofiles libzimpl-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
cd check
sh check.sh ../%{_vpath_builddir}/bin/zimpl
cd -
%endif
%files -f %{oreon_filedir}/main.list
%files -n libzimpl -f %{oreon_filedir}/libzimpl.list
%files -n libzimpl-devel -f %{oreon_filedir}/libzimpl-devel.list

%changelog

%autochangelog
