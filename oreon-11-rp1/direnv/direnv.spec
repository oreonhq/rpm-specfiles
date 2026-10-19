%global source0_hash 4142fbb661f3218913fac08d327c415e87b3e66bd0953185294ff8f3228ead24
%bcond check 1
%global goipath         github.com/direnv/direnv/v2
Version:                2.37.1
%gometa -L -f
Name:           direnv
Release:        1%{?dist}
Summary:        Per-directory shell configuration tool
License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  /usr/bin/go-md2man
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description
direnv augments existing shells with a new feature that can load and unload
environment variables depending on the current directory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
%gobuild -o %{gobuilddir}/bin/direnv %{goipath}
find man/ -name "*.md" -exec sh -c 'go-md2man -in="{}" -out="$(echo "{}" | sed "s|\.md||g")"' \;
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0755 -vp man/*.1             %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
