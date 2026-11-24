# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 84e413fa9a1bc4e2607ecc0e51add363e1bc5ad42f7cc5baec7b253e8f685ad3
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global somajor 4

%bcond_with tests

Name:           librist
Version:        0.2.11
Release:        1%{?dist}
Summary:        Library for Reliable Internet Stream Transport (RIST) protocol

License:        BSD-2-Clause and ISC
URL:            https://code.videolan.org/rist/librist
Source0:        %{url}/-/archive/v%{version}/librist-v%{version}.tar.gz

Patch0:         gcc16-fix-const-correctness.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  libcmocka-devel
BuildRequires:  gnutls-devel
BuildRequires:  nettle-devel
BuildRequires:  pkgconfig(libcjson)

%description
A library that can be used to speak the RIST protocol (as defined by Video
Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Technical documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains technical documentation for
developing applications that use %{name}.

%package -n     rist-tools
Summary:        User tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n rist-tools
This package contains the user tools for the RIST protocol library.

%prep
%oreon_sha256
%autosetup -n %{name}-v%{version} -p1

%build
%meson -Duse_nettle=true -Duse_mbedtls=false
%meson_build

%install
%meson_install
chmod -x %{buildroot}%{_includedir}/%{name}/*.h
chmod -x docs/*

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -av docs/* %{buildroot}%{_docdir}/%{name}

%if %{with tests}
%check
%meson_test
%endif

%files
%doc README.md CONTRIBUTING.md
%license COPYING
%{_libdir}/*.so.%{somajor}{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%license COPYING
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/VSF_TR-06-1.pdf
%doc %{_docdir}/%{name}/VSF_TR-06-2.pdf
%doc %{_docdir}/%{name}/librist_logo.png
%doc %{_docdir}/%{name}/RIST_vs_SRT.png

%files -n rist-tools
%{_bindir}/rist*

%changelog
%autochangelog
