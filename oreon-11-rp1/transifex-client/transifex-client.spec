%global source0_hash 759320acd621991046533089bb77320202853cc97b860ab7783040d0e4d5e34f
%bcond check 1
%global goipath         github.com/transifex/cli
Version:                1.6.17
%gometa -L -f
%global common_description %{expand:
The Transifex Command-line Client is a command line tool that enables
you to easily manage your translations within a project without the
need of an elaborate UI system.}
Name:           transifex-client
Release:        1%{?dist}
Summary:        Command line tool for Transifex translation management
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND LGPL-3.0-only AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cli-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch:          0001-fix-simplify-error-formatting-to-satisfy-Go-1.24-vet.patch
Patch:          0001-Remove-autoupdate-feature.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/tx %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
