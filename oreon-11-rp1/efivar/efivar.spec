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
# please don't fix this to reflect github's incomprehensible url that goes
# to a different tarball.
Source0:        https://github.com/rhboot/efivar/releases/download/%{version}/efivar-%{version}.tar.bz2
Source1:        efivar.patches

# include patches
%include %{SOURCE1}

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 39-12
- Prepare for Oreon 11 (RP1)
