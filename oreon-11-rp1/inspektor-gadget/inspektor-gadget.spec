%global source0_hash d2b6b65c4cdc8b543b01567b745522f63bb7f437ce907e76d9c7668bc68cd045
%global goipath         github.com/inspektor-gadget/inspektor-gadget
Version:                0.49.0
%gometa -L -f
Name:           inspektor-gadget
Release:        1%{?dist}
Summary:        Tools and framework for data collection and system inspection using eBPF
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only WITH Linux-syscall-note AND ISC AND MIT AND MPL-2.0
URL:            %{gourl}
ExcludeArch:    ppc64le ppc64 s390x
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.xz
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Inspektor Gadget is a collection of tools (or gadgets) to debug and inspect
Kubernetes resources and applications.
It manages the packaging, deployment and execution of eBPF programs in a
Kubernetes cluster, including many based on BCC tools, as well as some
developed specifically for use in Inspektor Gadget.
It automatically maps low-level kernel primitives to high-level Kubernetes
resources, making it easier and quicker to find the relevant information.

This package contains ig, the local CLI flavor of Inspektor Gadget.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
# Required to unpack vendor on top of main
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global currentgoldflags ""
export GO_LDFLAGS="-X %{goipath}/internal/version.version=v%{version} \
  -X %{goipath}/cmd/common/image.builderImage=ghcr.io/inspektor-gadget/gadget-builder:v%{version}"
export GO_BUILDTAGS="netgo"
go build %{gobuildflags} -o %{gobuilddir}/bin/ig %{goipath}/cmd/ig
%install
%go_vendor_license_install -c %{SOURCE2}
mkdir -p "%{buildroot}/%{_bindir}"
install -D -m0755 %{gobuilddir}/bin/ig %{buildroot}/%{_bindir}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{SOURCE2}
set -e
set -o pipefail
if [ -d /sys/kernel/debug/tracing ]; then
  sleep inf &
  sleep_pid=$!
  ./bin/build/ig snapshot process --host | grep -qP "sleep\s+${sleep_pid}"
  kill $sleep_pid
else
  echo "Skipping ig check as prerequisites are not satisfied in the chroot"
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
