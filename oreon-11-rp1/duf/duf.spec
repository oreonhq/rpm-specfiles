%global source0_hash 1334d8c1a7957d0aceebe651e3af9e1c1e0c6f298f1feb39643dd0bd8ad1e955
%bcond check 1
%global goipath         github.com/muesli/duf
Version:                0.9.1
%gometa -L -f
Name:           duf
Release:        1%{?dist}
Summary:        Disk Usage/Free Utility - a better 'df' alternative
License:        Apache-2.0 AND BSD-3-Clause AND MIT
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
Disk Usage/Free Utility - a better 'df' alternative.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/duf %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                       %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/duf %{buildroot}%{_bindir}/
install -m 0755 -vd                       %{buildroot}%{_mandir}/man1
cp -a duf.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
