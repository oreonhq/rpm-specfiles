%global source0_hash b07c28c6c4bdafa272073a310b75bc22c49da8904585a89c30e5ca4233e63843
%bcond check 1
%global goipath         filippo.io/age
%global forgeurl        https://github.com/FiloSottile/age
Version:                1.3.2
%gometa -L -f
Name:           age
Release:        1%{?dist}
Summary:        Simple, modern and secure encryption tool
License:        BSD-3-Clause AND (0BSD OR CC0-1.0 OR Unlicense)
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
A simple, modern and secure encryption tool (and Go library) with small
explicit keys, no config options, and UNIX-style composability.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
GO_LDFLAGS="-X main.Version=%{version}"
for cmd in cmd/{age,age-keygen,age-inspect} ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/
install -m 644 doc/age-keygen.1 %{buildroot}%{_mandir}/man1/
install -m 644 doc/age-inspect.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
