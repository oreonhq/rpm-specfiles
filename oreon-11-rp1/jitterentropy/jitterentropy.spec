%global source0_hash e2af325cdc7d951a66af782fad4bcdd622e9d8355dd024b7562e2f8b3f6079cd

%global libjit_soversion 3
Name:           jitterentropy
Version:        3.6.0
Release:        4%{?dist}
Summary:        Library implementing the jitter entropy source

License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/smuellerDD/jitterentropy-library
Source0:        https://github.com/smuellerDD/jitterentropy-library/archive/v3.6.0/jitterentropy-library-3.6.0.tar.gz

BuildRequires: gcc
BuildRequires: make

# Disable Upstream Makefiles debuginfo strip on install
Patch0: jitterentropy-rh-makefile.patch

%description
Library implementing the CPU jitter entropy source

%package devel
Summary: Development headers for jitterentropy library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for jitterentropy

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p0 -n %{name}-library-%{version}

%build
%set_build_flags
%make_build

%install
mkdir -p %{buildroot}/usr/include/
%make_install PREFIX=/usr LIBDIR=%{_lib}

%files
%doc README.md CHANGES.md
%license LICENSE LICENSE.bsd LICENSE.gplv2
%{_libdir}/libjitterentropy.so.%{libjit_soversion}*

%files devel
%{_includedir}/*
%{_libdir}/libjitterentropy.so
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.0-4
- Prepare for Oreon 11 (RP1)
