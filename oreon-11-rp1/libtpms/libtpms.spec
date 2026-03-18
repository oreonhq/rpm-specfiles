Name:           libtpms
Version:        0.10.2
Release:        3%{?dist}
Summary:        Library providing Trusted Platform Module (TPM) functionality
License:        BSD-3-Clause AND LicenseRef-TCGL

URL:            https://github.com/stefanberger/libtpms
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/v%{version}.tar.gz.asc#/%{name}-%{version}.tar.gz.asc
# https://github.com/stefanberger.gpg
Source2:        gpgkey-B818B9CADF9089C2D5CEC66B75AD65802A0B4211.asc

Patch0001:      0001-Fix-a-compilation-error-in-TPMLIB_GetPlaintext.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sed

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Include files for libtpms
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description   devel
Libtpms header files and documentation.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --with-tpm2 --with-openssl
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' -print -delete

%check
make check

%ldconfig_scriptlets

%files
%license LICENSE
%doc README CHANGES
%{_libdir}/%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/TPM*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.2-3
- Prepare for Oreon 11 (RP1)
