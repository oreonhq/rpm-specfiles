%global source0_hash 14d46cc60f38998bccb6d6cda020048340bb9e0bc0afabbd77ff89b6bb05ccdb

Summary:        Library with simple API for communication with LXI devices
Name:           liblxi
Version:        1.22
Release:        4%{?dist}
# src/vxi11core* and src/include/vxi11core* are EPICS, rest is BSD-3-Clause
License:        BSD-3-Clause AND EPICS
URL:            https://lxi-tools.github.io/
Source0:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxi/liblxi/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/101BAC1C15B216DBE07A3EEA2BDB4A0944FA00B1
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.53.2
BuildRequires:  %{_bindir}/rpcgen
BuildRequires:  libtirpc-devel
BuildRequires:  avahi-devel
BuildRequires:  libxml2-devel

%description
The LXI library (liblxi) is an open source software library for GNU/Linux
systems which offers a simple API for communicating with LXI enabled
instruments. The API allows applications to easily discover instruments on
networks and communicate SCPI commands.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%{_libdir}/%{name}.so.1*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lxi.h
%{_mandir}/man3/lxi_*.3*

%changelog
%autochangelog
