%global source0_hash 322f0c200887c2b0e6c412c70ad5de741a30e7687028966cfe26aa7534218369
%bcond check 1
%global gomodulesmode GO111MODULE=on
%global goipath         github.com/projectdiscovery/chaos-client
Version:                0.5.2
%gometa -L -f
%global common_description %{expand:
Go client to communicate with Chaos DB API.}
Name:           golang-github-projectdiscovery-chaos-client
Release:        1%{?dist}
Summary:        Go client to communicate with Chaos DB API
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ICU AND ISC AND MIT AND MPL-2.0 AND Unlicense
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/chaos-client-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/chaos %{goipath}/cmd/chaos
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
export GO111MODULE=on
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
