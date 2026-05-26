Name: redfish-finder 
Version: 0.4
Release: %autorelease
Summary: Utility for parsing SMBIOS information and configuring canonical BMC access
ExclusiveArch: x86_64 aarch64

%define debug_package %{nil}

License: GPL-2.0-or-later
URL: https://github.com/nhorman/redfish-finder
Source:        https://github.com/nhorman/redfish-finder/archive/refs/tags/v0.4.tar.gz

# Fix shabang python interpreter: https://github.com/nhorman/redfish-finder/commit/59fc5f964bf6971da552d059520d7798fccbd4fc
Patch0: redfish-finder-python3.patch

# Fix parsing HostConfig for DHCP: https://github.com/nhorman/redfish-finder/commit/581327fd45351dd53c06a26517bb7f92e19d8f31
Patch1: hostconfig-dhcp-parse.patch

# Fix DHCP mode: https://github.com/nhorman/redfish-finder/commit/c624c9dfe03c0e066eea1240b4b9ca8f3ed07eb8
Patch2: fix-dhcp-mode.patch

# Support AutoConfig mode: https://github.com/nhorman/redfish-finder/commit/f6248933605e051992e5a0c29b2c9753e0dc4e76
Patch3: support-autoconf-mode.patch

BuildRequires: systemd-rpm-macros

Requires: python3
Requires: NetworkManager
Requires: dmidecode

%description
Scans Smbios information for type 42 management controller information, and uses
that to configure the appropriate network interface so that the BMC is
canonically accessible via the host name redfish-localhost

%prep
%autosetup

%build
#noop here

%install
install -D -p -m 0755 redfish-finder %{buildroot}/%{_bindir}/redfish-finder
install -D -p -m 0644 redfish-finder.1 %{buildroot}/%{_mandir}/man1/redfish-finder.1
install -D -p -m 0644 ./redfish-finder.service %{buildroot}/%{_unitdir}/redfish-finder.service

%post
%systemd_post redfish-finder.service

%preun
%systemd_preun redfish-finder.service

%postun
%systemd_postun_with_restart redfish-finder.service


%files
%doc README.md
%license COPYING
%{_bindir}/redfish-finder
%{_mandir}/man1/redfish-finder.1.*
%{_unitdir}/redfish-finder.service


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4-1
- Prepare for Oreon 11 (RP1)
