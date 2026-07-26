%global source0_hash 1839ed5bbb6e562b6fc3078a43108380f49de81ea8f373981936514bbf33b20d

Name:           nmbscan
Version:        1.2.6
Release:        34%{?dist}
Summary:        NMB/SMB network scanner

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://nmbscan.g76r.eu/
Source0:        http://nmbscan.g76r.eu/down/%{name}-%{version}.tar.gz
Source1:        %{name}.1

# Remove dependency on deprecated arp tool, use ip neigh instead
Patch0:         %{name}-1.2.6-arp.patch

# rhbz#2279884 - Use grep -E instead of egrep to avoid using the grep alias
Patch1:         %{name}-1.2.6-egrep.patch

BuildArch:      noarch

Requires:       bind-utils
Requires:       iputils
Requires:       iproute
Requires:       samba-client

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

%autosetup -c %{name}-%{version}

%build
# Nothing to build

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 nmbscan %{buildroot}%{_bindir}/
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files
%doc Documentation/HOWTO_contribute.txt
%license Documentation/gplv2.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
