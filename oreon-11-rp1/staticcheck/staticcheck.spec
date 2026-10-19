%global source0_hash ed3723fa5d6093622de2d2a6464ee4a82a54d5f6daad1f3c3f005261d1a598c5
%bcond check 1
%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                2026.1
%global tag             2026.1
%gometa -L -f
Name:           staticcheck
Release:        1%{?dist}
Summary:        The advanced Go linter
License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{version}/go-tools-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Obsoletes:      golang-honnef-tools < 2023.1.3-13
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Staticcheck - The advanced Go linter.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/staticcheck %{goipath}/cmd/staticcheck
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
