%global source0_hash 6cc922d2241e10968d8985b2a8a8abe1328d8bd0ebcf5f7741d8387022436f00
%bcond check 1
%global goipath         github.com/sibprogrammer/xq
Version:                1.4.0
%gometa -L -f
Name:           xq
Release:        1%{?dist}
Summary:        Command-line XML and HTML beautifier and content extractor
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
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
Command-line XML and HTML beautifier and content extractor.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X main.commit=fedora \
                -X main.version=%{version} \
                -X main.date=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)"
%gobuild -o %{gobuilddir}/bin/xq %{goipath}/
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mv ./docs/%{name}.man ./docs/%{name}.1
install -Dpm 0644 ./docs/%{name}.1 -t %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
