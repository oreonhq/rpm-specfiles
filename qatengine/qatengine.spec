# SPDX-License-Identifier: MIT

# Build as an OpenSSL provider instead of as an engine
%bcond provider %[0%{?fedora} >= 41 || 0%{?rhel} >= 10]
# QAT_HW only acceleration for RHEL
%bcond sw %{undefined rhel}

# Define the directory where the OpenSSL engines are installed
%if %{with provider}
%global modulesdir %(pkg-config --variable=modulesdir libcrypto)
%else
%global enginesdir %(pkg-config --variable=enginesdir libcrypto)
%endif

Name:           qatengine
Version:        2.0.0
Release:        3%{?dist}
Summary:        Intel QuickAssist Technology (QAT) OpenSSL Engine

# Most of the source code is BSD, with the following exceptions:
# - qat.txt, qat_err.h & qat_err.c files are Apache License 2.0
License:        BSD-3-Clause
URL:            https://github.com/intel/QAT_Engine
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1909065
ExclusiveArch:  x86_64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  qatlib-devel >= 23.02.0
%if !0%{?rhel}
BuildRequires:  intel-ipp-crypto-mb-devel >= 1.0.6
BuildRequires:  intel-ipsec-mb-devel >= 2.0
%endif
BuildRequires:  openssl

%description
This package provides the Intel QuickAssist Technology OpenSSL Engine
(an OpenSSL Plug-In Engine) which provides cryptographic acceleration
for both hardware and optimized software using Intel QuickAssist Technology
enabled Intel platforms.

%prep
%autosetup -n QAT_Engine-%{version}

%build
autoreconf -ivf
%configure %{?with_sw:--enable-qat_sw} %{?with_provider:--enable-qat_provider}
%make_build

%install
%make_install

%if 0%{?rhel}
find %{buildroot} -name "*.la" -delete
%endif

%check
%if %{with provider}
export OPENSSL_MODULES=%{buildroot}%{modulesdir}
openssl list -providers -provider qatprovider
%else
export OPENSSL_ENGINES=%{buildroot}%{enginesdir}
openssl engine -v %{name}
%endif

%files
%license LICENSE*
%doc README.md docs*
%if %{with provider}
%{modulesdir}/qatprovider.so
%else
%{enginesdir}/%{name}.so
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-3
- Prepare for Oreon 11 (RP1)
