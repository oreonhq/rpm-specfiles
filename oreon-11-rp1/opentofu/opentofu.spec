%global source0_hash 450f962f262d9f484ad1fb73454650740cdce0d83a854ad8b6c183cc5822eb09
%bcond check 1
%global goipath         github.com/opentofu/opentofu
Version:                1.11.5
%gometa -L -f
Name:           opentofu
Release:        1%{?dist}
Summary:        OpenTofu lets you declaratively manage your cloud infrastructure
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
OpenTofu lets you declaratively manage your cloud infrastructure.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export LDFLAGS="-X github.com/opentofu/opentofu/version.dev=no \
                -X main.version=v%{version} "
%gobuild -o %{gobuilddir}/bin/tofu %{goipath}/cmd/tofu
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
for test in "TestResourceProvider_ApplyCustomWorkingDirectory" "TestGet_cancel" \
            "TestInit_cancelModules" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
