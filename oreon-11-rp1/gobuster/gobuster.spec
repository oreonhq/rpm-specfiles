%global source0_hash 6919232eafbd0c4bbc9664d7f434b6a8d82133aa09f1400341ef6985ceff208a
%bcond check 1
%global goipath         github.com/OJ/gobuster/v3
Version:                3.8.2
%gometa -L -f
Name:           gobuster
Release:        1%{?dist}
Summary:        Directory/File, DNS and VHost busting tool written in Go
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://github.com/OJ/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
Directory/File, DNS and VHost busting tool written in Go.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/gobuster %{goipath}
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
