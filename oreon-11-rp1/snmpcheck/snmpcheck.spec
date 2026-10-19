%global source0_hash 298d7f065af57440b0af029b015adbd71597ae892caf0cea3bf4b14293ee9a42
Name:           snmpcheck
Version:        1.9
Release:        22%{?dist}
Summary:        An utility to get information via SNMP protocols
License:        GPL-3.0-or-later
URL:            https://www.nothink.org/codes/snmpcheck/
Source0:        https://www.nothink.org/codes/snmpcheck/%{name}-%{version}.rb
Source1:        snmpcheck.1
BuildArch:      noarch
Requires:       ruby(release)
Requires:       rubygem(snmp)
# oreon:deps

# /oreon:deps
%description
snmpcheck supports the following enumerations:
   * Contact
   * Description
   * Devices
   * Domain
   * Hardware and storage information
   * Hostname
   * IIS statistics
   * IP forwarding
   * Listening UDP ports
   * Location
   * Motd
   * Mountpoints
   * Network interfaces
   * Network services
   * Processes
   * Routing information
   * Software components (Windows programs or RPMs etc.)
   * System Uptime
   * TCP connections
   * Total Memory
   * Uptime
   * User accounts
   * Web server information (IIS)

%prep

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
