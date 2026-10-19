%global source0_hash 5975f940740dd816057ab3cf20cebde3ece3250891952a566f8555f73fb67b21
%bcond check 1
%global goipath         git.sr.ht/~xenrox/hut
%global forgeurl        https://git.sr.ht/~xenrox/hut
%global version0        0.7.0
%global tag             v%{version0}
%gometa -L -f
Name:           hut
Version:        %{forgeversion}
Release:        1%{?dist}
Summary:        A CLI tool for Sourcehut
License:        AGPL-3.0-only AND Apache-2.0 AND BSD-3-Clause AND LGPL-3.0-or-later WITH LGPL-3.0-linking-exception AND MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}.tar.gz#/%{name}-%{version0}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Patch:          0001-Set-CLI-command-for-git-webhook-create-to-lower-case.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  scdoc
# /oreon:deps
%description
hut is a CLI tool for interacting with Sourcehut instances. It supports
git.sr.ht as well as self-hosted Sourcehut instances.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%global gomodulesmode GO111MODULE=on
GO_LDFLAGS="-X main.version=v%{version}"
%gobuild -o hut %{goipath}
%make_build doc/hut.1 completions
%install
%go_vendor_license_install -c %{S:2}
%make_install PREFIX=%{_prefix}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
