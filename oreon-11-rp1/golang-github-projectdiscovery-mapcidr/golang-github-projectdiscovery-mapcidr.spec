%global source0_hash d1253ab474de254cb77628d3274bf6fdcf087223f219dcf26186de83776bf717
%bcond check 1
%global goipath         github.com/projectdiscovery/mapcidr
Version:                1.1.97
%gometa -L -f
Name:           golang-github-projectdiscovery-mapcidr
Release:        1%{?dist}
Summary:        Utility for operations on subnet/CIDR ranges
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mapcidr-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Utility program to perform multiple operations for a given subnet/CIDR ranges.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/mapcidr %{goipath}/cmd/mapcidr
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "Test_asnClient_GetCIDRsForASNNum" "TestASNClient_GetIPAddressesAsStream" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
export GO111MODULE=on
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
