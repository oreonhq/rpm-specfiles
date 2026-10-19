%global source0_hash 546fe0bc72fff119126676abfa8f26ce5a1a239e85bc2ed52ee78866e12a431f
%global srcname Ultimarc-linux
Name:           ultimarc
Version:        1.2.0
Release:        1%{?dist}
Summary:        Library and command line utility to configure Ultimarc boards
License:        GPL-2.0-only
URL:            https://github.com/katie-snow/Ultimarc-linux
Source0:        https://github.com/katie-snow/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libtool
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
# /oreon:deps
%description
This utility will configure the following Ultimarc boards: ServoStik, PACDrive,
IPAC Ultimate, I-Pac 2, I-Pac 4, Mini-Pac, JPAC, UltraStik 360, PacLED64, U-HID
and U-HID Nano. There is support for the PAC 2015 boards, UltraStik 2015 board
and the previous generation of the PAC boards. It uses JSON configuration files
to configure the different boards. It also supports the ability to change the
device ID of the UltraStik 360 boards, allowing for the configuring of four
different boards at once.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Shared libraries for %{name}
%description    libs
Libraries to configure Ultimarc boards.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# collate JSON config examples
mkdir examples
cp -P src/umtool/*.json examples

%build

./autogen.sh
%configure --disable-static
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/libultimarc.la
mkdir -p %{buildroot}%{_udevrulesdir}
cp -P 21-ultimarc.rules %{buildroot}%{_udevrulesdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ultimarc-devel -f %{oreon_filedir}/ultimarc-devel.list
%files -n ultimarc-libs -f %{oreon_filedir}/ultimarc-libs.list

%changelog

%autochangelog
