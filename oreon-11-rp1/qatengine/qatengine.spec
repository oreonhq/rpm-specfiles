%global source0_hash 5a457b1ee186e6e4b5c8cb27660dd60a527e5620786b3764ebaf9d877ea3be33
%bcond provider %[0%{?fedora} >= 41 || 0%{?rhel} >= 10]
%bcond sw %{undefined rhel}
%if %{with provider}
%global modulesdir %(pkg-config --variable=modulesdir libcrypto)
%else
%global enginesdir %(pkg-config --variable=enginesdir libcrypto)
%endif
Name:           qatengine
Version:        2.2.0
Release:        1%{?dist}
Summary:        Intel QuickAssist Technology (QAT) OpenSSL Engine
License:        BSD-3-Clause
URL:            https://github.com/intel/QAT_Engine
Source0:        https://github.com/intel/QAT_Engine/archive/refs/tags/v%{version}.tar.gz#/qatengine-%{version}.tar.gz
ExclusiveArch:  x86_64
%if !0%{?rhel} || (0%{?oreon} >= 11)
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intel-ipp-crypto-mb-devel
BuildRequires:  intel-ipsec-mb-devel
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  qatlib-devel
# /oreon:deps
%description
This package provides the Intel QuickAssist Technology OpenSSL Engine
(an OpenSSL Plug-In Engine) which provides cryptographic acceleration
for both hardware and optimized software using Intel QuickAssist Technology
enabled Intel platforms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir QAT_Engine-%{version}
%oreon_prep
%build

autoreconf -ivf
%configure %{?with_sw:--enable-qat_sw} %{?with_provider:--enable-qat_provider}
%make_build
%install
%make_install
%if 0%{?rhel} || (0%{?oreon} >= 11)
find %{buildroot} -name "*.la" -delete
%oreon_autofiles main
%endif
%check

%if %{with provider}
export OPENSSL_MODULES=%{buildroot}%{modulesdir}
openssl list -providers -provider qatprovider
%else
export OPENSSL_ENGINES=%{buildroot}%{enginesdir}
openssl engine -v %{name}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-1
- Import
