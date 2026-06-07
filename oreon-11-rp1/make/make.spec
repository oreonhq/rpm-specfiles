%global source0_hash none

# -*- coding: utf-8 -*-
# This decides the SRPM name.  Set to "make" for a rolling release
# (like Fedora) or "make-latest" for a long term release that needs
# optional versioned updates.
Name: make
Epoch: 1
Version: 4.4.1
Release: 12%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND GFDL-1.3-or-later AND FSFULLR
URL: https://www.gnu.org/software/make/
Source:        https://mirrors.kernel.org/gnu/make/make-%{version}.tar.gz

%if "%{name}" != "make"
# Set this to the sub-package base name, for "make-latest"
%global make %(echo make%{version} | tr -d .)
%if 0%{?rhel} > 0
%global _prefix /opt/rh/%{make}
%else
# We intentionally do not define a case for Fedora, as it should not
# need this functionality, and letting it error avoids accidents.
%{error:"Each downstream must specify its own /opt namespace"}
%endif
Summary: Meta package to include latest version of make
%else
%global make %{name}
Summary: A GNU tool which simplifies the build process for users
Provides:   make-latest = %{version}-%{release}
Provides:   %(echo make%{version} | tr -d .) = %{version}-%{release}
%endif

# This gives the user the option of saying --with guile, but defaults to WITHOUT
%bcond_with guile

Patch0: make-4.3-getcwd.patch

# Assume we don't have clock_gettime in configure, so that
# make is not linked against -lpthread (and thus does not
# limit stack to 2MB).
Patch1: make-4.0-noclock_gettime.patch

# BZs #142691, #17374
Patch2: make-4.3-j8k.patch

# autoreconf
BuildRequires: make
BuildRequires: autoconf, automake, gettext-devel
BuildRequires: procps
BuildRequires: perl
%if %{with guile}
BuildRequires: pkgconfig(guile-3.0)
%endif
BuildRequires: gcc

%if "%{name}" != "make"
# We're still on the make-latest package
Requires: %{make}
%description -n make-latest
The latest GNU Make, with a version-specific install
%files -n make-latest

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

%check
echo ============TESTING===============
/usr/bin/env LANG=C make check && true
echo ============END TESTING===========

%files -n %{make} -f make.lang
%license COPYING
%doc NEWS README AUTHORS
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/*.info*
%{_includedir}/gnumake.h
%if "%{name}" != "make"
/etc/scl/prefixes/%{make}
%{_prefix}/enable
%endif

%files -n %{make}-devel
%{_includedir}/gnumake.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4.1-12
- Prepare for Oreon 11 (RP1)
