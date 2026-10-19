%global source0_hash 1839ed5bbb6e562b6fc3078a43108380f49de81ea8f373981936514bbf33b20d
Name:           nmbscan
Version:        1.2.6
Release:        1%{?dist}
Summary:        NMB/SMB network scanner
License:        GPL-2.0-only
URL:            http://nmbscan.g76r.eu/
Source0:        http://nmbscan.g76r.eu/down/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Patch0:         %{name}-1.2.6-arp.patch
Patch1:         %{name}-1.2.6-egrep.patch
BuildArch:      noarch
Requires:       bind-utils
Requires:       iputils
Requires:       iproute
Requires:       samba-client
# oreon:deps

# /oreon:deps
%description
Scans a SMB shares network, using NMB and SMB protocols. Useful to acquire
an information on a local area network (security audit, etc.)

Matches the information such as NMB/SMB/Windows host name, IP address,
IP host name, Ethernet MAC address, Windows user name,
NMB/SMB/Windows domain name and master browser.

Can discover all NMB/SMB/Windows hosts on a local area network thanks to 
hosts lists maintained by master browsers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 nmbscan %{buildroot}%{_bindir}/
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
