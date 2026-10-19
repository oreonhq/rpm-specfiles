%global source0_hash 4ff37c733cad1b27e67b747db8ba16cdc31038a899896f26fc51c4520f9f31ed
%bcond check 1
%global goipath         golang.org/x/vuln
%global forgeurl        https://github.com/golang/vuln
Version:                1.1.4
%global commit          a9cf566971d512048614ae269b160fe47a1fceb3
%gometa -L -f
Name:           govulncheck
Release:        1%{?dist}
Summary:        Database client and tools for the Go vulnerability database
Provides: golang-x-vuln = %{version}-%{release}
Obsoletes: golang-x-vuln < 1.1.4-1
License:        Apache-2.0 AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/vuln-%{commit}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
govulncheck is a command-line tool that scans Go code and binaries for known
vulnerabilities using the Go vulnerability database. It only surfaces
vulnerabilities in functions that your code actually calls.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/govulncheck %{goipath}/cmd/govulncheck
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2 -F -s TestGoModTidy -s TestHeaders -s TestCommand
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
