%global source1_hash d46ca0f3943929a0e22cf7dede7a501932d5b08af0c59395cdadd6c983031a4c
%global source0_hash 45fc28a6ff3c7a359d4448132ca190f0a9c760540c445dba4597a5b71de40f68
Name:           libcacard
Version:        2.8.2
Release:        1%{?dist}
Summary:        CAC (Common Access Card) library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://gitlab.freedesktop.org/spice/libcacard
Source0:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz
Source1:        http://www.spice-space.org/download/libcacard/%{name}-%{version}.tar.xz.sha256sum
Source3:        db2.crypt
Epoch:          3
Conflicts:      qemu-common < 2:2.5.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gnutls-utils
BuildRequires:  meson
BuildRequires:  nss-devel
BuildRequires:  nss-tools
BuildRequires:  opensc
BuildRequires:  openssl
BuildRequires:  pcsc-lite-devel
BuildRequires:  softhsm
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
pushd $(dirname %{SOURCE0})
sha256sum -c %{SOURCE1}
popd
%setup -q
cp %{SOURCE3} tests/

%build

%meson
%meson_build
%check

%ifnarch s390x
%meson_test
%endif
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcacard-devel -f %{oreon_filedir}/libcacard-devel.list

%changelog

%autochangelog
