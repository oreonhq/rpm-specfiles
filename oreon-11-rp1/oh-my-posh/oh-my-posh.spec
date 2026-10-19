%global source0_hash f0f5b1598d20f062ea9fa015b06c42abb9fc7b09c55402c6f757b71c8c2e4eb4
%bcond check 1
%global goipath         github.com/jandedobbeleer/oh-my-posh
Version:                 28.10.0
%gometa -L -f
Name:           oh-my-posh
Release:        1%{?dist}
Summary:        The most customisable and low-latency cross platform/shell prompt renderer
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0 AND Unicode-DFS-2016 AND (FTL OR GPL-2.0-or-later)
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
# /oreon:deps
%description
The most customisable and low-latency cross platform/shell prompt renderer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X github.com/jandedobbeleer/oh-my-posh/src/build.Version=%{version}  \
                   -X github.com/jandedobbeleer/oh-my-posh/src/build.Date=$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)"
cd src
  %gobuild -o %{gobuilddir}/bin/oh-my-posh
cd ..
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
cd src
%gotest $(go list ./... | awk '!/(upgrade|segments|config)/ {print $1}')
cd ..
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
