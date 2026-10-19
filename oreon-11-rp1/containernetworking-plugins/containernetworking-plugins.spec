%global source0_hash 34bd82d47e981940751619c9cc44c095bb90bfcaf8d71865cbb822c37690a764
%global source1_hash none
%bcond check 1
%global goipath         github.com/containernetworking/plugins
Version:                1.9.1
%gometa -L -f
%global common_description %{expand:
Reference and example networking plugins, maintained by the CNI team.}
Name:           containernetworking-plugins
Release:        1%{?dist}
Summary:        Reference and example networking plugins, maintained by the CNI team
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://github.com/containernetworking/plugins/archive/v1.9.1/plugins-1.9.1.tar.gz#/containernetworking-plugins-1.9.1.tar.gz
Source2:        go-vendor-tools.toml
ExclusiveArch: %{golang_arches}
Requires:       systemd
Obsoletes:      containernetworking-cni < 0.7.1-2
Provides:       containernetworking-cni = %{version}-%{release}
Provides:       kubernetes-cni
Provides:       container-network-stack = 1
# oreon:deps
BuildRequires:  go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-devel
# /oreon:deps
%description
%{common_description}
The CNI (Container Network Interface) project consists of a specification
and libraries for writing plugins to configure network interfaces in Linux
containers, along with a number of supported plugins. CNI concerns itself
only with network connectivity of containers and removing allocated resources
when the container is deleted.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%goprep -A
%global gomodulesmode GO111MODULE=on
GO111MODULE=on go mod vendor

%build

for cmd in \
   plugins/ipam/dhcp \
   plugins/ipam/host-local \
   plugins/ipam/static \
   plugins/main/bridge \
   plugins/main/dummy \
   plugins/main/host-device \
   plugins/main/ipvlan \
   plugins/main/loopback \
   plugins/main/macvlan \
   plugins/main/ptp \
   plugins/main/tap \
   plugins/main/vlan \
   plugins/meta/bandwidth \
   plugins/meta/firewall \
   plugins/meta/portmap \
   plugins/meta/sbr \
   plugins/meta/tuning \
   plugins/meta/vrf \
   plugins/sample; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_libexecdir}/cni
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}/%{_libexecdir}/cni/
install -dp %{buildroot}%{_unitdir}
install -p plugins/ipam/dhcp/systemd/cni-dhcp.service %{buildroot}%{_unitdir}
install -p plugins/ipam/dhcp/systemd/cni-dhcp.socket  %{buildroot}%{_unitdir}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck -d plugins/main/windows -t plugins -d pkg/ip -d pkg/ipam -d pkg/ns -t pkg/utils
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.1-1
- Import
