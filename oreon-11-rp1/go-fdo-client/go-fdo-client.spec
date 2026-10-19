%global source0_hash 0007ccf532c6702213732f6971f8b1545ce52ed7c4ba9091ed76e5041a5ac53e
%bcond check 1
%global goipath         github.com/fido-device-onboard/go-fdo-client
%global with_debug 1
%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package %{nil}
%endif
Version:        1.0.0
%gometa -L -f
Name:           go-fdo-client
Release:        1%{?dist}
Summary:        FIDO FDO compliant device on-boarding tool
License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
go-fdo-client is the device-side implementation of FIDO Device Onboard
specification in Go. It provides an FDO client that interacts with
FDO manufacturer and owner servers to perform device on-boarding.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
#%%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GOEXPERIMENT="nodwarf5"
export GO_LDFLAGS="-X %{goipath}/internal/version.VERSION=%{version}"
%gobuild -o %{gobuilddir}/bin/go-fdo-client %{goipath}
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
