%global source0_hash c9edd15f2eeeea63232f3e669a48e992c7be9aff57ee22672ac31f5eca1609a6

Name:           efivar
Version:        39
Release:        12%{?dist}
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
URL:            https://github.com/rhboot/efivar
Requires:       %{name}-libs = %{version}-%{release}
ExclusiveArch:  %{efi}

BuildRequires:  gcc
BuildRequires:  efi-srpm-macros git glibc-static libabigail
BuildRequires:  make
BuildRequires:  mandoc
BuildRequires:  git
# Upstream release 39+ ships no release artifact, only the tag archive.
Source0:        https://github.com/rhboot/efivar/releases/download/%{version}/efivar-%{version}.tar.bz2

# Was efivar.patches (%%include needs SOURCES at parse time for spectool)
Patch0001: 0001-ABI-update-for-newer-libabigail.patch
Patch0002: 0002-ABI-update-after-glibc-changes.patch
Patch0003: 0003-ABI-update-after-glibc-changes.patch
Patch0004: 0004-efivarfs-Update-a-file-variable-store-On-SetVariable.patch

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package libs
Summary: Library to manage UEFI variables

%description libs
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary: Development headers for libefivar
Requires: %{name}-libs = %{version}-%{release}

%description devel
development headers required to use libefivar.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}
git init
git config user.email "%{name}-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

%build
# This package implements symbol versioning with toplevel ASM statments which is
# incompatible with LTO.  Disable LTO
%define _lto_cflags %{nil}

make LIBDIR=%{_libdir} BINDIR=%{_bindir} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
%makeinstall CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
install -m 0644 src/abignore %{buildroot}%{_includedir}/efivar/.abignore

%check
%ifarch x86_64
make abicheck CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%endif

%ldconfig_scriptlets libs

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md
%{_bindir}/efivar
%{_bindir}/efisecdb
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%license COPYING
%{_libdir}/*.so.*

%changelog
* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 39-12
- Source0 from GitHub tag archive (release has no uploaded tarball)
- Inline patch list, drop %%include efivar.patches for spectool

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 39-12
- Prepare for Oreon 11 (RP1)
