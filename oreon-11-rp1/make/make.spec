%global source0_hash dd16fb1d67bfab79a72f5e8390735c49e3e8e70b4945a15ab1f81ddb78658fb3
Name: make
Epoch: 1
Version: 4.4.1
Release:        12%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND GFDL-1.3-or-later AND FSFULLR
URL: https://www.gnu.org/software/make/
Source0:        https://mirrors.kernel.org/gnu/make/make-%{version}.tar.gz
%if "%{name}" != "make"
%global make %(echo make%{version} | tr -d .)
%{error:"Each downstream must specify its own /opt namespace"}
Summary:        A GNU tool which simplifies the build process for users
%else
%global make %{name}
Summary:        A GNU tool which simplifies the build process for users
Provides:   make-latest = %{version}-%{release}
Provides:   %(echo make%{version} | tr -d .) = %{version}-%{release}
%endif
%bcond_with guile
Patch0: make-4.3-getcwd.patch
Patch1: make-4.0-noclock_gettime.patch
Patch2: make-4.3-j8k.patch
%if %{with guile}
%endif
%if "%{name}" != "make"
Requires: %{make}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  procps
# /oreon:deps
%description -n make-latest
The latest GNU Make, with a version-specific install

%package -n %{make}
Summary: A GNU tool which simplifies the build process for users
%endif
%description -n %{make}
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%package -n %{make}-devel
Summary: Header file for externally visible definitions
%description -n %{make}-devel
The %{make}-devel package contains gnumake.h.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n make-%{version} -p1

rm -f tests/scripts/features/parallelism.orig

%build

autoreconf -vfi
%configure \
%if %{with guile}
    --with-guile
%else
    --without-guile
%endif
%make_build
%install
%make_install
ln -sf make ${RPM_BUILD_ROOT}/%{_bindir}/gmake
ln -sf make.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/gmake.1
rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir
%if "%{name}" != "make"
install -d -m 755 ${RPM_BUILD_ROOT}/etc/scl/prefixes
dirname %{_prefix} > %{make}.prefix
install -p -m 644 %{make}.prefix ${RPM_BUILD_ROOT}/etc/scl/prefixes/%{make}
echo "export PATH=%{_prefix}/bin:\$PATH" > enable.scl
install -p -m 755 enable.scl ${RPM_BUILD_ROOT}/%{_prefix}/enable
%endif
%find_lang make
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

echo ============TESTING===============
/usr/bin/env LANG=C make check && true
echo ============END TESTING===========
%if "%{name}" != "make"
%files -f %{oreon_filedir}/main.list
%files -n make-devel -f %{oreon_filedir}/make-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.1-12
- Prepare for Oreon 11 (RP1)
%endif
