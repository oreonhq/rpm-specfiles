%global source0_hash b491ae9a444f5f4cb925913dfa12ad7a2bcd8aa149114df7afb2fa921359b6e1
%bcond check 1
%global goipath         github.com/rootless-containers/rootlesskit/v2
Version:                2.3.6
%gometa -L -f
Name:           rootlesskit
Release:        1%{?dist}
Summary:        Linux-native "fake root" for implementing rootless containers
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://github.com/rootless-containers/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Provides:       golang-github-rootless-containers-rootlesskit = %{version}-%{release}
Obsoletes:      golang-github-rootless-containers-rootlesskit < 1.0.1-15
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
Linux-native "fake root" for implementing rootless containers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -p1
tar -xf %{S:1}

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
%gotest ./... -skip 'TestBuiltIn/Test(TCP|UDP)4?'
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
