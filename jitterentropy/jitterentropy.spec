%global libjit_soversion 3
Name:           jitterentropy
Version:        3.6.0
Release:        4%{?dist}
Summary:        Library implementing the jitter entropy source

License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/smuellerDD/jitterentropy-library
Source0:        %{url}/archive/v%{version}/%{name}-library-%{version}.tar.gz

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
