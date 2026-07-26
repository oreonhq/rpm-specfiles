%global source0_hash 3af673876fd21ce5d8089cd2057bb304cd6dc4510e7d94a5d55a53a5e57b681f

Name:           linux-sysinfo-snapshot
Version:        3.7.9.7
Release:        %autorelease
Summary:        System information snapshot tool for Mellanox adapters

License:        BSD-3-Clause
URL:            https://github.com/Mellanox/linux-sysinfo-snapshot
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed

Requires:       python3dist(setuptools)

Recommends:     bridge-utils
Recommends:     dmidecode
Recommends:     dkms
Recommends:     grep
Recommends:     hostname
Recommends:     iproute
Recommends:     iscsi-initiator-utils
Recommends:     kmod
Recommends:     libvirt-client
Recommends:     lldpad
Recommends:     lslw
Recommends:     mdadm
Recommends:     mstflint
Recommends:     net-tools
Recommends:     NetworkManager
Recommends:     numactl
Recommends:     openvswitch
Recommends:     pciutils
Recommends:     util-linux
Recommends:     systemd

%description
Linux Sysinfo Snapshot is a tool designed to take a snapshot of all the
configuration and relevant information on the server and Mellanox's adapters.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix config path
touch -r sysinfo-snapshot.py timestamp
sed -i 's:^DEFAULT_CONFIG_PATH = .*$:DEFAULT_CONFIG_PATH = "%{_sysconfdir}/sysinfo-snapshot/config.csv":' sysinfo-snapshot.py
touch -r timestamp sysinfo-snapshot.py
rm timestamp

%build
# Nothing to build

%install
install -Dpm0755 sysinfo-snapshot.py %{buildroot}/%{_bindir}/sysinfo-snapshot
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/sysinfo-snapshot config.csv

%check
./sysinfo-snapshot.py -v

%files
%license LICENSE
%doc README.md
%{_bindir}/sysinfo-snapshot
%dir %{_sysconfdir}/sysinfo-snapshot
%config(noreplace) %{_sysconfdir}/sysinfo-snapshot/config.csv

%changelog
%autochangelog
