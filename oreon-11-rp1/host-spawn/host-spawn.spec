%global source0_hash 77be74180d3c14cdf6199e2f5d77ad5a732b5902beecfdb81a3760038862af43
%bcond check 1
%global goipath         github.com/1player/host-spawn
Version:                1.6.2
%gometa -L -f
Name:           host-spawn
Release:        1%{?dist}
Summary:        Run commands on your host from inside your toolbox or flatpak sandbox
License:        BSD-2-Clause AND BSD-3-Clause AND MIT-0
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
Run commands on your host from inside your toolbox or flatpak sandbox.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/host-spawn %{goipath}
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
