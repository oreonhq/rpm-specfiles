%global source0_hash 45fc28a6ff3c7a359d4448132ca190f0a9c760540c445dba4597a5b71de40f68

Name:           libcacard
Version:        2.8.2
Release:        1%{?dist}
Summary:        CAC (Common Access Card) library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.freedesktop.org/spice/libcacard
Source0:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz
Source1:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz.sha256sum
Source3:        db2.crypt
Epoch:          3

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  nss-devel
BuildRequires:  softhsm
BuildRequires:  opensc
BuildRequires:  gnutls-utils
BuildRequires:  nss-tools
BuildRequires:  openssl
BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pcsc-lite-devel
Conflicts:      qemu-common < 2:2.5.0

%description
This library provides emulation of smart cards to a virtual card
reader running in a guest virtual machine.

It implements DoD CAC standard with separate pki containers
(compatible coolkey), using certificates read from NSS.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
pushd $(dirname %{SOURCE0})
sha256sum -c %{SOURCE1}
popd
%setup -q
cp %{SOURCE3} tests/

%build
%meson
%meson_build

%check
# Do not run the tests on s390x, which fails
%ifnarch s390x
%meson_test
%endif

%install
%meson_install

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libcacard.so.*

%files devel
%{_includedir}/cacard
%{_libdir}/libcacard.so
%{_libdir}/pkgconfig/libcacard.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.2-1
- Prepare for Oreon 11 (RP1)
