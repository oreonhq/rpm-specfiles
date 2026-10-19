%global source0_hash 16dfed4e45ed1ee3e31d1c7166bebd803c0bfc4e110e02cad41f7ba7dde8e56f
%bcond check 1
%global goipath         github.com/prometheus/prom2json
Version:                1.5.0
%gometa -L -f
%global common_description %{expand:
A tool to scrape a Prometheus client and dump the result as JSON.}
Name:           golang-github-prometheus-prom2json
Release:        1%{?dist}
Summary:        A tool to scrape a Prometheus client and dump the result as JSON
License:        Apache-2.0 AND BSD-3-Clause AND ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/prom2json-%{version}.tar.gz
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

%gobuild -o %{gobuilddir}/bin/prom2json %{goipath}/cmd/prom2json
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
