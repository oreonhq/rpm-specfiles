%global source0_hash 9a65ccafa62066192153d3143cae74ed230f78cea6f089fa49483e56d15a82ac
Name:           linux-sysinfo-snapshot
Version:        3.8.0.0
Release:        1%{?dist}
Summary:        System information snapshot tool for Mellanox adapters
License:        BSD-3-Clause
URL:            https://github.com/Mellanox/linux-sysinfo-snapshot
Source0:        https://github.com/Mellanox/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
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
# oreon:deps
BuildRequires:  python3
BuildRequires:  python3dist(setuptools)
BuildRequires:  sed
# /oreon:deps
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

%install
install -Dpm0755 sysinfo-snapshot.py %{buildroot}/%{_bindir}/sysinfo-snapshot
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/sysinfo-snapshot config.csv
%oreon_autofiles main

%check

./sysinfo-snapshot.py -v
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
