%global source0_hash b39fae47ca85753493cf714ed8099d99652d6cebb880a5ae4f682b3e9be5f6a4
Name:           firewalk
Version:        5.0
Release:        1%{?dist}
Summary:        Active reconnaissance network security tool
License:        BSD
URL:            http://www.packetfactory.net/projects/firewalk/
Source0:        http://www.packetfactory.net/firewalk/dist/%{name}.tar.gz
Patch0:         firewalk-5.0-gcc.patch
Patch1: firewalk-configure-c99.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libdnet-devel
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
# /oreon:deps
%description
Firewalk is an active reconnaissance network security tool that attempts
to determine what layer 4 protocols a given IP forwarding device will pass.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Firewalk
%patch -P0 -p0
%patch -P1 -p1
# Needed for x86_64, automake can't be run here
cp -f %{_datadir}/automake-*/config.* .

%build

%configure
%make_build
%install
%make_install
install -Dp -m 0644 man/firewalk.8 $RPM_BUILD_ROOT%{_mandir}/man8/firewalk.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
