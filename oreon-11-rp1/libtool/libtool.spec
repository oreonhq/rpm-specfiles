%global source0_hash 2ef1067c16c97db930fd740cc9bc3d3ba9a583804ae5ac42cc3e8719e49e191e
%global gcc_major  16
%global automake_version 1.18.1
%bcond_without check
Summary:        The GNU Portable Library Tool
Name:    libtool
Version: 2.6.2
Release:        1%{?dist}
License: GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND LGPL-2.0-or-later WITH Libtool-exception AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND MIT AND FSFAP AND FSFULLR AND FSFULLRWD AND GFDL-1.3-or-later AND X11 AND LicenseRef-Fedora-public-domain
URL:     http://www.gnu.org/software/libtool/
Source0:        https://mirrors.kernel.org/gnu/libtool/libtool-%{version}.tar.xz
Patch:  libtool-2.4.5-rpath.patch
%undefine _hardened_build
Patch: libtool-2.4.7-hardening.patch
Patch: libtool-2.4.6-disable_non-pic_arm.patch
Patch: riscv-non-PIC-into-shared-objects.patch
%if ! 0%{?_module_build}
Patch: libtool-nodocs.patch
%endif
Requires: gcc(major) = %{gcc_major}
Requires: autoconf, automake, sed, tar, findutils
%if ! 0%{?_module_build}
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  help2man
BuildRequires:  libstdc++-devel
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf
and GNU Automake).

%package ltdl
Summary:  Runtime libraries for GNU Libtool Dynamic Module Loader
Provides: %{name}-libs = %{version}-%{release}
License:  LGPL-2.0-or-later WITH Libtool-exception
%description ltdl
The libtool-ltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%package ltdl-devel
Summary: Tools needed for development using the GNU Libtool Dynamic Module Loader
Requires: automake = %automake_version
Requires: %{name}-ltdl = %{version}-%{release}
License:  LGPL-2.0-or-later WITH Libtool-exception
%description ltdl-devel
Static libraries and header files for development with ltdl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libtool-%{version} -p1

autoreconf -v

%build

%configure
%make_build \
    CUSTOM_LTDL_CFLAGS="%_hardening_cflags" \
    CUSTOM_LTDL_LDFLAGS="%_hardening_ldflags"
%check

%if %{with check}
make check VERBOSE=yes || { cat tests/testsuite.dir/*/testsuite.log ; false ; }
%endif
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/libltdl.{a,la}
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtool-ltdl -f %{oreon_filedir}/libtool-ltdl.list
%files -n libtool-ltdl-devel -f %{oreon_filedir}/libtool-ltdl-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.4-10
- Import
