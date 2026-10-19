%global source0_hash 3eb02708b671a35de25797ceff5fdc2010827d6ec8273df84dc02f0ed2147853
%bcond check 1
%global goipath         github.com/liquidweb/liquidweb-cli
Version:                0.7.0
%gometa -L -f
%global common_description %{expand:
Official command line interface for the LiquidWeb API.}
Name:           lw-cli
Release:        1%{?dist}
Summary:        Official command line interface for the LiquidWeb API
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/liquidweb-cli-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
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

%gobuild -o %{gobuilddir}/bin/liquidweb-cli %{goipath}
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck -d github.com/liquidweb/liquidweb-cli/cmd
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
