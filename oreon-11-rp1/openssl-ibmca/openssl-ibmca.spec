%global source0_hash 5903c029ef3fc98e17e4209450df554819ceee548b3a6eeb6d55983a1d55843c
%global modulesdir %%(pkg-config --variable=modulesdir libcrypto)
Summary:        OpenSSL provider for IBMCA
Name: openssl-ibmca
Version: 2.5.0
Release:        3%{?dist}
License: Apache-2.0
URL: https://github.com/opencryptoki
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: libica >= 4.0.0
ExclusiveArch: s390 s390x
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libica-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  perl(FindBin)
# /oreon:deps
%description
A dynamic OpenSSL provider for IBMCA crypto hardware on IBM Z machines
to accelerate cryptographic operations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

./bootstrap.sh

%build

%configure --disable-engine --enable-provider --libdir=%{modulesdir} --with-libica-cex --with-libica-version=4
%make_build
%install
%make_install
rm -f %{buildroot}%{modulesdir}/*.la
rm -rf %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
