%global source0_hash 5903c029ef3fc98e17e4209450df554819ceee548b3a6eeb6d55983a1d55843c

%global modulesdir %%(pkg-config --variable=modulesdir libcrypto)

Summary: OpenSSL provider for IBMCA
Name: openssl-ibmca
Version: 2.5.0
Release: 3%{?dist}
License: Apache-2.0
URL: https://github.com/opencryptoki
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# post GA fixes
#Patch0: %%{name}-%%{version}-fixes.patch
Requires: libica >= 4.0.0
BuildRequires: make
BuildRequires: gcc
BuildRequires: libica-devel >= 4.0.0
BuildRequires: automake libtool
BuildRequires: openssl >= 3.0.5
BuildRequires: perl(FindBin)
ExclusiveArch: s390 s390x


%description
A dynamic OpenSSL provider for IBMCA crypto hardware on IBM Z machines
to accelerate cryptographic operations.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

./bootstrap.sh


%build
%configure --disable-engine --enable-provider --libdir=%{modulesdir} --with-libica-cex --with-libica-version=4
%make_build


%install
%make_install
rm -f %{buildroot}%{modulesdir}/*.la

# remove generated sample configs
rm -rf %{buildroot}%{_datadir}/%{name}


%check
make check


%files
%license LICENSE
%doc ChangeLog README.md
%doc src/provider/ibmca-provider-opensslconfig
%{modulesdir}/ibmca-provider.so
%{_mandir}/man5/ibmca-provider.5*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.0-3
- Import
