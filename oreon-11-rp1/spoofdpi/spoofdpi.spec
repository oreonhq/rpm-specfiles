%global source0_hash 75a3af546374a2a0c54bed5e13685e9b851a5d7580251851c060c6fc8716d5e9
%bcond check 1
%global goipath         github.com/xvzc/SpoofDPI
Version:                1.2.1
%gometa -L -f
Name:           spoofdpi
Release:        1%{?dist}
Summary:        Simple and fast anti-censorship tool written in Go
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/SpoofDPI-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       libpcap
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  libpcap-devel
# /oreon:deps
%description
Simple and fast anti-censorship tool written in Go.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
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
